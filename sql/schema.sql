CREATE TABLE dim_customer (
    customer_key INTEGER PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    customer_segment VARCHAR(50)
);

CREATE TABLE fact_order (
    order_key INTEGER PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL,
    customer_key INTEGER NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(14,2),
    status VARCHAR(30),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
);

CREATE INDEX idx_fact_order_date ON fact_order(order_date);
