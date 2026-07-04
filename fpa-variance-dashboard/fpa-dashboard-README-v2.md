# FP&A Revenue Dashboard

## Business Problem
Regional and departmental leadership need a self-service way to check budget vs. actual revenue performance without waiting on a manual monthly report — and finance needs a single source of truth that flags underperforming regions automatically.

## Dataset
18 months (Jan-25–Jun-26) of Budget and Actual revenue across 4 UK regions (London, Manchester, Birmingham, Leeds) and 4 business lines (Retail Sales, Wholesale, Online Sales, Foodservice). 288 rows total.

## Tools Used
Excel (SUMIFS dynamic filtering, Data Validation dropdowns, conditional formatting, native charts).

## Key Insights
- **Full-period revenue variance:** tracked within a tight band of budget across all regions
- **London and Manchester** contribute the largest share of both budget and actual revenue, making them the highest-priority regions for variance monitoring
- **Automated insight formulas** surface the best-performing region and the region needing attention without manual lookup — turning a static report into a decision-support tool

## Dashboard Preview
![FP&A Revenue Dashboard](./fpa-revenue-dashboard-screenshot.jpg)

## Key Features
- Interactive Region and Department filters — every KPI and chart updates live
- KPI cards for Total Budget, Actual, Variance (£/%) with automatic green/red conditional formatting
- Monthly trend chart that responds to filter selection
- Regional performance comparison chart (fixed, full-year view)
- Department revenue mix pie chart
- Automated insights: best-performing region, region needing attention, top department by revenue

## Files
- `fpa-revenue-dashboard.xlsx` — the full interactive dashboard (open the **Dashboard** tab)
- `revenue_budget_data_gbp.csv` — underlying dataset
- `fpa-revenue-dashboard-screenshot.jpg` — dashboard preview image

## How to Use
1. Open the workbook in Excel and go to the **Dashboard** tab
2. Use the Region and Department dropdowns (cells C5 and F5) to filter — KPIs and the trend chart update instantly
3. Regional comparison, department mix, and insights reflect the full dataset regardless of filter
