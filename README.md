# E-Commerce Data Engineering Project (Portfolio Version)

This is a simulated version of an enterprise-level e-commerce data pipeline I worked on professionally.  
It demonstrates how to build a scalable, secure, and analytics-ready data platform using Azure.

---

## 🛠 Tools Used

- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics (Notebooks, SQL Pools)
- PySpark
- Delta Lake
- Power BI (for final reporting – not included here)

---

## 🏗️ Architecture

We followed the Medallion Architecture:

### Bronze Layer
- Ingest raw CSV/JSON files from sources into Azure Data Lake (ADLS Gen2)
- Tools: ADF Pipelines

### Silver Layer
- Clean, deduplicate, enrich, and standardize data
- Tools: Synapse Notebooks using PySpark

### Gold Layer
- Aggregate data for reporting (daily sales, top products, etc.)
- Tools: Delta Tables + Synapse SQL Pools

---

## 🔐 Features

- Secure authentication (Service Principal)
- Delta Lake for version control
- Data partitioning and caching for performance
- Logging and error handling

---

## 👨‍💻 My Role

- Designed data models & Medallion Architecture  
- Built ADF pipelines for data ingestion  
- Wrote PySpark code in Synapse for transformation  
- Tuned pipeline performance using partitioning & caching  
- Applied security best practices (RBAC, encryption)

## 📂 Folder Structure

ecommerce-data-engineering/
├── bronze/ # Ingestion layer
├── silver/ # Cleaned and transformed data
├── gold/ # Aggregated data for BI
├── README.md # Project description


> ⚠️ **Note**: This is a simulated project. No confidential code or real client data is used.



