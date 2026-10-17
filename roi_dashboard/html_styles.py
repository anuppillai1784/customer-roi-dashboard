STYLES = """
:root {
  --bg: #111514;
  --surface: #182020;
  --line: #2c3634;
  --text: #e6ece8;
  --muted: #9aa7a1;
  --hours: #6fb5a6;
  --roi: #e2ab4c;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 16px/1.5 -apple-system, "Helvetica Neue", Arial, sans-serif;
}
main { max-width: 1040px; margin: 0 auto; padding: 32px 16px 56px; }
h1, h2 { font-family: Georgia, "Times New Roman", serif; font-weight: 400; }
h1 { font-size: 2rem; margin: 0 0 8px; }
h2 {
  font-size: 1.3rem;
  margin: 40px 0 14px;
  padding-top: 20px;
  border-top: 1px solid var(--line);
}
.lede { color: var(--muted); max-width: 64ch; margin: 0 0 16px; }
.notice {
  margin: 0;
  padding: 10px 14px;
  border-left: 3px solid var(--roi);
  background: var(--surface);
  color: var(--muted);
}
.table-wrap { overflow-x: auto; background: var(--surface); }
table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
th, td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--line);
  text-align: right;
  vertical-align: top;
}
th:nth-child(-n+2), td:nth-child(-n+2) { text-align: left; }
thead th { color: var(--muted); font-size: 0.8rem; font-weight: 600; }
tr.total td, tr.total th { font-weight: 600; }
.roi { color: var(--roi); font-size: 1.05rem; white-space: nowrap; }
.basis {
  display: block;
  max-width: 30ch;
  margin-left: auto;
  color: var(--muted);
  font-size: 0.75rem;
  line-height: 1.35;
  white-space: normal;
}
.chart { display: block; width: 100%; height: auto; background: var(--surface); }
.chart .label, .chart .value { font-size: 13px; fill: var(--text); }
.chart .value { fill: var(--muted); }
.chart .bar { fill: var(--hours); }
.rules { color: var(--muted); padding-left: 20px; }
.rules li { margin: 6px 0; }
footer { margin-top: 40px; color: var(--muted); font-size: 0.8rem; }
@media (max-width: 600px) {
  main { padding: 24px 16px 40px; }
  h1 { font-size: 1.6rem; }
}
"""
