from pyspark.sql import SparkSession


def explore_dataframe():
    spark = SparkSession.builder.appName("Skewness Introduction").getOrCreate()

    # TODO get your file path from s3 for parking_violation.csv
    input_path = "../data/parking_violation.csv"
    df = spark.read.format("csv").option("header", True).load(input_path)

    # investigate what columns you have
    col_list = df.columns
    print(col_list)

    # TODO groupby month and year to get count
    year_df = df.groupby("year").count()
    year_df.show()
    month_df = df.groupby("month").count()
    month_df.show()

    # TODO write file partition by year, and study the executor in the spark UI
    # TODO use repartition function
    df.repartition("year").write.csv("../data/year_partitioned")
    df.repartition("month").write.csv("../data/month_partitioned")


if __name__ == "__main__":
    explore_dataframe()
