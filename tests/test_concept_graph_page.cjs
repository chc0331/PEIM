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
  dispatch(name) { if (this.listeners[name]) this.listeners[name]({}); }
}

test("첫 화면에서 모든 주제를 보여주고 선택 후 다시 돌아갈 수 있다", async () => {
  const names = ["search", "search-hint", "results", "summary", "graph-pane", "graph", "graph-caption", "graph-title", "details", "built-at", "overview", "depth-control", "overview-note", "detail-legend"];
  const elements = Object.fromEntries(names.map(name => [name, new Element()]));
  const depth = new Element();
  depth.value = "1";
  const document = {
    getElementById: id => elements[id],
    createElement: () => new Element(),
    createTextNode: text => { const node = new Element(); node.textContent = text; return node; },
    querySelector: () => depth,
    querySelectorAll: () => [depth]
  };
  const node = (id, label, file) => ({id, label, aliases: [], description: "", file_type: "concept", source_file: `wiki/concepts/${file}.md`});
  const nodes = [node("data", "데이터 거버넌스", "data"), node("tls", "TLS 1.3", "tls"), node("norm", "정규화", "normalization"), node("detail", "데이터 품질", "data")];
  for (let i = 0; i < 14; i++) nodes.push(node(`extra${i}`, `부가 개념 ${i}`, "data"));
  const graph = {
    built_at: "2026-11-10",
    nodes,
    topic_ids: ["data", "tls", "norm"],
    edges: [
      {source: "data", target: "detail", relation: "references", confidence: "EXTRACTED"},
      {source: "detail", target: "tls", relation: "references", confidence: "EXTRACTED"}
    ]
  };
  const networks = [];
  class Network {
    constructor(container, data) { this.data = data; networks.push(this); }
    destroy() {}
    once() {}
    on() {}
    setOptions() {}
    fit() {}
    moveTo() {}
  }
  const vis = {Network};
  const context = {document, window: {vis, matchMedia: () => ({matches: false})}, vis, fetch: async () => ({ok: true, json: async () => graph}), console};
  const source = fs.readFileSync(path.join(__dirname, "../site/concept-graph/app.js"), "utf8");
  vm.runInNewContext(source, context);
  await new Promise(resolve => setTimeout(resolve, 0));

  assert.match(elements["graph-caption"].textContent, /전체/);
  assert.equal(networks.at(-1).data.nodes.length, 3);
  assert.equal(networks.at(-1).data.edges.length, 1);
  assert.equal(networks.at(-1).data.edges[0].from, "data");
  assert.equal(networks.at(-1).data.edges[0].to, "tls");
  assert.equal(elements.results.children.length, 3);

  const dataButton = elements.results.children.map(li => li.children[0]).find(button => button.textContent.includes("데이터 거버넌스"));
  dataButton.dispatch("click");
  assert.match(elements["graph-caption"].textContent, /^데이터 거버넌스/);
  assert.equal(networks.at(-1).data.nodes.length, 2);
  elements.overview.dispatch("click");
  assert.match(elements["graph-caption"].textContent, /전체/);

  elements.search.value = "부가";
  elements.search.dispatch("input");
  assert.equal(elements.results.children.length, 14);
});
