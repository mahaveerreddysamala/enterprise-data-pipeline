-- Monthly revenue and order volume
SELECT order_month,
       COUNT(*) AS orders,
       SUM(net_amount) AS revenue,
       AVG(net_amount) AS avg_order_value
FROM fact_order
GROUP BY order_month
ORDER BY order_month;

-- Customer lifetime value proxy
SELECT customer_key,
       COUNT(*) AS order_count,
       SUM(amount) AS lifetime_revenue,
       MAX(order_date) AS last_order_date
FROM fact_order
GROUP BY customer_key
ORDER BY lifetime_revenue DESC;
