from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# Create Spark session
spark = SparkSession.builder.appName("RatingCount").getOrCreate()

# Load the .data file without headers
df = spark.read.option("header", "false").option("delimiter", " ").csv("gs://banded-edge-437103-i9/moviedata.data")

# Split the single column into multiple columns assuming it has four fields: userId, movieId, rating, timestamp
df = df.select(split(col("_c0"), "\\s+").alias("fields")) \
       .select(
           col("fields").getItem(0).alias("userId"),
           col("fields").getItem(1).alias("movieId"),
           col("fields").getItem(2).alias("rating").cast("int"),
           col("fields").getItem(3).alias("timestamp")
       )

# Select and process the rating column
rating_counts = df.groupBy("rating").count().filter("rating BETWEEN 1 AND 5").orderBy("rating")

# Show the result
rating_counts.show()