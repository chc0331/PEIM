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
  courseView: document.getElementById("course-view"),
  overview: document.getElementById("overview"),
  groupLinks: document.getElementById("group-links"),
  path: document.getElementById("graph-path"),
  pathItems: document.getElementById("path-items"),
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
let rootGroup;
let activeGroup;
let showGroupLinks = false;
const topicGroupByFile = new Map();

function norm(value) {
  return String(value || "").normalize("NFKC").toLocaleLowerCase("ko-KR");
}

function textNode(tag, content, className) {
  const el = document.createElement(tag);
  el.textContent = content;
  if (className) el.className = className;
  return el;
}

function listButton(label, subtitle, activate, current = false) {
  const li = document.createElement("li");
  const button = textNode("button", label);
  button.type = "button";
  if (current) button.setAttribute("aria-current", "true");
  if (subtitle) button.appendChild(textNode("small", subtitle));
  button.addEventListener("click", event => {
    activate();
    if (event.detail === 0) elements.results.focus({preventScroll: true});
  });
  li.appendChild(button);
  return li;
}

function groupSummary(group) {
  const topics = `${group.topicIds.length}개 주제`;
  return group.children ? `${group.children.length}개 단원 · ${topics}` : topics;
}

function searchResults() {
  const q = norm(elements.search.value.trim());
  elements.results.replaceChildren();
  if (!q && !selectedId && activeGroup?.children) {
    elements.hint.textContent = activeGroup === rootGroup ? "과목 목록" : `${activeGroup.children.length}개 단원`;
    for (const group of activeGroup.children) {
      elements.results.appendChild(listButton(group.label, groupSummary(group), () => showBrowse(group)));
    }
    return;
  }
  let matches;
  if (q) {
    matches = data.nodes.map(node => {
      const labels = [node.label, ...(node.aliases || [])].map(norm);
      const score = labels.includes(q) ? 0 : labels.some(value => value.startsWith(q)) ? 1 : labels.some(value => value.includes(q)) ? 2 : 3;
      return {node, score};
    }).filter(item => item.score < 3).sort((a, b) => a.score - b.score || a.node.label.localeCompare(b.node.label, "ko")).map(item => item.node);
  } else {
    matches = (activeGroup?.topicIds ?? data.topic_ids).map(id => nodesById.get(id)).filter(Boolean);
    if (!activeGroup) matches.sort((a, b) => a.label.localeCompare(b.label, "ko"));
  }
  elements.hint.textContent = q ? `검색 결과 ${matches.length}개` : `주제 ${matches.length}개`;
  if (!matches.length) elements.results.appendChild(textNode("li", q ? "일치하는 개념이 없습니다." : "이곳에 배치된 주제가 없습니다.", "hint"));
  for (const node of matches) {
    const alias = (node.aliases || []).find(value => norm(value) !== norm(node.label));
    elements.results.appendChild(listButton(node.label, alias, () => select(node.id, true), node.id === selectedId));
  }
}

function loadHierarchy() {
  const hierarchy = data.hierarchy;
  if (!hierarchy) return;
  rootGroup = {label: "과목 지도", children: []};
  for (const {id, label, units} of hierarchy.courses) {
    const course = {id, label, parent: rootGroup};
    course.children = units.map(unit => ({id: unit.id, label: unit.label, topicIds: unit.topic_ids, parent: course}));
    course.topicIds = course.children.flatMap(unit => unit.topicIds);
    rootGroup.children.push(course);
  }
  for (const group of [
    {id: "study-methods", label: "학습 방법", topicIds: hierarchy.study_methods},
    {id: "unclassified", label: "분류 대기", topicIds: hierarchy.unclassified}
  ]) {
    if (group.topicIds.length) rootGroup.children.push({...group, parent: rootGroup});
  }
  for (const group of rootGroup.children) {
    for (const unit of group.children ?? [group]) {
      for (const id of unit.topicIds) topicGroupByFile.set(nodesById.get(id).source_file, unit);
    }
  }
}

function updatePath() {
  elements.courseView.setAttribute("aria-current", activeGroup ? "page" : "false");
  elements.overview.setAttribute("aria-current", !activeGroup && !selectedId ? "page" : "false");
  const path = [];
  for (let group = activeGroup; group; group = group.parent) path.unshift(group);
  if (!activeGroup && rootGroup) path.push(rootGroup, {label: "전체 주제 지도"});
  if (selectedId) path.push(nodesById.get(selectedId));
  elements.path.hidden = path.length < 2;
  elements.pathItems.replaceChildren();
  path.forEach((entry, index) => {
    const li = document.createElement("li");
    if (index === path.length - 1) {
      const current = textNode("span", entry.label);
      current.setAttribute("aria-current", "page");
      li.appendChild(current);
    } else {
      const button = textNode("button", entry.label);
      button.type = "button";
      button.addEventListener("click", event => {
        showBrowse(entry);
        if (event.detail === 0) elements.results.focus({preventScroll: true});
      });
      li.appendChild(button);
    }
    elements.pathItems.appendChild(li);
  });
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

function aggregateLinks(items) {
  const groupByFile = new Map();
  for (const item of items) {
    for (const id of item.topicIds ?? [item.id]) groupByFile.set(nodesById.get(id).source_file, item.id);
  }
  const links = new Map();
  for (const edge of data.edges) {
    const from = groupByFile.get(nodesById.get(edge.source).source_file);
    const to = groupByFile.get(nodesById.get(edge.target).source_file);
    if (!from || !to || from === to) continue;
    const key = JSON.stringify([from, to]);
    const link = links.get(key);
    if (link) link.count++;
    else links.set(key, {from, to, count: 1});
  }
  return [...links.values()];
}

function drawNetwork(nodes, edges, options, open) {
  network?.destroy();
  network = null;
  if (!window.vis?.Network) {
    elements.graph.replaceChildren(textNode("p", "그래프를 불러오지 못했습니다. 목록과 검색으로 탐색할 수 있습니다.", "graph-error"));
    return null;
  }
  network = new window.vis.Network(elements.graph, {nodes, edges}, {
    autoResize: true,
    interaction: {hover: true, navigationButtons: true, keyboard: true},
    ...options
  });
  network.on("click", event => {
    if (event.nodes.length) open(event.nodes[0]);
  });
  return network;
}

function overviewNodes(topics) {
  const startingFiles = ["data-governance.md", "tls13.md", "devops-cicd.md", "relational-normalization.md", "ai-governance.md", "cloud-computing.md"];
  const rank = node => {
    const index = startingFiles.indexOf(node.source_file.replace("wiki/concepts/", ""));
    return index === -1 ? startingFiles.length : index;
  };
  topics.sort((a, b) => rank(a) - rank(b) || a.label.localeCompare(b.label, "ko"));
  const compact = elements.graph.clientWidth < 600;
  const labelLimit = compact ? 10 : 18;
  let x = 0, y = 0, dx = 1, dy = 0, length = 1, progress = 0, turns = 0;
  return topics.map(node => {
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
}

function scopedNodes(items, showTopicCounts) {
  const compact = elements.graph.clientWidth < 520;
  const columns = Math.min(compact ? 2 : 3, Math.max(items.length, 1));
  const rows = Math.ceil(items.length / columns);
  const columnGap = compact ? 160 : 208;
  return items.map((item, index) => {
    const row = Math.floor(index / columns);
    const inRow = Math.min(columns, items.length - row * columns);
    return {
      id: item.id,
      label: showTopicCounts ? `${item.label}\n${item.topicIds.length}개 주제` : item.label,
      title: textNode("span", item.label),
      x: (index % columns - (inRow - 1) / 2) * columnGap,
      y: (row - (rows - 1) / 2) * 86,
      shape: "box",
      margin: 10,
      widthConstraint: {maximum: columnGap - 32},
      borderWidth: 1,
      color: {background: "#eef7fc", border: "#8fb6ce", hover: {background: "#dbeef8", border: "#176a9c"}},
      font: {color: "#14263d", size: 14, face: "sans-serif"}
    };
  });
}

function renderBrowse() {
  const children = activeGroup?.children;
  const items = children ?? (activeGroup?.topicIds ?? data.topic_ids).map(id => nodesById.get(id)).filter(Boolean);
  const links = children && !showGroupLinks ? [] : aggregateLinks(items);
  let caption;
  if (activeGroup && activeGroup === rootGroup) {
    const courses = data.hierarchy.courses;
    const units = courses.reduce((total, course) => total + course.units.length, 0);
    caption = `${courses.length}개 과목 · ${units}개 단원 · 전체 주제 ${data.topic_ids.length}개`;
  } else if (children) {
    caption = groupSummary(activeGroup);
  } else {
    caption = `${activeGroup ? "주제" : "전체 주제"} ${items.length}개 · 문서 간 연결 ${links.length}개`;
  }
  if (children && showGroupLinks) caption += ` · 묶음 간 연결 ${links.length}개`;

  elements.graphTitle.textContent = activeGroup?.label ?? "전체 주제 지도";
  elements.caption.textContent = caption;
  elements.graph.setAttribute("aria-label", `${elements.graphTitle.textContent}. ${caption}. 목록에서도 항목을 선택할 수 있습니다.`);
  elements.groupLinks.hidden = !children;
  elements.groupLinks.setAttribute("aria-pressed", String(showGroupLinks));
  elements.depthControl.hidden = true;
  elements.detailLegend.hidden = true;
  elements.overviewNote.hidden = Boolean(children && !showGroupLinks);
  elements.overviewNote.textContent = children
    ? "같은 방향의 개념 관계를 한 선으로 묶습니다. 선에 마우스를 올리면 관계 수를 볼 수 있습니다."
    : "각 항목은 개념 문서입니다. 선은 서로 다른 문서에 속한 개념 사이의 연결입니다.";

  const displayNodes = activeGroup ? scopedNodes(items, Boolean(children)) : overviewNodes(items);
  const displayEdges = links.map(({from, to, count}, index) => ({
    id: index, from, to, title: `개념 연결 ${count}개`,
    arrows: {to: {enabled: true, scaleFactor: 0.5}},
    color: {color: activeGroup ? "#91aec1" : "rgba(40, 91, 125, 0.14)", hover: "#176a9c"},
    smooth: {type: "curvedCW", roundness: 0.14},
    width: 1
  }));
  const instance = drawNetwork(displayNodes, displayEdges, {
    layout: {improvedLayout: false}, physics: false
  }, id => {
    if (children) showBrowse(children.find(group => group.id === id));
    else select(id);
  });
  if (activeGroup) instance?.fit({animation: false});
  else instance?.moveTo({position: {x: 0, y: 0}, scale: 0.8});
}

function showBrowse(group = null) {
  activeGroup = group;
  selectedId = null;
  elements.search.value = "";
  updatePath();
  searchResults();
  renderBrowse();
  elements.details.replaceChildren(textNode("p", "개념 주제를 열면 설명과 위키 원문을 볼 수 있습니다.", "description"));
}

function showGraph() {
  if (!selectedId) return;
  const focus = nodesById.get(selectedId);
  const depth = Number(document.querySelector('input[name="depth"]:checked').value);
  const visible = neighborhood(selectedId, depth);
  const edges = data.edges.filter(edge => visible.has(edge.source) && visible.has(edge.target));
  elements.caption.textContent = `${focus.label} · ${visible.size}개 노드 · ${edges.length}개 연결`;
  elements.graph.setAttribute("aria-label", `${focus.label}에서 ${depth}단계까지의 관련 개념 ${visible.size}개와 연결 ${edges.length}개`);
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
  const instance = drawNetwork(displayNodes, displayEdges, {
    layout: {improvedLayout: true},
    physics: {stabilization: {iterations: 150}, barnesHut: {gravitationalConstant: -3800, springLength: 140}}
  }, select);
  instance?.once("stabilized", () => {
    instance.setOptions({physics: false});
    instance.fit({animation: {duration: 300}});
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
  activeGroup = topicGroupByFile.get(nodesById.get(id).source_file) ?? rootGroup;
  elements.graphTitle.textContent = "관련 개념";
  elements.groupLinks.hidden = true;
  elements.depthControl.hidden = false;
  elements.overviewNote.hidden = true;
  elements.detailLegend.hidden = false;
  updatePath();
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
    loadHierarchy();
    elements.summary.textContent = `${data.topic_ids.length.toLocaleString("ko-KR")}개 주제 · 전체 노드 ${data.nodes.length.toLocaleString("ko-KR")}개 · 연결 ${data.edges.length.toLocaleString("ko-KR")}개`;
    elements.builtAt.textContent = `그래프 빌드: ${data.built_at}`;
    elements.search.addEventListener("input", searchResults);
    elements.courseView.hidden = !rootGroup;
    elements.courseView.addEventListener("click", () => showBrowse(rootGroup));
    elements.overview.addEventListener("click", () => showBrowse());
    elements.groupLinks.addEventListener("click", () => {
      showGroupLinks = !showGroupLinks;
      renderBrowse();
    });
    document.querySelectorAll('input[name="depth"]').forEach(input => input.addEventListener("change", showGraph));
    showBrowse(rootGroup);
  } catch (error) {
    elements.summary.textContent = "개념 데이터를 불러오지 못했습니다.";
    elements.graph.replaceChildren(textNode("p", `페이지 데이터를 확인해 주세요: ${error.message}`, "graph-error"));
  }
}

start();
