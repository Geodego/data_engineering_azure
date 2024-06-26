# Data Lakes and Lakehouse with Azure Databricks

## Table of Contents

1. [Introduction](#introduction)
   - [Building a data lake](#building-a-data-lake)
   - [Building Lakehouse Architecture with Delta Lake in Azure Databricks](#building-lakehouse-architecture-with-delta-lake-in-azure-databricks)

2. [Data Lake and Lakehouse on Azure](#data-lake-and-lakehouse-on-azure)

3. [Azure Data Lake Gen 2](#azure-data-lake-gen-2)

4. [Delta Lake using Azure Databricks](#delta-lake-using-azure-databricks)
   - [Uploading files to Delta using Databricks DBFS](#uploading-files-to-delta-using-databricks-dbfs)
   - [Ingesting Data into Delta Lake](#ingesting-data-into-delta-lake)
   - [Creating and Deleting Tables](#creating-and-deleting-tables)
   - [Reading and Writing Data](#reading-and-writing-data)

5. [Stages of Data Processing](#stages-of-data-processing)
   - [Bronze Stage](#bronze-stage)
   - [Silver Stage](#silver-stage)
   - [Gold Stage](#gold-stage)

6. [Integrating Azure Tools](#integrating-azure-tools)
   - [Azure Data Factory](#azure-data-factory)
   - [Azure Synapse Analytics](#azure-synapse-analytics)
   - [Power BI](#power-bi)

7. [Data Governance and Security](#data-governance-and-security)
   - [Data Access Controls](#data-access-controls)
   - [Data Encryption](#data-encryption)
   - [Compliance](#compliance)

8. [Performance Optimization](#performance-optimization)
   - [Delta Caching](#delta-caching)
   - [Data Partitioning](#data-partitioning)
   - [Indexing](#indexing)

9. [Monitoring and Maintenance](#monitoring-and-maintenance)
   - [Monitoring Data Pipelines](#monitoring-data-pipelines)
   - [Managing Databricks Clusters](#managing-databricks-clusters)
   - [Automating Maintenance Tasks](#automating-maintenance-tasks)

10. [Case Studies and Best Practices](#case-studies-and-best-practices)
    - [Real-world Implementations](#real-world-implementations)
    - [Lessons Learned](#lessons-learned)
    - [Best Practices for Data Lakes and Lakehouse](#best-practices-for-data-lakes-and-lakehouse)

## Introduction

Microsoft Azure has options for building both a traditional data lake as well as a modern lakehouse with databricks:
- **Building a data lake**: For a traditional data lake, Microsoft Azure offers Azure Data Lake Gen 2 which can handle 
multiple petabytes of information while providing hundreds of gigabits of throughput.
- **Building Lakehouse Architecture with Delta Lake in Azure Databricks**: For building lakehouse architecture, you 
should use Delta Lake in Azure Databricks. Delta Lake is comprised of data storage and the Delta engine. This 
architecture enables your organization to develop data engineering pipelines to ingest, process, and analyze large 
amounts of structured, semi-structured, and unstructured data while maintaining governance over your data.

### Data Lake and Lakehouse on Azure
Data lakes are an important tool for solving complex problems in larger organizations. Often these organizations have 
terabytes of data across many different data sources. This data may consist of typical SQL OLTP databases, geospatial 
databases, image data, and enterprise content management datastores containing files of all different types.

Data lakes provide solutions for organizations facing these types of challenges with managing and analyzing data of this 
scale and diversity.

Here's Microsoft's overview of [Lakehouse Architecture on Azure](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/simplify-your-lakehouse-architecture-with-azure-databricks-delta/ba-p/2027272).

## Azure Data Lake Gen 2

Microsoft [Azure Data Lake Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) is 
the second generation of Azure Data Lake.

Some of the key features of Azure Data Lake Gen 2 are:
- Incorporates and extends Azure Blob Storage.
- Hierarchical namespaces to enable the better organization of information
- The entire structure is accessible using Hadoop compatible APIs.

Azure Data Lake Gen 2 seamlessly integrates with other data engineering tools within Azure such as Azure Synapse, Azure 
Data Factory, and Azure Databricks. It provides a solid foundation for many common data engineering scenarios.

## Delta Lake using Azure Databricks

<img src="0-images/chap5/delta_lake.png" alt="delta_lake.png" width="970"/>

There are several tasks you need to understand in order to get started working with Delta Lake in Azure Databricks.
The entry to working with Delta Lake in Azure is through the Databricks workspace. Once you have created your workspace, 
you have access to Delta Lake. After you've created the Databricks workspace there are three more main tasks:
- Ingest data into delta lake
- Create and delete tables
- Read and write data both to and from files as well as to and from tables

To ingest data into Delta Lake, there are four ways:
- Auto Loader
- COPY INTO
- ADF Copy
- Optimized Spark scripts

We will focus on using Spark Scripts to ingest data from the DBFS (Databricks File System) into Delta tables. To use the 
Spark API to ingest data from the DBFS into Delta, first, we read the file in, in this case using the CSV file format. 
The statement reads directly from the DBFS filestore and creates a data frame, here named “df”.
```python
df = spark.read.format("csv") \
  .option("sep", ",") \
  .load("/FileStore/shared_uploads/data.csv") 
```
The next step is to write the data out using df.write. By setting the format to “delta” these data are saved into the 
Delta Lake at the location specified, in this case “/delta/data”.
```python
df.write \
  .format("delta") \
  .mode("overwrite") \
  .save("/delta/data")
```

### Uploading files to Delta using Databricks DBFS
- Within the Databricks workspace, on the left-hand side, click on the Data icon to open the Data tab.
- Initially, we can select `Databases` but we can't browse the DBFS from here. 
- To enable DBFS file browsing see [writing Spark scripts in Databricks](https://github.com/Geodego/data_engineering_azure/blob/master/3-data_lakes_and_lakehouses/4-azure_databricks.md#writing-spark-scripts-in-databricks).
- Now we have an option for database tables as well as DBFS.
- We are going to upload a file into `FileStore` in the DBFS.
- click on the `Upload` button on the top right hand side of the panel.
- Here we can add a location for our data (e.g. 'demo'). Now if I upload a file it will be placed in `FileStore/demo/data.csv`.

### Ingesting Data into Delta Lake
This method is useful for one time ingestion of data into the DBFS.

This is not the preferred method for setting up a data pipeline that needs to run regularly. For that, you should 
integrate other Azure tools such as Azure Data Factory or Azure Functions for getting data into Azure Databricks.

- Going back to the data tab, we can see in DBFS the `data.csv` file we uploaded.
- Go to `Workspace` from the left-hand navigation, under `Shared`, click on the down arrow and select `Create` and then
`Notebook`.
- check that you have a Spark cluster running.
- We'll read the file with the following code:
```python
df = spark.read.format("csv") \
    .option("inferSchema", "false") \
    .option("header", "true") \
    .option("sep", ",") \
    .load("/FileStore/demo/data.csv")
# make sure the data is loaded correctly
display(df)
```
- run the cell using `run cell` in the top right corner
- using the `+` sign at the bottom of our results, we can insert a new cell 
- To write the data to Delta, we use the following code:
```python
df.write.format("delta") \
  .mode("overwrite") \
  .save("/delta/data")
```
- run the cell to ingest the data from the csv file into the Delta Lake.
- using the left-hand navigation, go to the `Data` tab and select `DBFS`
- There is now a `delta` folder with a `data` folder inside it. This is where the data from the csv file is stored as 
a parquet file.

### Creating and Deleting Tables
There are several ways to create tables using scripts. First, you can use a traditional CREATE TABLE SQL statement:
```python
spark.sql("CREATE TABLE LoanData(" \
  "loan_id BIGINT, " + \
  "paid_amnt DOUBLE" 
)
```
Alternately, you can create a Delta Lake table by using the saveAsTable function from a Spark dataframe:
```python
df.write.format("delta") \
  .mode("overwrite") \
  .saveAsTable("LoanData")
```

- click on the `Data` tab in the left-hand navigation and go to the DBFS file system.
- From the previous example, we already have a folder called `data` in the delta lake. This is the data we will use to
create a Delta table.
- Go to `Workspace` from the left-hand navigation, and select the workspace `demo` we created earlier.
- There are two different way to create a table from the Delta data:
  - The first way involves reading the data in from the Delta file:
    - ingest the data:
    ```python
        df = spark.read.format("delta") \
            .load("/delta/data")
    ```
    - run the cell. We now have a dataframe that we can use to create a table. Now:
    ```python
        df.write.format("delta") \
          .mode("overwrite") \
          .saveAsTable("datatable")
    ``` 
    - run the cell. Now we have a table called `datatable`.
    - Go back to the `Data` tab and select `Database Tables`. We can see the `datatable` we just created.
  - The second way uses Spark SQL to create a table from the Delta data:
    - run the following code:
    ```python
        spark.sql("CREATE TABLE datatable2 USING DELTA LOCATION '/delta/data'")
    ```
    - run the cell. Now we have a table called `datatable2`.
    - Go back to the `Data` tab and select `Database Tables`. We can see the `datatable` we just created. 
- To delete a table:
  - you can use SQL: 
    - Coming back to the notebook, run the following code:
    ```python
        spark.sql("DROP TABLE IF EXISTS datatable2")
    ```
    - run the cell. Now the table `datatable2` is deleted.
  - Or you can use the arrow next to your table name and click `Delete`.

### Reading and Writing Data
You need to be able to read and write data both to and from files as well as to and from tables.

To **read data** from a Delta Table in Azure Databricks, you can simply use the spark.table syntax to read by table 
name. Alternately, you can use the full data location path with the spark.read function using the delta format. Both of 
these functions will return a spark dataframe.
```python
spark.table("default.tablename")
spark.read.format("delta").load("/delta/tablename") 
```

To **write data** to a Delta Table, simply use the write function from a spark dataframe. Just as with reading, you can 
write either to a table or to a delta file location. Notice the “append” mode used here. This is a way to update 
existing data rather than simply overwrite the data.
```python
df.write.format("delta").mode("append") \    
.saveAsTable("default.tablename")

df.write.format("delta").mode("append")  \      
.save("/delta/tablename")
```

One way to quickly write data into a Delta Lake table is to use the `USING DELTA LOCATION` syntax when creating a table. 
You can also use the dataframe `saveAsTable` function that we used to create a table in the first place.
```python
spark.sql("CREATE TABLE TableName" \
  "USING DELTA LOCATION '/delta/data'"
)
```

### Stages of Data processing

<img src="0-images/chap5/stages_data_processing.png" alt="stages_data_processing" width="650"/>

First, data are ingested raw into ingestion tables. This is commonly referred to as the Bronze stage.

Next, data are refined and combined into what is commonly called the Silver stage. Data at this stage can often be used 
by data scientists and machine learning modelers.

The final stage is the creation of features and aggregates such as a star schema’s fact and dimension tables. This is 
called the Gold stage and data at this stage are useful for common business intelligence and analytics solutions such as 
Azure Synapse or PowerBI.

### Processing Delta lake Table Stages

**Step 1: Bronze stage**: Ingest data into the delta file system.
- Go to the workspace and create a new notebook. In the first cell:
```python
df = spark.read.format("csv") \
  .option("inferSchema", "true") \
  .option("header", "true") \
  .option("sep", ",") \
  .load("/FileStore/demo2/stolenvehicules.csv")

df.write.format("delta") \
    .save("/delta/bronze_vehicles")
```
- use the `run cell` button. 

**Step 2**: check what the data looks like:
- In a new cell:
```python
display(df)
```
- we see that there are no keys and that there are duplicates.

**Step 3: Silver stage**: Create a key and remove duplicates. Save the result in a delta table.
- In a new cell:
```python
df = spark.read.format("delta") \
  .load("/delta/bronze_vehicles")

from pyspark.sql.functions import sha2, concat_ws
df = df.dropDuplicates(df.columns) \
  .withColumn("hash", sha2(concat_ws("||", *df.columns), 256))

df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_vehicles")
```
- using the 'data' tab, we can check that our table has been saved.

**Step 4: Gold stage** Create a table that aggregate some information
- In a new cell:
```python
df = spark.table("silver_vehicles")
df = df.groupBy("VehicleType", "DateStolen").count()

df.write.format("delta") \
    .mode("overwrite")  \
    .saveAstable("gold_stolenbytypeanddate")
```