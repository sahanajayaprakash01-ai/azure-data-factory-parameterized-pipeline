Azure Data Factory Parameterized Data Ingestion Pipeline

Project Overview
This project demonstrates a parameterized data ingestion pipeline built using Azure Data Factory (ADF).
The pipeline is designed to dynamically process different input files using parameters instead of creating separate pipelines or datasets for each file.

What the Pipeline Does
The Azure Data Factory pipeline reads sales data from a source location and copies the data to the destination using a Copy Activity.
The pipeline uses a `fileName` parameter to dynamically specify which input file should be processed.

Example files:
- `sales_jan.csv`
- `sales_feb.csv`
- `sales_mar.csv`
The same pipeline can process different files by changing the parameter value.

Why Parameterization?
Without parameterization, a separate pipeline or dataset configuration may be required for different files.
With parameterization, the same pipeline can be reused for multiple files by passing a different file name.

Benefits
- Reusable pipeline
- Reduces duplicate development
- Easier maintenance
- Supports dynamic file processing
- Improves scalability

Pipeline Flow
Input CSV File
      ↓
Parameterized Dataset
      ↓
Copy Activity
      ↓
Destination
