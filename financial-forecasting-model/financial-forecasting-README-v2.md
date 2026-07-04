# Financial Forecasting Model

## Business Problem
Leadership needs to stress-test revenue and profitability assumptions before committing to a budget — understanding not just the "expected" outcome, but the realistic best-case and worst-case range, so capital and hiring decisions aren't built on a single point estimate.

## Dataset
5 years of financial statement data (FY2024A–FY2028E: 2 years actual, 3 years forecast) for a UK FMCG distribution business — driver-based assumptions for growth, margins, working capital, and capex feed a fully linked 3-statement model.

## Tools Used
Excel (formulas, driver-based assumptions, scenario sensitivity tables, native charts) — no macros, fully auditable.

## Key Insights
- **FY2028E Net Income ranges from £2.1M (Worst Case) to £4.2M (Best Case)** against a £3.0M Base Case — a ±31%/+39% sensitivity range driven by just ±6pp growth and ±3pp margin flex
- **Balance sheet ties to £0** across all 5 years — every projected year is fully linked and internally consistent, not just a top-line forecast
- **Revenue compounds from £11.8M to £16.2M** (Base Case) over the forecast period, a 37% cumulative increase

## Dashboard Preview
**Scenario Planning — Best/Base/Worst Case comparison:**
![Scenario Planning](./forecast-scenario-planning-screenshot.jpg)

**Revenue Forecast — Historical + Scenario Projections:**
![Revenue Forecast](./forecast-revenue-chart-screenshot.jpg)

## Structure
| Tab | Purpose |
|---|---|
| `Assumptions` | Base case drivers: growth, margins, working capital days, tax, interest |
| `Income Statement` | Revenue through Net Income, FY2024A–FY2028E |
| `Balance Sheet` | Fully linked; balances to £0 across all 5 years |
| `Cash Flow` | Operating, investing, financing activities, tied to the Balance Sheet |
| `Scenario Planning` | Worst/Base/Best case assumptions and FY2028E output comparison, with chart |
| `Revenue Forecast` | Historical + 3-scenario revenue trajectory, charted |

## Files
- `financial-forecasting-model.xlsx` — the complete model (6 tabs)
- `forecast-scenario-planning-screenshot.jpg`, `forecast-revenue-chart-screenshot.jpg` — preview images

## Notes
Illustrative figures based on a mid-size UK FMCG distribution business (~£11.8M revenue base year). Adjust the Assumptions or Scenario Planning tabs to re-run under different conditions.
