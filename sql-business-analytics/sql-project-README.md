# SQL Business Analytics Project

A SQL-based sales analytics project covering customer segmentation, revenue KPIs, and product performance — built on a mock sales database modeled on a UK FMCG cash-and-carry distribution business.

## Overview
This project analyzes 2.5 years of transaction data (150 customers, 55 products, 2,458 orders, 7,480 order lines) to answer real FP&A/commercial questions: which customers are most valuable, where is revenue concentrated, and which products drive the business.

## Database Schema
4 tables: `customers`, `products`, `orders`, `order_lines`

```
customers (customer_id, customer_name, business_type, region, signup_date)
products  (product_id, product_name, category, unit_price)
orders    (order_id, customer_id, order_date, order_total)
order_lines (line_id, order_id, product_id, quantity, line_total)
```

## Key Queries
| File | What it does |
|---|---|
| `01_schema.sql` | Table definitions and indexes |
| `02_customer_segmentation.sql` | RFM (Recency, Frequency, Monetary) customer segmentation |
| `03_revenue_kpis.sql` | Revenue by region/category/product, monthly trends, customer LTV, quarterly AOV |

## Sample Results

**Customer Segmentation (RFM)**
| Segment | Customers | Avg Lifetime Spend | Total Revenue |
|---|---|---|---|
| Champions | 48 | £8,748 | £419,925 |
| Loyal Customers | 31 | £4,963 | £153,858 |
| Churned / Low Value | 51 | £1,344 | £68,525 |
| At Risk | 20 | £2,650 | £52,994 |

**Revenue by Region**
| Region | Orders | Customers | Revenue | Avg Order Value |
|---|---|---|---|---|
| London | 734 | 51 | £208,778 | £284.44 |
| Manchester | 567 | 35 | £167,169 | £294.83 |
| Birmingham | 456 | 29 | £124,852 | £273.80 |
| Leeds | 391 | 22 | £109,855 | £280.96 |
| Bristol | 310 | 13 | £84,649 | £273.06 |

## Key Insight
**48 "Champion" customers (32% of the base) generate 63% of total revenue** — a classic Pareto pattern that points directly to where account management and retention effort should be prioritized.

## Tools Used
- SQL (SQLite) — window functions (`NTILE`), CTEs, joins, aggregations
- Python (data generation and query testing via `sqlite3`/`pandas`)

## Files
- `sales_database.db` — the SQLite database
- `01_schema.sql`, `02_customer_segmentation.sql`, `03_revenue_kpis.sql` — query files
- `sample_output_*.csv` — example query results

## How to Use
Open `sales_database.db` with any SQLite client (DB Browser for SQLite, or `sqlite3` CLI), then run the queries in order. All queries were tested and verified against this dataset.
