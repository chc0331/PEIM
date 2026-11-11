"use strict";

const WIKI_BASE_URL = "https://github.com/chc0331/PEIM/blob/main/";
const RELATED = {
  conceptually_related_to: "관련",
  references: "참조",
  cites: "인용",
  implements: "구현",
  rationale_for: "근거",
  shares_data_with: "데이터 공유"
};
const elements = {
  search: document.getElementById("search"),
  hint: document.getElementById("search-hint"),
  results: document.getElementById("results"),
  summary: document.getElementById("summary"),
  graphPane: document.getElementById("graph-pane"),
  graph: document.getElementById("graph"),
  caption: document.getElementById("graph-caption"),
  graphTitle: document.getElementById("graph-title"),
  overview: document.getElementById("overview"),
  depthControl: document.getElementById("depth-control"),
  overviewNote: document.getElementById("overview-note"),
  detailLegend: document.getElementById("detail-legend"),
  details: document.getElementById("details"),
  builtAt: document.getElementById("built-at")
};
let data;
let nodesById;
let adjacent;
let selectedId;
let network;

function norm(value) {
  return String(value || "").normalize("NFKC").toLocaleLowerCase("ko-KR");
}

function textNode(tag, content, className) {
  const el = document.createElement(tag);
  el.textContent = content;
  if (className) el.className = className;
  return el;
}

function resultButton(node) {
  const li = document.createElement("li");
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = node.label;
  button.setAttribute("aria-current", String(node.id === selectedId));
  const alias = (node.aliases || []).find(value => norm(value) !== norm(node.label));
  if (alias) button.appendChild(textNode("small", alias));
  button.addEventListener("click", () => select(node.id, true));
  li.appendChild(button);
  return li;
}

function searchResults() {
  const q = norm(elements.search.value.trim());
  elements.results.replaceChildren();
  let matches;
  if (q) {
    matches = data.nodes.map(node => {
      const labels = [node.label, ...(node.aliases || [])].map(norm);
      const score = labels.includes(q) ? 0 : labels.some(value => value.startsWith(q)) ? 1 : labels.some(value => value.includes(q)) ? 2 : 3;
      return {node, score};
    }).filter(item => item.score < 3).sort((a, b) => a.score - b.score || a.node.label.localeCompare(b.node.label, "ko")).map(item => item.node);
  } else {
    matches = data.topic_ids.map(id => nodesById.get(id)).filter(Boolean).sort((a, b) => a.label.localeCompare(b.label, "ko"));
  }
  elements.hint.textContent = q ? `검색 결과 ${matches.length}개` : `전체 주제 ${matches.length}개 · 목록을 스크롤하세요`;
  if (!matches.length) elements.results.appendChild(textNode("li", "일치하는 개념이 없습니다.", "hint"));
  matches.forEach(node => elements.results.appendChild(resultButton(node)));
}

function neighborhood(id, depth) {
  const seen = new Set([id]);
  let frontier = [id];
  for (let step = 0; step < depth; step++) {
    const next = [];
    for (const current of frontier) {
      for (const neighbor of adjacent.get(current) || []) {
        if (!seen.has(neighbor)) {
          seen.add(neighbor);
          next.push(neighbor);
        }
      }
    }
    frontier = next;
  }
  return seen;
}

function relationLabel(edge) {
  return RELATED[edge.relation] || edge.relation.replaceAll("_", " ");
}

function showOverview() {
  selectedId = null;
  elements.search.value = "";
  searchResults();
  elements.graphTitle.textContent = "전체 주제 지도";
  elements.depthControl.hidden = true;
  elements.overviewNote.hidden = false;
  elements.detailLegend.hidden = true;

  const topics = data.topic_ids.map(id => nodesById.get(id)).filter(Boolean);
  const topicByFile = new Map(topics.map(node => [node.source_file, node.id]));
  const links = new Map();
  for (const edge of data.edges) {
    const from = topicByFile.get(nodesById.get(edge.source).source_file);
    const to = topicByFile.get(nodesById.get(edge.target).source_file);
    if (!from || !to || from === to) continue;
    const key = JSON.stringify([from, to]);
    links.set(key, {from, to});
  }
  elements.caption.textContent = `전체 주제 ${topics.length}개 · 문서 간 연결 ${links.size}개`;
  elements.graph.setAttribute("aria-label", `전체 주제 ${topics.length}개와 문서 간 연결 ${links.size}개. 목록에서도 주제를 선택할 수 있습니다.`);
  elements.details.replaceChildren(
    textNode("h3", "주제를 선택하세요", "node-title"),
    textNode("p", "목록이나 지도에서 주제를 선택하면 관련 개념을 자세히 볼 수 있습니다. 검색창에서는 세부 개념도 찾을 수 있습니다.", "description")
  );

  if (network) network.destroy();
  if (!window.vis || !window.vis.Network) {
    elements.graph.replaceChildren(textNode("p", "그래프 라이브러리를 불러오지 못했습니다. 주제 목록과 검색은 이용할 수 있습니다.", "graph-error"));
    return;
  }

  const startingFiles = ["data-governance.md", "tls13.md", "devops-cicd.md", "relational-normalization.md", "ai-governance.md", "cloud-computing.md"];
  const rank = node => {
    const index = startingFiles.indexOf(node.source_file.replace("wiki/concepts/", ""));
    return index === -1 ? startingFiles.length : index;
  };
  topics.sort((a, b) => rank(a) - rank(b) || a.label.localeCompare(b.label, "ko"));
  const compact = elements.graph.clientWidth < 600;
  const labelLimit = compact ? 10 : 18;
  let x = 0, y = 0, dx = 1, dy = 0, length = 1, progress = 0, turns = 0;
  const displayNodes = topics.map(node => {
    const position = {x: x * (compact ? 160 : 250), y: y * 100};
    x += dx;
    y += dy;
    if (++progress === length) {
      progress = 0;
      [dx, dy] = [-dy, dx];
      if (++turns % 2 === 0) length++;
    }
    return {
      id: node.id,
      label: node.label.length > labelLimit ? `${node.label.slice(0, labelLimit - 1)}…` : node.label,
      title: node.label,
      ...position,
      shape: "dot",
      size: 14,
      color: {background: "#397fa8", border: "#ffffff"},
      font: {color: "#14263d", size: 14, face: "sans-serif", strokeWidth: 5, strokeColor: "#ffffff"},
      borderWidth: 2
    };
  });
  const displayEdges = [...links.values()].map((edge, index) => ({
    id: index, ...edge, arrows: {to: {enabled: true, scaleFactor: 0.5}},
    color: {color: "rgba(40, 91, 125, 0.14)", hover: "#176a9c"}, width: 1
  }));
  network = new vis.Network(elements.graph, {nodes: displayNodes, edges: displayEdges}, {
    autoResize: true,
    interaction: {hover: true, navigationButtons: true, keyboard: true},
    layout: {improvedLayout: false},
    physics: false
  });
  network.moveTo({position: {x: 0, y: 0}, scale: 0.8});
  network.on("click", event => {
    if (event.nodes.length) select(event.nodes[0]);
  });
}

function showGraph() {
  const focus = nodesById.get(selectedId);
  const depth = Number(document.querySelector('input[name="depth"]:checked').value);
  const visible = neighborhood(selectedId, depth);
  const edges = data.edges.filter(edge => visible.has(edge.source) && visible.has(edge.target));
  elements.caption.textContent = `${focus.label} · ${visible.size}개 노드 · ${edges.length}개 연결`;
  elements.graph.setAttribute("aria-label", `${focus.label}에서 ${depth}단계까지의 관련 개념 ${visible.size}개와 연결 ${edges.length}개`);
  if (network) network.destroy();
  if (!window.vis || !window.vis.Network) {
    elements.graph.replaceChildren(textNode("p", "그래프 라이브러리를 불러오지 못했습니다. 오른쪽 관련 개념 목록은 이용할 수 있습니다.", "graph-error"));
    return;
  }
  const displayNodes = [...visible].map(id => {
    const node = nodesById.get(id);
    const selected = id === selectedId;
    const document = node.file_type === "document";
    return {
      id,
      label: node.label,
      title: node.label,
      shape: "dot",
      size: selected ? 25 : document ? 14 : 17,
      color: {background: selected ? "#e5a545" : document ? "#8394a5" : "#397fa8", border: selected ? "#9d6416" : "#ffffff"},
      font: {color: "#14263d", size: selected ? 16 : 13, face: "sans-serif", strokeWidth: 5, strokeColor: "#ffffff"},
      borderWidth: 2
    };
  });
  const displayEdges = edges.map((edge, index) => ({
    id: index,
    from: edge.source,
    to: edge.target,
    arrows: "to",
    title: `${relationLabel(edge)} · ${edge.confidence}`,
    color: {color: "#9db1c0", hover: "#176a9c"},
    width: 1.5
  }));
  network = new vis.Network(elements.graph, {nodes: displayNodes, edges: displayEdges}, {
    autoResize: true,
    interaction: {hover: true, navigationButtons: true, keyboard: true},
    layout: {improvedLayout: true},
    physics: {stabilization: {iterations: 150}, barnesHut: {gravitationalConstant: -3800, springLength: 140}}
  });
  network.once("stabilized", () => {
    network.setOptions({physics: false});
    network.fit({animation: {duration: 300}});
  });
  network.on("click", event => {
    if (event.nodes.length) select(event.nodes[0]);
  });
}

function showDetails() {
  const node = nodesById.get(selectedId);
  const panel = elements.details;
  panel.replaceChildren();
  panel.appendChild(textNode("h3", node.label, "node-title"));
  panel.appendChild(textNode("span", node.review_status || node.document_status, "status"));
  panel.appendChild(textNode("p", node.description || "이 노드의 별도 설명은 기준 위키에서 확인할 수 있습니다.", "description"));
  const source = textNode("p", "위키 문서: ", "meta");
  const link = document.createElement("a");
  link.href = WIKI_BASE_URL + node.source_file.split("/").map(encodeURIComponent).join("/");
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = node.source_file.replace("wiki/concepts/", "");
  source.appendChild(link);
  if (node.source_location) source.appendChild(document.createTextNode(` · ${node.source_location}`));
  panel.appendChild(source);
  panel.appendChild(textNode("h3", "직접 연결된 개념"));
  const relations = data.edges.filter(edge => edge.source === selectedId || edge.target === selectedId);
  const list = document.createElement("ul");
  list.className = "relation-list";
  relations.sort((a, b) => (nodesById.get(a.source === selectedId ? a.target : a.source).label).localeCompare(nodesById.get(b.source === selectedId ? b.target : b.source).label, "ko"));
  for (const edge of relations) {
    const outgoing = edge.source === selectedId;
    const other = nodesById.get(outgoing ? edge.target : edge.source);
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `${outgoing ? "→" : "←"} ${other.label}`;
    button.appendChild(textNode("small", `${relationLabel(edge)} · ${edge.confidence === "EXTRACTED" ? "문서에 명시된 연결" : edge.confidence === "INFERRED" ? "추론된 연결" : "불확실한 연결"}`));
    button.addEventListener("click", () => select(other.id, true));
    li.appendChild(button);
    list.appendChild(li);
  }
  panel.appendChild(list);
}

function select(id, revealGraph = false) {
  selectedId = id;
  elements.graphTitle.textContent = "관련 개념";
  elements.depthControl.hidden = false;
  elements.overviewNote.hidden = true;
  elements.detailLegend.hidden = false;
  searchResults();
  showDetails();
  showGraph();
  if (revealGraph && window.matchMedia("(max-width: 690px)").matches) elements.graphPane.scrollIntoView({block: "start"});
}

async function start() {
  try {
    const response = await fetch("./graph-data.json", {cache: "no-store"});
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    data = await response.json();
    nodesById = new Map(data.nodes.map(node => [node.id, node]));
    adjacent = new Map(data.nodes.map(node => [node.id, new Set()]));
    for (const edge of data.edges) {
      adjacent.get(edge.source).add(edge.target);
      adjacent.get(edge.target).add(edge.source);
    }
    elements.summary.textContent = `${data.topic_ids.length.toLocaleString("ko-KR")}개 주제 · 전체 노드 ${data.nodes.length.toLocaleString("ko-KR")}개 · 연결 ${data.edges.length.toLocaleString("ko-KR")}개`;
    elements.builtAt.textContent = `그래프 빌드: ${data.built_at}`;
    elements.search.addEventListener("input", searchResults);
    elements.overview.addEventListener("click", showOverview);
    document.querySelectorAll('input[name="depth"]').forEach(input => input.addEventListener("change", showGraph));
    showOverview();
  } catch (error) {
    elements.summary.textContent = "개념 데이터를 불러오지 못했습니다.";
    elements.graph.replaceChildren(textNode("p", `페이지 데이터를 확인해 주세요: ${error.message}`, "graph-error"));
  }
}

start();
