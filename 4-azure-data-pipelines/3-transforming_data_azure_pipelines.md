# Transforming Data in Azure Data Pipelines

## Table of Contents

## Introduction

Data pipelines contain transformation logic to manipulate data views. You can execute transformation logic such as:
- Filtering a row based upon a condition
- Combining data from two sources or streams
- Generating new columns or modify existing fields

This module will cover the following topics:
- Transform data in Azure Data Factory and Synapse Pipelines with Data Flows
- Debug, trigger, and monitor pipeline activities containing data flows
- Perform transformations programmatically using external compute
- Integrate Power Query in Azure Pipelines

## Mapping Data Flows

<img src="./0-images/chap3/mapping-data-flows.png" alt="mapping-data-flows.png" width="650"/>

Mapping Data Flows are activities that perform the data extraction from the data stores and then transform and store the 
transformed data to the destination data store. These Data Flows are executed inside scaled-out Apache Spark clusters 
for limitless scale and performance.
The UI allows developers to create the Mapping Data Flows using drag and drop features without writing code. There are 
three types of transformations available in Mapping Data Flows:
- Schema modifiers: These transformations allow us to manipulate the data to create new derived columns based on calculations, aggregate data, or pivoting the data etc.
- Row modifiers: These transformations allow us to change rows for e.g. filtering rows, sort rows, alter row based on insert/update/delete/upsert policies.
- Multiple inputs/outputs: These transformations allow us to generate new data with joins, unions, or splitting the data.

Below are the various types of transformations:

<img src="./0-images/chap3/data-flow-transformation-types.jpg" alt="data-flow-transformation-types.jpg" width="650"/>

### Expression Builder
Data Flows are integrated with the Visual Expression Builder in Azure Data Factory to perform transformation logic as simple expressions. The expression builder provides IntelliSense for highlighting, checking syntax, and also auto-completion.

Expressions are composed of columns from the input schema, functions, and parameters. All of these evaluate to Spark data types at runtime.
- Input Schema: References the columns from the input data source.
- Functions: Built-in functions that include array functions, aggregate functions, conversion functions, date and time functions, and window Functions etc.
- Parameters: Reference the parameters that are passed from the pipeline.
- Cached Lookup: Perform lookup in the data being processed in the activity.

### ex Mapping Data Flow in Azure Data Factory
- Select on the left `Author`
  - select the `...` near `Data Flows` and select `+ New Data Flow`
  - click on `add source` and give the source a name
  - in `data set` we need to select the relevant dataset
  - on order to be able to preview the data we need to activate `Data flow debug` on top of the screen
    - This will spin up a Spark cluster. Specify 2 hours if you plan to work that long.
    - click on `Debug settings` to specify the number of rows to preview
    - now you can select the header `data preview` to see the data
- Now we need to select the destination where we want to store the data
- click on the `+` near the activity (on the right of the large blue arrow) and select `sink`
  - give the sink a name
  - select the relevant dataset for that table in Synapse
  - You need to make sure the mappings are correct. If you see the `Auto Mapping` enabled, it means ADF
  will map the fields automatically. Sometimes if the data types are different then the auto mapping
  will not work. In that case you need to uncheck the `Auto Mapping` and map the fields manually.
  - Go to `Data Preview` to see how the data will look like in the destination.
  - Give a name to the data flow and click on `Publish All`

## Transform and aggregate data using Data Flows

For this example you need to create the `aggregate` table in Synapse.
Back to ADF:
- Create the dataset related to the `aggregate` table
- Create a new data flow
  - add the source sql table
  - Filter:
    - add a filter activity to filter the wrong sales order. For example `sales_order_id`!=xxxx.
    - click on `refresh` to make sure the data is filtered
    - click on `save and finish`
  - New column:
  - click on `+` and select `Derived Column`
    - give the column a name
    - in the expression builder you can create a new column. For example `sales_order_id`+1
    - click on `save and finish`
  - create a `sink`:
    - select the synapse table you've created
    - and map the fields
    - click on `Data Preview` to see how the data will look like in the destination.
  - Publish the data flow
- Create a new pipeline to test the data flow
  - Drag a data flow activity 
  - select in `settings` the data flow you've created
  - select the link service
  - publish the pipeline
- Trigger the pipeline:
  - click on `Add Trigger` and select `Trigger Now`
  - on the `Monitor` tab you can see the status of the pipeline
- Go to synapse to see the data in the `aggregate` table

## Create Pipeline Activity

After creating the data flow, you need to create a pipeline activity to execute the data flow. The pipeline activity is a
container that defines the workflow of the data flow. The pipeline activity can be triggered manually or scheduled to run
at a specific time.
- In th `author` tab, click on the `...` near `Pipelines` and select `+ New Pipeline`
- drag the data flow activity of interest to the pipeline
  - Give a name to the activity
  - in `settings`:
    - select the data flow you've created
    - In the `run on azure` section you can select the integration runtime you created or `autoresolveintegrationruntime`
    - In order to transfer the data to synapse, you need to select a staging folder.
    - select the link service that you created for the staging container
    - select the container
    - click `ok`
- You can add others activities to the pipeline and show dependencies between them with the arrows
- Give a name to the pipeline and click on `Publish All`

## Debug and trigger pipelines

After a pipeline is created, you will have to trigger it to run it, debug it, or monitor the pipeline activities.
Executing the pipeline to run the activities is called triggering the pipeline. The pipeline can be triggered to
execute immediately or at a scheduled time.Debugging helps to run the pipelines activities without publishing the source
control repository.You can also set the breakpoints to interactively debug various part of the pipeline.

Once triggered the pipeline needs to be monitored to make sure there are no failures. This will monitor every step of 
the pipeline and associate data flows with detailed error messages if there are any failures. Failed pipelines can be 
rerun from the pipeline run screen.

We can set the alerts to raise based on criteria. Alerts can be sent as emails, SMS...

### Exercise Debug and Trigger Pipelines

- You don't have to publish the pipeline to debug it
- If you have a debug session active in the debug tab you have 2 options: use that session or integration tun time. Here
we use the dataflow debug session.
- Then you can use the integration run time or the debug cluster. We use the debug cluster.
- The debug will start. You can click on the glasses to see the individual steps.
- If everything looks good, you can click on `Publish All` to publish the pipeline.
- Now you can go ahead and trigger the pipeline by clicking on `Add Trigger` and select `Trigger Now`
- When the pipeline is running you can monitor the progress in the `Monitor` tab.
- You can go to synapse to check the transfer has been done successfully.

## Transforming data on external compute

While the native functionality inside Mapping Dataflows gives you the ability to transform the data with no-code user 
interface, it is also possible to transform the data using the external compute environments with code. Below are some 
examples:
- Execute a stored procedure on an external database like Azure SQL DB or Synapse Dedicated Pool
- Execute Azure Function developed with Python, C#, Java etc.
- Execute a Notebook on Azure Databricks or Synapse Spark pool

### Exercise: Notebooks using Synapse Pipelines

In Synapse Studio:
- If you do not have a Spark pool, you need to create one.
- In Synapse Studio navigate to Azure Data Lake Storage Gen2 and upload a csv file of your choice into the container. 
Note: If you would like to use your files under your preferred Azure Storage account then you need to create a linked 
service inside Synapse Studio and grant "Storage Blob Contributor" role for the Synapse Workspace on the storage 
account.
- Right click on the uploaded file and select New Notebook-> Load to Dataframe. You will see sample code populated 
automatically to load the data from the file:
```python
df = spark.read.load('abfss://yourcontainer@yourstorage.dfs.core.windows.net/salesdata_2020.csv', format='csv', header=True)
display(df.limit(10))
```
- Add the code similar to below to save that data into a Spark table:
```python
spark.sql("CREATE DATABASE IF NOT EXISTS schemaname")
df.write.mode("overwrite").saveAsTable("schemaname.tablename")
```
- Publish the notebook 
- go to Integrate Hub in Synapse Studio and create a Pipeline to execute the above Notebook. Monitor the pipeline and 
fix any errors.
- After successful execution of the Pipeline, Navigate to Data hub and see the newly created table under Workspace and 
Lake Database section.
  



