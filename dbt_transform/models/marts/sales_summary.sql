{{ config(materialized='table') }}

WITH staging_sales AS (
    SELECT * FROM {{ ref('stg_sales') }}
),

daily_summary AS (
    SELECT 
        sale_date,
        COUNT(*) AS number_of_transactions,
        SUM(quantity) AS total_quantity_sold,
        SUM(total) AS total_revenue,
        AVG(total) AS average_transaction_value,
        COUNT(DISTINCT product) AS unique_products_sold
    FROM staging_sales
    GROUP BY sale_date
),

product_summary AS (
    SELECT 
        product,
        COUNT(*) AS times_sold,
        SUM(quantity) AS total_quantity,
        SUM(total) AS total_revenue,
        AVG(price) AS average_price
    FROM staging_sales
    GROUP BY product
)

SELECT 
    'daily' AS summary_type,
    sale_date::text AS dimension,
    number_of_transactions AS metric_1,
    total_revenue AS metric_2,
    average_transaction_value AS metric_3
FROM daily_summary

UNION ALL

SELECT 
    'product' AS summary_type,
    product AS dimension,
    times_sold AS metric_1,
    total_revenue AS metric_2,
    average_price AS metric_3
FROM product_summary
