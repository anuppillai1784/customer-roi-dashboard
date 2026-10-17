# Customer ROI Dashboard

## What it does

The tool reads usage events for customer departments. It computes tasks automated, hours saved, token spend and ROI for one month. It writes one self-contained HTML dashboard and one JSON report.

## Why it matters

A customer wants to know what automation saves in hours and in dollars. This dashboard answers for each department and shows the assumptions beside each answer.

## Quickstart

You need Python 3.11 or later and nothing else. Run these commands from the repo root.

```sh
python3 -m unittest discover
python3 -m roi_dashboard build --month 2026-09 --out-dir examples
```

The first command runs the tests. The second command writes `examples/roi-2026-09.html` and `examples/roi-2026-09.json`. Without `--out-dir`, the files go to `output/`.

## Repo tree

```text
.gitignore                         # Ignores caches and the output/ folder
LICENSE                            # MIT license
README.md                          # This file
pyproject.toml                     # Project metadata, no dependencies
examples/
  roi-2026-09.html                 # Sample dashboard for September 2026
  roi-2026-09.json                 # Sample report for September 2026
roi_dashboard/
  __init__.py                      # Package marker
  __main__.py                      # Entry point for python3 -m roi_dashboard
  cli.py                           # The build command and its arguments
  config.json                      # Rate, task times, prices, departments, seed
  config.py                        # Loads config.json
  events.py                        # Event record and month filter
  html_assumptions.py              # Assumptions section of the page
  html_chart.py                    # Inline SVG bar chart of hours saved
  html_format.py                   # Number formats and HTML escaping
  html_page.py                     # Page layout
  html_styles.py                   # Page CSS
  html_table.py                    # Department results table
  metrics.py                       # Hours saved, labor value, token spend and ROI
  output.py                        # Writes the HTML and JSON files
  report.py                        # Monthly report, rounding and assumptions
  synthetic.py                     # Seeded synthetic usage events
tests/
  __init__.py                      # Package marker for the test runner
  fixtures.py                      # Hand-built config and events for tests
  test_cli.py                      # Build command and byte-identical output
  test_config.py                   # Config loading
  test_empty_department.py         # Departments with no events
  test_month_filter.py             # Month filter and ROI for one month
  test_render.py                   # Assumptions beside ROI, self-contained page
  test_report.py                   # Report rows, totals and assumptions
  test_roi_math.py                 # ROI math on a hand-computed fixture
  test_synthetic.py                # Seeded event generation
```

## How it works

The config file sets the loaded hourly rate, the baseline and review minutes for each task type, and the price table. It also lists the departments and a fixed random seed. The synthetic module creates usage events for the months in the config. The month filter keeps only the events in the month you request.

Metrics run once for each department. Hours saved sums the net minutes of each automated task, then divides by 60. Net minutes are baseline minutes minus review minutes. Labor value is hours saved multiplied by the loaded hourly rate. Token spend sums the cost of every task, automated or not.

ROI is labor value minus token spend, divided by token spend. When token spend is zero, ROI is null. The report adds the assumptions to the JSON file. The HTML page shows the same assumptions beside every ROI value.

## Sample output

These rows come from `examples/roi-2026-09.json`. Labor value and token spend are in USD.

| Customer | Department | Tasks | Automated | Hours saved | Labor value | Token spend | ROI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Customer A | Finance Operations | 40 | 30 | 19.03 | 1142.00 | 11.3306 | 99.79 |
| Customer A | Customer Support | 40 | 25 | 16.17 | 970.00 | 9.8001 | 97.98 |
| Customer B | Legal | 40 | 24 | 18.25 | 1095.00 | 9.6249 | 112.77 |
| Customer B | Sales Operations | 40 | 26 | 17.17 | 1030.00 | 14.0896 | 72.10 |
| All departments | | 160 | 105 | 70.62 | 4237.00 | 44.8452 | 93.48 |

## Limits

- All data is synthetic. Customer names, department names and usage events are invented.
- The task times, the hourly rate and the prices are illustrative. They are not measured or quoted.
- The price table is not a vendor price list. Real token costs will differ.
- Hours saved assume that each automated task would take the baseline minutes by hand. The tool does not test this assumption.
- Token spend counts input and output tokens only. It does not count infrastructure, support or setup costs.
- ROI values are large because token spend is small next to labor value. Read each ROI value with the assumptions beside it.
- The tool reports one month at a time. It draws events only from the synthetic months in the config.
- The HTML page loads no external files. It needs a modern web browser.
