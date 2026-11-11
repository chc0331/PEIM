const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

class Element {
  constructor() { this.children = []; this.attributes = {}; this.listeners = {}; this.value = ""; this._text = ""; }
  set textContent(value) { this._text = String(value); this.children = []; }
  get textContent() { return this._text + this.children.map(child => child.textContent).join(""); }
  appendChild(child) { this.children.push(child); return child; }
  replaceChildren(...children) { this._text = ""; this.children = children; }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  addEventListener(name, handler) { this.listeners[name] = handler; }
  dispatch(name, event = {}) { this.listeners[name]?.(event); }
  focus() { this.focused = true; }
}

const site = path.join(__dirname, "../site/concept-graph");

function fixtureGraph() {
  const node = (id, label, file) => ({id, label, aliases: [], description: "", file_type: "concept", source_file: `wiki/concepts/${file}.md`});
  const nodes = [node("data", "데이터 거버넌스", "data"), node("tls", "TLS 1.3", "tls"), node("norm", "정규화", "normalization"), node("detail", "데이터 품질", "data")];
  for (let i = 0; i < 14; i++) nodes.push(node(`extra${i}`, `부가 개념 ${i}`, "data"));
  return {
    built_at: "2026-11-10",
    nodes,
    topic_ids: ["data", "tls", "norm"],
    edges: [
      {source: "data", target: "detail", relation: "references", confidence: "EXTRACTED"},
      {source: "detail", target: "tls", relation: "references", confidence: "EXTRACTED"}
    ]
  };
}

async function loadPage(graph) {
  const html = fs.readFileSync(path.join(site, "index.html"), "utf8");
  const elements = Object.fromEntries(Array.from(html.matchAll(/\bid="([^"]+)"/g), ([, id]) => [id, new Element()]));
  const depth = new Element();
  depth.value = "1";
  const document = {
    getElementById: id => elements[id],
    createElement: () => new Element(),
    createTextNode: text => { const node = new Element(); node.textContent = text; return node; },
    querySelector: () => depth,
    querySelectorAll: () => [depth]
  };
  const networks = [];
  class Network {
    constructor(container, data) { this.data = data; this.handlers = {}; networks.push(this); }
    destroy() {}
    once() {}
    on(name, handler) { this.handlers[name] = handler; }
    setOptions() {}
    fit() {}
    moveTo() {}
  }
  const vis = {Network};
  const context = {document, window: {vis, matchMedia: () => ({matches: false})}, vis, fetch: async () => ({ok: true, json: async () => graph}), console};
  const source = fs.readFileSync(path.join(site, "app.js"), "utf8");
  vm.runInNewContext(source, context);
  await new Promise(resolve => setTimeout(resolve, 0));
  return {elements, depth, networks};
}

function result(elements, label) {
  return elements.results.children.map(li => li.children[0]).find(button => button?.textContent.startsWith(label));
}

test("이전 데이터는 전체 주제 지도로 열고 모든 노드를 검색할 수 있다", async () => {
  const {elements, networks} = await loadPage(fixtureGraph());
  assert.match(elements["graph-caption"].textContent, /전체/);
  assert.equal(elements["course-view"].hidden, true);
  assert.equal(networks.at(-1).data.nodes.length, 3);
  assert.equal(networks.at(-1).data.edges.length, 1);
  assert.equal(networks.at(-1).data.edges[0].from, "data");
  assert.equal(networks.at(-1).data.edges[0].to, "tls");
  assert.equal(elements.results.children.length, 3);

  result(elements, "데이터 거버넌스").dispatch("click");
  assert.match(elements["graph-caption"].textContent, /^데이터 거버넌스/);
  assert.equal(networks.at(-1).data.nodes.length, 2);
  elements.overview.dispatch("click");
  assert.match(elements["graph-caption"].textContent, /전체/);

  elements.search.value = "부가";
  elements.search.dispatch("input");
  assert.equal(elements.results.children.length, 14);
});

test("과목·단원·주제로 이동하고 묶음 관계와 전체 검색을 이용할 수 있다", async () => {
  const graph = fixtureGraph();
  graph.nodes.push(
    {id: "method", label: "회상 연습", source_file: "wiki/concepts/recall.md"},
    {id: "new", label: "새 주제", source_file: "wiki/concepts/new.md"}
  );
  graph.topic_ids.push("method", "new");
  for (const [source, target] of [["norm", "data"], ["norm", "tls"], ["tls", "detail"]]) {
    graph.edges.push({source, target, relation: "references", confidence: "EXTRACTED"});
  }
  graph.hierarchy = {
    courses: [
      {id: "course-db", label: "데이터베이스", units: [
        {id: "unit-norm", label: "관계형 모델링", topic_ids: ["norm"]},
        {id: "unit-data", label: "데이터 관리", topic_ids: ["data"]}
      ]},
      {id: "course-security", label: "보안", units: [
        {id: "unit-tls", label: "암호와 통신", topic_ids: ["tls"]}
      ]}
    ],
    study_methods: ["method"],
    unclassified: ["new"]
  };
  const {elements, depth, networks} = await loadPage(graph);
  const pathLabels = () => elements["path-items"].children.map(item => item.textContent);
  const current = () => networks.at(-1);

  assert.equal(elements["graph-title"].textContent, "과목 지도");
  assert.match(elements["graph-caption"].textContent, /2개 과목 · 3개 단원 · 전체 주제 5개/);
  assert.equal(elements.results.children.length, 4);
  assert.equal(current().data.edges.length, 0);
  elements["group-links"].dispatch("click");
  assert.equal(elements["group-links"].attributes["aria-pressed"], "true");
  assert.equal(current().data.edges.length, 2);
  assert.equal(current().data.edges.find(edge => edge.from === "course-db" && edge.to === "course-security").title, "개념 연결 2개");
  assert.equal(current().data.edges.find(edge => edge.from === "course-security" && edge.to === "course-db").title, "개념 연결 1개");

  current().handlers.click({nodes: ["course-db"]});
  assert.deepEqual(pathLabels(), ["과목 지도", "데이터베이스"]);
  assert.equal(current().data.edges.length, 1);
  assert.equal(current().data.edges[0].from, "unit-norm");
  assert.equal(current().data.edges[0].to, "unit-data");
  result(elements, "관계형 모델링").dispatch("click", {detail: 0});
  assert.equal(elements.results.focused, true);
  assert.equal(elements["group-links"].hidden, true);
  result(elements, "정규화").dispatch("click");
  assert.deepEqual(pathLabels(), ["과목 지도", "데이터베이스", "관계형 모델링", "정규화"]);
  elements["path-items"].children[2].children[0].dispatch("click");
  assert.equal(elements["graph-title"].textContent, "관계형 모델링");

  elements.search.value = "TLS";
  elements.search.dispatch("input");
  result(elements, "TLS 1.3").dispatch("click");
  assert.deepEqual(pathLabels(), ["과목 지도", "보안", "암호와 통신", "TLS 1.3"]);
  depth.value = "2";
  depth.dispatch("change");
  assert.match(elements.graph.attributes["aria-label"], /2단계/);
  elements.overview.dispatch("click");
  assert.equal(elements["graph-title"].textContent, "전체 주제 지도");
  assert.equal(elements.results.children.length, 5);
  elements["course-view"].dispatch("click");
  result(elements, "학습 방법").dispatch("click");
  assert.equal(elements.results.children.length, 1);
  assert.ok(result(elements, "회상 연습"));
  elements["course-view"].dispatch("click");
  result(elements, "분류 대기").dispatch("click");
  assert.ok(result(elements, "새 주제"));
});
