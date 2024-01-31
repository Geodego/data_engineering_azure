from pyspark.sql import SparkSession


def repartition():
    spark = SparkSession.builder \
        .appName("Repartition Example") \
        .master("local[*]") \
        .getOrCreate()

    # TODO Path to your file
    import pandas as pd
    df = spark.read.format('csv') \
        .option('header', 'true') \
        .option('inferSchema', 'true') \
        .load('../data/parking_violation.csv')

    # Select all columns except the first one that contains the index
    df = df.select(df.columns[1:])
    df.printSchema()
    df.show(5)

    # TODO explore & do some transformations and actions and see how Spark works,
    # especially on the executor tab
    # for example.. write is an action
    # fill it in with your desired path and look at the executor tab
    # df.write.partitionBy('year').csv("../data/year_partitioned")

    # this partition by year generates a "java.lang.OutOfMemoryError: Java heap space" error
    # Lets analyse the distribution of the column "year"
    df.groupBy('year').count().show()

    # Now, try doing repartition
    # TODO Add the number of your workers
    # Write another path, and take a look at Executor tab. What changed?
    df.repartition("year").write.csv("../data/repartition.csv")


if __name__ == "__main__":
    repartition()
