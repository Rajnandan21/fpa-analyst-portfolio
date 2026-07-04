-- ============================================================
-- REVENUE & KPI ANALYSIS
-- ============================================================

-- 1. Revenue by Region
SELECT
    c.region,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_id) AS active_customers,
    ROUND(SUM(o.order_total), 2) AS total_revenue,
    ROUND(AVG(o.order_total), 2) AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;

-- 2. Revenue by Business Type
SELECT
    c.business_type,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(o.order_total), 2) AS total_revenue,
    ROUND(SUM(o.order_total) * 100.0 / (SELECT SUM(order_total) FROM orders), 1) AS pct_of_total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.business_type
ORDER BY total_revenue DESC;

-- 3. Monthly Revenue Trend
SELECT
    STRFTIME('%Y-%m', order_date) AS month,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(order_total), 2) AS revenue
FROM orders
GROUP BY STRFTIME('%Y-%m', order_date)
ORDER BY month;

-- 4. Top 10 Products by Revenue
SELECT
    p.product_name,
    p.category,
    SUM(ol.quantity) AS total_units_sold,
    ROUND(SUM(ol.line_total), 2) AS total_revenue
FROM order_lines ol
JOIN products p ON ol.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- 5. Revenue by Product Category
SELECT
    p.category,
    SUM(ol.quantity) AS total_units_sold,
    ROUND(SUM(ol.line_total), 2) AS total_revenue,
    ROUND(SUM(ol.line_total) * 100.0 / (SELECT SUM(line_total) FROM order_lines), 1) AS pct_of_total_revenue
FROM order_lines ol
JOIN products p ON ol.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 6. Customer Lifetime Value (Top 10)
SELECT
    c.customer_name,
    c.business_type,
    c.region,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(o.order_total), 2) AS lifetime_value,
    ROUND(AVG(o.order_total), 2) AS avg_order_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.business_type, c.region
ORDER BY lifetime_value DESC
LIMIT 10;

-- 7. New Customer Acquisition by Month
SELECT
    STRFTIME('%Y-%m', signup_date) AS signup_month,
    COUNT(*) AS new_customers
FROM customers
GROUP BY STRFTIME('%Y-%m', signup_date)
ORDER BY signup_month;

-- 8. Average Order Value Trend by Quarter
SELECT
    STRFTIME('%Y', order_date) || '-Q' ||
        ((CAST(STRFTIME('%m', order_date) AS INTEGER) - 1) / 3 + 1) AS quarter,
    COUNT(order_id) AS orders,
    ROUND(AVG(order_total), 2) AS avg_order_value,
    ROUND(SUM(order_total), 2) AS total_revenue
FROM orders
GROUP BY quarter
ORDER BY quarter;
