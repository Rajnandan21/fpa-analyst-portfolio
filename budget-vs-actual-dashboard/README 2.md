
# Budget vs Actual FP&A Dashboard

## Business Problem
Management needs monthly visibility into budget variances and forecast risk — by revenue line, by expense category, and in aggregate — to flag issues early and support confident capital and resourcing decisions.

## Dataset
24 months (Jan-25–Dec-26) of Budget, Actual, and Forecast figures across 4 revenue categories (Retail Sales, Wholesale, Online Sales, Foodservice) and 5 expense categories (COGS, Payroll, Marketing, Logistics, Admin). 216 rows total.

## Tools Used
Excel (SUMIFS dynamic filtering, Data Validation, conditional formatting, native charting), MAPE-based forecast accuracy methodology.

## Key Insights
- **Revenue variance:** +0.02% vs. budget (full period) — effectively on target
- **Expense variance:** -0.08% vs. budget — spend held under control
- **Forecast accuracy improved to 96.1%**, calculated using Mean Absolute Percentage Error (MAPE) — a methodology that avoids positive/negative errors masking true forecast quality
- **Net variance:** +£29,783 favorable against plan across the full period

## Dashboard Preview
![Budget vs Actual Dashboard](./budget-vs-actual-dashboard-screenshot.jpg)

## Executive Summary
[📄 Download the one-page Executive Summary PDF](./budget-vs-actual-executive-summary.pdf)

## Key Features
- Interactive month filter — dropdown instantly recalculates all KPIs
- Revenue & Expense variance KPIs with automatic green/red conditional formatting
- Net variance combining both revenue and expense impact
- Forecast accuracy tracking with dedicated trend chart
- 3 trend charts: Monthly Revenue, Monthly Expense, Forecast Accuracy %
- Full category-level variance breakdown table

## Files
- `budget-vs-actual-dashboard.xlsx` — the full interactive dashboard (open the **Dashboard** tab)
- `budget_actual_forecast_data.csv` — underlying dataset
- `budget-vs-actual-executive-summary.pdf` — one-page executive summary
- `budget-vs-actual-dashboard-screenshot.jpg` — dashboard preview image

## How to Use
1. Open the workbook in Excel and go to the **Dashboard** tab
2. Use the Month dropdown (cell C5) to filter Revenue/Expense KPIs to a single month, or leave on "All" for full-period totals
3. Review monthly trend charts and the full category-level variance breakdown
