-- ============================================================
-- CUSTOMER SEGMENTATION: RFM Analysis
-- (Recency, Frequency, Monetary)
-- ============================================================
-- Classifies each customer into a value segment based on:
--   Recency  = days since last order (lower = better)
--   Frequency = total number of orders (higher = better)
--   Monetary = total spend (higher = better)
-- ============================================================

WITH customer_metrics AS (
    SELECT
        c.customer_id,
        c.customer_name,
        c.business_type,
        c.region,
        JULIANDAY('2026-06-30') - JULIANDAY(MAX(o.order_date)) AS recency_days,
        COUNT(o.order_id) AS frequency,
        ROUND(SUM(o.order_total), 2) AS monetary
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name, c.business_type, c.region
),
scored AS (
    SELECT
        *,
        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM customer_metrics
)
SELECT
    customer_id,
    customer_name,
    business_type,
    region,
    ROUND(recency_days, 0) AS recency_days,
    frequency,
    monetary,
    (r_score + f_score + m_score) AS rfm_total,
    CASE
        WHEN (r_score + f_score + m_score) >= 10 THEN 'Champions'
        WHEN (r_score + f_score + m_score) >= 8  THEN 'Loyal Customers'
        WHEN (r_score + f_score + m_score) >= 6  THEN 'At Risk'
        ELSE 'Churned / Low Value'
    END AS segment
FROM scored
ORDER BY rfm_total DESC;

-- ============================================================
-- SEGMENT SUMMARY: count and average spend per segment
-- ============================================================
WITH customer_metrics AS (
    SELECT
        c.customer_id,
        JULIANDAY('2026-06-30') - JULIANDAY(MAX(o.order_date)) AS recency_days,
        COUNT(o.order_id) AS frequency,
        ROUND(SUM(o.order_total), 2) AS monetary
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id
),
scored AS (
    SELECT
        *,
        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM customer_metrics
),
segmented AS (
    SELECT
        *,
        CASE
            WHEN (r_score + f_score + m_score) >= 10 THEN 'Champions'
            WHEN (r_score + f_score + m_score) >= 8  THEN 'Loyal Customers'
            WHEN (r_score + f_score + m_score) >= 6  THEN 'At Risk'
            ELSE 'Churned / Low Value'
        END AS segment
    FROM scored
)
SELECT
    segment,
    COUNT(*) AS num_customers,
    ROUND(AVG(monetary), 2) AS avg_lifetime_spend,
    ROUND(SUM(monetary), 2) AS total_segment_revenue
FROM segmented
GROUP BY segment
ORDER BY total_segment_revenue DESC;
