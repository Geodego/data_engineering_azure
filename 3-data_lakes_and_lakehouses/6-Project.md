# Project: Azure Data Lakehouse Project

## Azure Databricks set-up
- To view your DBFS files, enable the DBFS file browser in Databricks by going to Admin Console -> Workspace Settings -> Advanced
- If you are going to use PySpark Pandas, make sure you create your Spark Cluster using a Databricks runtime >= 10.0
- Single node: You can use either the Standard_DS3_v2 or Standard_DS4_v2 SKU

steps:
- create a cluster
- create a notebook


## Extract step
- Upload the csv file to DBFS (see 'uploading files to delta using databricks')
- Import the data into Azure Databricks using Delta Lake to create a Bronze data store (done in notebook)
