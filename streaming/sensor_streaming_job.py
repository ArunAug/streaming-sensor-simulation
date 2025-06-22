from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

spark = SparkSession.builder.appName("SensorStream").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = StructType() \
    .add("sensor_id", StringType()) \
    .add("timestamp", LongType()) \
    .add("temperature", DoubleType()) \
    .add("humidity", DoubleType())

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "sensor-data")
    .load()
)

parsed = (
    df.selectExpr("CAST(value AS STRING)")
    .select(from_json(col("value"), schema).alias("data"))
    .select("data.*")
)

agg = parsed.groupBy("sensor_id").avg("temperature", "humidity")

query = (
    agg.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", False)
    .start()
)

query.awaitTermination()
