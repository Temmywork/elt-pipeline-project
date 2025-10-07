{{ config(materialized='view') }}

WITH source_data AS (
    SELECT 
        product,
        quantity,
        price,
        date
    FROM {{ source('raw', 'raw_sales') }}
),

cleaned_data AS (
    SELECT 
        product,
        COALESCE(quantity, 0) AS quantity,
        COALESCE(price, 0) AS price,
        date::date AS sale_date,
        COALESCE(quantity, 0) * COALESCE(price, 0) AS total
    FROM source_data
)

SELECT DISTINCT * FROM cleaned_data
