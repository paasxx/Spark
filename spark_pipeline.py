from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import os


def process_gps_data(input_path="csv_data/gps_data.csv", output_dir="output", filter_vehicle_id="V1"):
    spark = SparkSession.builder.appName("GPS Pipeline").getOrCreate()

    df = spark.read.option("header", True).option("InferSchema", True).csv(input_path)

    df_filtered = df.filter(col("vehicle_id")==filter_vehicle_id)

    df_avg = df.groupBy("vehicle_id").agg(avg("speed_kmh").alias("avg_speed"))

    print("\n Filtered Data:")
    df_filtered.show()
    print("\n Velocidade média por veículo:")
    df_avg.show()


    os.makedirs(output_dir, exist_ok=True)

    df_avg.write.mode("overwrite").csv(f"{output_dir}/avg_speed")
    df_filtered.write.mode("overwrite").csv(f"{output_dir}/filtered_{filter_vehicle_id}")


    spark.stop()

if __name__ == "__main__":
    process_gps_data()