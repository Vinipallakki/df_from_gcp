from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("GCS-PySpark-Filter-Hello") \
    .getOrCreate()


# Set the GCS bucket and file path
bucket = "banded-edge-437103-i9"
file_path = f"gs://{bucket}/new 9.txt"

# Read the text data from GCS
text_df = spark.read.text(file_path)

# Filter rows that contain the word "hello" (case-insensitive)
filtered_df = text_df.filter(col("value").contains("hello"))

# Show the filtered data
filtered_df.show(truncate=False)


# Stop the Spark session
spark.stop()