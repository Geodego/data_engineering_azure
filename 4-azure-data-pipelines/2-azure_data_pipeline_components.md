# Azure Data Pipeline Components

## Table of Contents

- [Expert Perspective: Data Pipelines](#expert-perspective-data-pipelines)
- [Pipelines and Activities](#pipelines-and-activities)
- [Creating Azure Resources](#creating-azure-resources)
  - [Creating an Azure SQL Database resource](#creating-an-azure-sql-database-resource)
  - [Creating an Azure Data Lake Gen2 resource](#creating-an-azure-data-lake-gen2-resource)
  - [Creating an Azure Data Factory resource](#creating-an-azure-data-factory-resource)
- [Pipeline Component: Linked Services](#pipeline-component-linked-services)
- [Pipeline Components: Datasets](#pipeline-components-datasets)
  - [Creating a Dataset](#creating-a-dataset)

## Expert Perspective: Data Pipelines

Organizations have been accumulating vast amounts of structured and unstructured data throughout their processes to 
analyze and optimize the process with data analytics. This helps meet various objectives such as cost savings, 
generating more revenues, developing new products, and improving customer satisfaction.

As organizations migrate more data workloads to Cloud platforms such as Azure, the need for automated and petabyte-scale 
data movement and transformation is crucial for faster decision-making with the data. The right answer for this 
challenge is to leverage Azure Data Factory or Azure Synapse Pipelines.

Azure Data Factory or Azure Synapse Pipelines provide cloud-based code-free ETL (or ELT) as a service to orchestrate the 
data movement between 100s of data sources at petabyte scale.

<img src="./0-images/chap2/bi-architecture.png">

## Pipelines and Activities

Pipeline in Azure Data Factory or Synapse are logical grouping of various activities such as data movement, data 
transformation and control flow. The Activities inside the Pipelines are actions that we perform on the data. For 
example:
- Copy data activity is used to load data from on-prem SQL server to Azure Data Lake
- Dataflow activity to extract data from Data Lake, transform and load into Synapse
- Control Flow activity to iteratively perform the copy data activities or data flow activities

[The relationship between pipelines, activities and datasets](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?tabs=data-factory):
<img src="./0-images/chap2/pipelines-activities-datasets.png">

## Creating Azure Resources

### Creating an Azure SQL Database resource
see [Azure SQL Database](https://github.com/Geodego/data_engineering_azure/blob/master/2-data_warehouses/6-Azure_tools_configuration.md#azure-sql-database)
For requesting the database select on the left `Query editor (preview)`
### Creating an Azure Data Lake Gen2 resource
see [Azure Data Lake Gen2](https://github.com/Geodego/data_engineering_azure/blob/master/2-data_warehouses/6-Azure_tools_configuration.md#azure-blob-storage)

In the `Advanced` tab and enable the `hierarchy namespace` feature. That will make the Storage account a Data Lake Gen2.

### Creating an Azure Data Factory resource
- From Azure portal Home space click on `Create a resource`
- Select `Data Factory` from the list of resources
- Click on `Create`
- This brings you to the 'Create data factory' wizard.
- `Basics`:
  - `Resource group`: select the resource group you want to use
  - `name`: The name has to be unique
  - select the region
  - keep the version 2 of the ADF
- `Git Configuration`:
  - check the box `Configure Git later`
- We can leave the rest of the settings as default and go directly to the tab `Review + create`
- Click on `Create`

To use the Azure Data Factory, click on `Open ` 



## Pipeline Component: Linked Services 
A Linked Service is a pipeline component that contains the connection information needed to connect to a data source.

For example in order to connect to a SQL Server database, you will need the server name, a user name and password.

The Linked Service is the first building block in the process, so it has to be created before creating any other 
pipeline components.

ADF and Synapse provide connectors to 100 plus data sources under the following categories:
- Azure: Azure Blob Storage, Azure Search, Azure Synapse, Azure SQL DB, Cosmos DB etc.
- External Databases: Amazon Redshift, Google Big Query, SQL Server on-prem, Oracle, SAP etc.
- File: Amazon S3, Google Cloud Storage, FTP etc.
- Generic Protocol: ODBC, OData, REST, Sharepoint Online List etc.
- NoSQL: MongodB, Cassandra, Couchbase
- Services and Apps: Dynamics 365, Concur, AWS Web Service, Salesforce, Snowflake etc.

<img src="./0-images/chap2/linked-services.png">

## Pipeline Components: Datasets

While the Linked Service gives you the ability to connect to the data source, Datasets allow you to create a view of 
data source objects such as database tables and files on Data Lake. You need the datasets for every source object to 
extract the data and every target object to store the data.

### Creating a Dataset
- click on the `Author` tab
- click on `...` next to `datasets`
- click on `New dataset`
- select the type of dataset you want to create (Azure SQl database or Azure Synapse Analytics for example)
- `name`: for example, ds_salesorderheader
- `Linked service`: select the linked service you created earlier
- `Table name`: select the table you want to use
- keep the default option for the `import schema` option
- click on `publish all` to save the datasets
