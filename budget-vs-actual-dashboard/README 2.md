# Budget vs Actual FP&A Dashboard

An interactive Excel dashboard tracking monthly Revenue and Expense variance, with forecast accuracy tracking — built to mirror the board-ready variance reporting delivered at Dhamecha Group (UK FMCG distribution).

## Overview
This dashboard covers 24 months (Jan-25\u2013Dec-26) of Budget, Actual, and Forecast data across 4 revenue categories and 5 expense categories, with a live month filter, KPI cards, and forecast accuracy tracking \u2014 the core toolkit of a monthly FP&A reporting cycle.

## Key Features
- **Interactive month filter** \u2014 dropdown selector instantly recalculates all KPIs
- **Revenue variance KPI** \u2014 Budget vs Actual with automatic green/red conditional formatting
- **Expense variance KPI** \u2014 tracks cost overruns/underruns separately from revenue
- **Net variance** \u2014 combined revenue and expense variance impact on the bottom line
- **Forecast accuracy tracking** \u2014 96.1% full-period accuracy, calculated as 1 minus Mean Absolute Percentage Error (MAPE) between forecast and actual
- **3 trend charts**: Monthly Revenue (Budget vs Actual), Monthly Expense (Budget vs Actual), and Forecast Accuracy % over time
- **Variance by category table** \u2014 full-period breakdown across all 9 revenue/expense categories, colour-coded

## Tools Used
- Excel (SUMIFS-driven dynamic filtering, Data Validation dropdowns, conditional formatting, native charts, MAPE-based accuracy calculation)

## Files
- `budget-vs-actual-dashboard.xlsx` \u2014 the full interactive dashboard (open the **Dashboard** tab)
- `budget_actual_forecast_data.csv` \u2014 underlying dataset (216 rows: 24 months \u00d7 9 categories)

## How to Use
1. Open the workbook in Excel and go to the **Dashboard** tab
2. Use the Month dropdown (cell C5) to filter Revenue/Expense KPIs to a single month, or leave on "All" for full-period totals
3. Scroll down to review monthly trend charts and the full category-level variance breakdown
