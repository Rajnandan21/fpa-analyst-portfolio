-- ============================================================
-- SCHEMA: UK FMCG Distribution Sales Database
-- ============================================================
-- 4 tables: customers, products, orders, order_lines
-- Illustrative dataset modeled on a cash-and-carry distribution
-- business (similar in structure to Dhamecha Group operations)
-- ============================================================

CREATE TABLE customers (
    customer_id     INTEGER PRIMARY KEY,
    customer_name   TEXT NOT NULL,
    business_type   TEXT,   -- Independent Retailer, Restaurant, Catering Company, Convenience Store, Hotel
    region          TEXT,   -- London, Manchester, Birmingham, Leeds, Bristol
    signup_date     DATE
);

CREATE TABLE products (
    product_id      INTEGER PRIMARY KEY,
    product_name    TEXT NOT NULL,
    category        TEXT,   -- Beverages, Fresh Produce, Frozen Foods, Dry Goods, Household
    unit_price      REAL
);

CREATE TABLE orders (
    order_id        INTEGER PRIMARY KEY,
    customer_id     INTEGER REFERENCES customers(customer_id),
    order_date      DATE,
    order_total     REAL
);

CREATE TABLE order_lines (
    line_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id        INTEGER REFERENCES orders(order_id),
    product_id      INTEGER REFERENCES products(product_id),
    quantity        INTEGER,
    line_total      REAL
);

CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_lines_order ON order_lines(order_id);
CREATE INDEX idx_lines_product ON order_lines(product_id);
