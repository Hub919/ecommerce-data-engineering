"""
This PySpark script reads raw customer data from the Bronze Layer,
cleans and transforms it (removes duplicates, trims strings, filters nulls),
and writes the cleaned data to the Silver Layer in Delta format.
"""
# PySpark Script: Clean and Transform Customer Data

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim

# Create Spark session
spark = SparkSession.builder.appName("CustomerDataCleaning").getOrCreate()

# Load raw customer data (CSV format)
raw_df = spark.read.option("header", True).csv("abfss://raw@myecomstorage.dfs.core.windows.net/customers.csv")

# Clean and transform
cleaned_df = raw_df.dropDuplicates() \
                   .withColumn("customer_name", upper(trim(col("customer_name")))) \
                   .withColumn("email", trim(col("email"))) \
                   .filter(col("email").isNotNull())

# Save to Silver Layer (as Delta)
cleaned_df.write.format("delta").mode("overwrite").save("abfss://silver@myecomstorage.dfs.core.windows.net/cleaned_customers")

# Stop Spark session
spark.stop()
