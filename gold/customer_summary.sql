-- customer_summary.sql
-- Aggregated customer insights from Silver Layer

-- Count of unique customers
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(email) AS total_emails,
    COUNT(*) AS total_records
-- Table reference assumes Delta table already written from PySpark job
FROM 
    silver.cleaned_customers;
