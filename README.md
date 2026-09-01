# Azure Data Factory Parameterized Data Ingestion & Databricks Transformation Pipeline

## Project Overview
This project demonstrates an end-to-end Azure Data Engineering pipeline built using Azure Data Factory (ADF), Azure Data Lake Storage Gen2, Azure Databricks, and PySpark.
The project started with a parameterized data ingestion pipeline and was later upgraded to dynamically discover and process multiple files and perform data transformation using Azure Databricks and PySpark.
The pipeline is designed to process different input files without creating separate pipelines or datasets for each file.

## Project Evolution
The project was developed incrementally:

### V1 - Parameterized Data Ingestion
Implemented parameterized datasets and pipelines to process different sales files using a dynamic `fileName` parameter.

### V2 - Dynamic File Processing
Added Lookup and ForEach activities to dynamically discover available files and process multiple files using the same pipeline.

### V3 - Databricks & PySpark Transformation
Integrated Azure Databricks with Azure Data Factory and added PySpark-based data cleansing and transformation.

## What the Pipeline Does
The pipeline reads sales CSV files from the Azure Data Lake Storage Gen2 `raw` container.

Example files:
- `sales_jan.csv`
- `sales_feb.csv`
- `sales_mar.csv`

The pipeline dynamically discovers the available files using a Lookup activity and processes each file using a ForEach activity.
The files are copied to the curated storage area using an ADF Copy Activity.
After the ingestion stage, Azure Databricks is used to perform data cleansing and transformation using PySpark.

## Pipeline Architecture

```text
Sales CSV Files
       |
       v
Azure Data Lake Storage Gen2
       |
       | Raw Container
       v
Azure Data Factory
       |
       v
Lookup Activity
       |
       v
ForEach Activity
       |
       v
Copy Activity
       |
       v
Azure Databricks
       |
       v
PySpark Transformation
       |
       v
Curated / Transformed Data
Pipeline Flow
Input CSV Files
       |
       v
Parameterized Dataset
       |
       v
Lookup Activity
       |
       v
ForEach Activity
       |
       v
Copy Activity
       |
       v
Azure Databricks Notebook
       |
       v
PySpark Transformation
       |
       v
Curated / Transformed Output
1. Parameterized Dataset

The source dataset uses a filename parameter instead of a hard-coded file name.

Dataset:DS_Raw_Sales

Parameter:FileName

The dataset uses the dynamic expression:@dataset().FileName

This allows the same dataset to process different files.

For example:
sales_jan.csv
sales_feb.csv
sales_mar.csv

can all be processed using the same dataset configuration.

Benefits of Parameterization
Reusable datasets
Reduces duplicate development
Easier maintenance
Supports dynamic file processing
Improves scalability
Avoids hard-coding individual file names

2. Lookup Activity
The Lookup_filelist activity dynamically retrieves the list of available sales files from the source location.
During execution, the Lookup activity identified three files:
sales_jan.csv
sales_feb.csv
sales_mar.csv
This allows the pipeline to discover files dynamically instead of manually specifying each file.

3. ForEach Activity
The ForEach_filelist activity iterates through the files returned by the Lookup activity.
For each file, the Copy Activity is executed.
This allows the same pipeline to process multiple files without creating separate pipelines for each file.

4. Copy Activity
The Copy Activity transfers the source sales files from the raw storage location to the curated storage area.
The Copy Activity runs for each file processed by the ForEach activity.
The pipeline successfully processed the three input files.

5. Azure Databricks Integration
Azure Databricks is integrated with Azure Data Factory for the data transformation stage.
After the ingestion and copy process, the ADF pipeline invokes a Databricks notebook.
The Databricks notebook uses PySpark to perform data cleansing and transformation.

6. PySpark Data Transformation
The Databricks notebook performs data transformation using PySpark.
Data Cleansing
Rows with missing values in important columns are removed.
Example:
df_clean = df.dropna(
    subset=["CustomerID", "OrderID"]
)
Calculated Column

A new column called AmountWithTax is created using the TotalAmount column.
An 18% tax calculation is applied:

df_clean = df_clean.withColumn(
    "AmountWithTax",
    col("TotalAmount") * 1.18
)

The transformed DataFrame is displayed for verification:
display(df_clean)
Example Transformation

For example:
TotalAmount = 55000
After applying 18% tax:
AmountWithTax = 64900

7. Final Output
The transformed data is written back to the curated storage location.
The output contains the processed sales data along with the calculated AmountWithTax column.
Example output location:
curated/
    transformed/
The successful Spark output contains generated files such as:
part-00000-...
and execution marker files such as:
_SUCCESS
_committed_...
_started_...
Pipeline Execution

The complete pipeline was successfully executed.
The execution flow was:
Lookup_filelist
       |
       v
ForEach_filelist
       |
       v
Copy data1
       |
       v
Notebook1

The Lookup activity identified three input files and the subsequent processing activities completed successfully.
Technologies Used
Azure Data Factory
Azure Data Lake Storage Gen2
Azure Databricks
Apache Spark
PySpark
Python
Git
GitHub
Data Engineering Concepts Demonstrated
Data ingestion
Parameterized datasets
Dynamic file processing
Lookup Activity
ForEach Activity
Copy Activity
ADF pipeline orchestration
Azure Data Lake Storage Gen2
Azure Databricks integration
PySpark
Data cleansing
Data transformation
Curated data processing
Managed Identity authentication
Azure RBAC
Git and GitHub version control
