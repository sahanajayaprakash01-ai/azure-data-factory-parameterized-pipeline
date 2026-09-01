from pyspark.sql.functions import col

# Read source data
df = spark.read.csv(
    "abfss://curated@projectfirst.dfs.core.windows.net/sales_jan.csv",
    header=True,
    inferSchema=True
)

# Remove records where key columns are null
df_clean = df.dropna(
    subset=["CustomerID", "OrderID"]
)

# Calculate amount including 18% tax
df_clean = df_clean.withColumn(
    "AmountWithTax",
    col("TotalAmount") * 1.18
)

# Display transformed data
display(df_clean)
