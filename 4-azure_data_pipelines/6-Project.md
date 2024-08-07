# Project: Data Integration Pipelines for NYC Payroll Data Analytics

## Project Overview

The City of New York would like to develop a Data Analytics platform on Azure Synapse Analytics to accomplish two
primary objectives:

- Analyze how the City's financial resources are allocated and how much of the City's budget is being devoted to
  overtime.
- Make the data available to the interested public to show how the City’s budget is being spent on salary and overtime
  pay for all municipal employees.

As a Data Engineer, you should create high-quality data pipelines that are dynamic, can be automated, and monitored for
efficient operation. The project team also includes the city’s quality assurance experts who will test the pipelines to
find any errors and improve overall data quality.

The source data resides in Azure Data Lake and needs to be processed in a NYC data warehouse. The source datasets
consist of CSV files with Employee master data and monthly payroll data entered by various City agencies.

<img src="./0-images/chap6/nyc-payroll-db-schema.jpg" alt="ci-cd.png" width=496 />

We will be using Azure Data Factory to create Data views in Azure SQL DB from the source data files in DataLake Gen2.
Then we built our dataflows and pipelines to create payroll aggregated data that will be exported to a target directory
in DataLake Gen2 storage over which Synapse Analytics external table is built. At a high level your pipeline will look
like below:

<img src="./0-images/chap6/data-integration-pipelines-overview.jpg" alt="ci-cd.png" width=574 />

## Project Environment

For this project, you'll do your work in the Azure Portal, using several Azure resources including:

- Azure Data Lake Gen2 (Storage account with Hierarchical Namespaces checkbox checked when creating)
- Azure SQL DB
- Azure Data Factory
- Azure Synapse Analytics

You'll also need to create a Github repository for this project. At the end of the project, you will connect your Azure
pipelines to Github and submit the URL or contents of the repository.

## Project Data

[Download these .csv files](https://video.udacity-data.com/topher/2022/May/6283aff5_data-nyc-payroll/data-nyc-payroll.zip)
that provide the data for the project.

## Instructions

Note: issue with dataflow emp, column agency start date in data tables, and sink in azure datalake.

### Task 1: Create and Configure Resources

#### Create the data lake and upload data

- Create an Azure Data Lake Storage Gen2 (storage account, we call it `uproject4`) and associated storage container
  resource named `adlsnycpayroll-yourfirstname-lastintial`.
- In the Azure Data Lake Gen2 creation flow, go to Advanced tab and ensure below options are checked:
    - Require secure transfer for REST API operations
    - Allow enabling anonymous access on individual containers
    - Enable storage account key access
    - Default to Microsoft Entra authorization in the Azure portal
    - Enable hierarchical namespace
- Create three directories in this storage container named:
    - dirpayrollfiles
    - dirhistoryfiles
    - dirstaging
  `dirstaging` will be used by the pipelines to store staging data for integration with Azure Synapse.
- Upload the data files provided in the project data section to:
    - dirpayrollfiles for EmpMaster.csv, AgencyMaster.csv, TitleMaster.csv and nycpayroll_2021.csv
    - dirhistoryfiles for nycpayroll_2020.csv (historical data)

#### Create Azure Data Factory resource

see [Creating Azure Data Factory](https://github.com/Geodego/data_engineering_azure/blob/master/4-azure_data_pipelines/2-azure_data_pipeline_components.md#creating-an-azure-data-factory-resource)
- Create an Azure Data Factory resource

#### Create Azure SQL DB resource and tables

see [Creating Azure SQL DB](https://github.com/Geodego/data_engineering_azure/blob/master/2-data_warehouses/6-Azure_tools_configuration.md#azure-sql-database)
- Create an Azure SQL DB resource named `db_nycpayroll`:
    - In the creation steps, you will be required to create a SQL server, create a server with Service tier: Basic
    - In Networking tab, allow both of the below options (-> for that purpose you need to select `Public endpoint`):
        - Allow Azure services and resources to access this server 
        - Add current client IP address
      
For requesting the database select on the left `Query editor (preview)`
- Create Employee Master Data table:
  ```sql
    CREATE TABLE [dbo].[NYC_Payroll_EMP_MD](
    [EmployeeID] [varchar](10) NULL,
    [LastName] [varchar](20) NULL,
    [FirstName] [varchar](20) NULL
    ) 
    GO
    ```
- Create Job Title table:
  ```sql
    CREATE TABLE [dbo].[NYC_Payroll_TITLE_MD](
    [TitleCode] [varchar](10) NULL,
    [TitleDescription] [varchar](100) NULL
    )
    GO
  ```
- Create Agency Master Data table:
  ```sql
    CREATE TABLE [dbo].[NYC_Payroll_AGENCY_MD](
    [AgencyID] [varchar](10) NULL,
    [AgencyName] [varchar](50) NULL
    )
    GO
    ```
- Create Payroll 2020 transaction data table:
    ```sql
    CREATE TABLE [dbo].[NYC_Payroll_Data_2020](
        [FiscalYear] [int] NULL,
        [PayrollNumber] [int] NULL,
        [AgencyID] [varchar](10) NULL,
        [AgencyName] [varchar](50) NULL,
        [EmployeeID] [varchar](10) NULL,
        [LastName] [varchar](20) NULL,
        [FirstName] [varchar](20) NULL,
        [AgencyStartDate] [date] NULL,
        [WorkLocationBorough] [varchar](50) NULL,
        [TitleCode] [varchar](10) NULL,
        [TitleDescription] [varchar](100) NULL,
        [LeaveStatusasofJune30] [varchar](50) NULL,
        [BaseSalary] [float] NULL,
        [PayBasis] [varchar](50) NULL,
        [RegularHours] [float] NULL,
        [RegularGrossPaid] [float] NULL,
        [OTHours] [float] NULL,
        [TotalOTPaid] [float] NULL,
        [TotalOtherPay] [float] NULL
    ) 
    GO
    ```
- Create Payroll 2021 transaction data table:
    ```sql
     CREATE TABLE [dbo].[NYC_Payroll_Data_2021](
        [FiscalYear] [int] NULL,
        [PayrollNumber] [int] NULL,
        [AgencyCode] [varchar](10) NULL,
        [AgencyName] [varchar](50) NULL,
        [EmployeeID] [varchar](10) NULL,
        [LastName] [varchar](20) NULL,
        [FirstName] [varchar](20) NULL,
        [AgencyStartDate] [date] NULL,
        [WorkLocationBorough] [varchar](50) NULL,
        [TitleCode] [varchar](10) NULL,
        [TitleDescription] [varchar](100) NULL,
        [LeaveStatusasofJune30] [varchar](50) NULL,
        [BaseSalary] [float] NULL,
        [PayBasis] [varchar](50) NULL,
        [RegularHours] [float] NULL,
        [RegularGrossPaid] [float] NULL,
        [OTHours] [float] NULL,
        [TotalOTPaid] [float] NULL,
        [TotalOtherPay] [float] NULL
    ) 
    GO
    ```
- Create Payroll Summary table:
    ```sql
    CREATE TABLE [dbo].[NYC_Payroll_Summary](
        [FiscalYear] [int] NULL,
        [AgencyName] [varchar](50) NULL,
        [TotalPaid] [float] NULL 
    )
    GO
    ```

#### Create Synapse Analytics Workspace

see [Create Synapse Analytics workspace](https://github.com/Geodego/data_engineering_azure/blob/master/2-data_warehouses/6-Azure_tools_configuration.md#create-a-synapse-workspace)

- Create a Synapse Analytics workspace, or use one you already have created.
- Under Synapse, you will not be allowed to run SQL commands in the default main database. Go to `Develop` create a sql 
script and use the below command to create a database and then refresh the database selector dropdown. Choose your 
created database before running any queries:
  ```sql
  CREATE DATABASE udacity;
  ```
    - You are only allowed one Synapse Analytics workspace per Azure account, a Microsoft restriction.
    - Select Data Lake Gen2 `uproject4` and file system `<adlsnycpayroll-yourfirstname-lastintial>` for 
  Synapse Analytics when you are creating the Synapse Analytics workspace in the Azure portal.
    - Define the file format, if not already, for reading/saving the data from/to a comma delimited file in blob
      storage:
      ```sql
      -- Use the same file format as used for creating the External Tables during the LOAD step.
      IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
      CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
      WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
      FORMAT_OPTIONS (
      FIELD_TERMINATOR = ',',
      USE_TYPE_DEFAULT = FALSE
      ))
      GO
      ```
    - Define the data source to persist the results. Use the blob storage account name as applicable to you. The data
      source to use is the folder `dirstaging` defined previously.
      ```sql
      -- Use the same data source as used for creating the External Tables during the LOAD step.
      IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'ExtDataSource') 
      CREATE EXTERNAL DATA SOURCE [ExtDataSource] 
      WITH ( 
          LOCATION = 'abfss://<adlsnycpayroll-yourfirstname-lastintial>@uproject4.dfs.core.windows.net' 
      )
      GO
      ```
    - Create external table that references the `dirstaging` directory of DataLake Gen2 storage for staging payroll
      summary data:
      ```sql
      CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_Summary](
      [FiscalYear] nvarchar(4000) NULL,
      [AgencyName] nvarchar(4000) NULL,
      [TotalPaid] nvarchar(4000) NULL
      )
      WITH (
      LOCATION = '/dirstaging/summary.csv',
      DATA_SOURCE = [ExtDataSource],
      FILE_FORMAT = [SynapseDelimitedTextFormat]
      )
      GO
        ```
      the data will be stored in the ‘/’ directory in the blob storage in `dirstaging` (this was configured when creating
      datasource). You can change the location as you desire. Also, change the DATA_SOURCE value, as applicable to you.
      Note that, `uproject4` is the Data Lake Gen 2 storage name, and `<adlsnycpayroll-yourfirstname-lastintial>` is the
      name of the file system (container).

#### Check list

- Created an Azure Data Lake Gen2 storage account with folders, and uploaded .csv files to folders.
- Created Azure Data Factory Resource
- Created SQL DB resource and tables
- Created Synapse Analytics Workspace
- Capture screenshot of the below
  - DataLakeGen2 that shows files are uploaded 
  - Above 5 tables created in SQL db 
  - External table created in Synapse

-> how do you check the external table in Synapse?


### Task 2: Create Linked Services 

#### Create Linked Services in Azure Data Lake
In Azure Data Factory, create a linked service to the data lake that contains the data files:
- From the data stores, select Azure Data Lake Gen 2
- Test the connection

#### Create Linked Services in Azure SQL DB
- Create a Linked Service to SQL Database that has the current (2021) data
- in `version` select legacy
- If you get a connection error, remember to add the IP address to the firewall settings in SQL DB in the Azure Portal

#### Check list
- Capture screenshot of Linked Services page after successful creation
- Save configs of Linked Services after creation 

### Task 3: Create Datasets in Azure Data Factory

#### Create the datasets for the 2021 Payroll file on Azure Data Lake Gen2
- Select DelimitedText
- Set the path to the nycpayroll_2021.csv in the Data Lake
- Preview the data to make sure it is correctly parsed

#### Repeat the same process to create datasets for the rest of the data files in the Data Lake
- EmpMaster.csv
- TitleMaster.csv
- AgencyMaster.csv
- nycpayroll_2020.csv
- Remember to publish all the datasets

#### Create the dataset for all the data tables in SQL DB
- dbo.NYC_Payroll_EMP_MD
- dbo.NYC_Payroll_TITLE_MD
- dbo.NYC_Payroll_AGENCY_MD
- dbo.NYC_Payroll_Data_2020
- dbo.NYC_Payroll_Data_2021
- dbo.NYC_Payroll_Summary

#### Create the datasets for destination (target) table in Synapse Analytics
- dataset for NYC_Payroll_Summary:
  - Datastore: Azure Data Lake Storage Gen2
  - File format: DelimitedText
  - Linked service connected to the Data Lake Gen2 storage
  - Path: /dirstaging/

#### Check list
- Capture screenshots of datasets in Data Factory
- Save configs of datasets from Data Factory

### Task 4: Create Data Flows
In Azure Data Factory, create data flow to load 2020 Payroll data from Azure DataLake Gen2 storage to SQL db table 
created earlier:
- Create a new data flow `dataflow_payroll2020`
- Select the dataset for 2020 payroll file as the source, call the source activity `source_payroll_2020`
- Click on the + icon at the bottom right of the source, from the options choose sink. A sink will get added in the 
dataflow. Call the sink activity `sink_payroll_2020`
- Select the sink dataset as 2020 payroll table created in SQL db

Repeat the same process to add data flow to load data for each file in Azure DataLake to the corresponding SQL DB tables:
- `dataflow_payroll2021`
- `dataflow_emp`
- `dataflow_title`
- `dataflow_agency`

#### Check list
- Capture screenshots of data flows in Data Factory
- Save configs of data flows from Data Factory

### Task 5: Data flow: Data Aggregation and Parameterization
In this step, you'll extract the 2021 year data and historical data, merge and aggregate. The aggregation will be on 
Agency Name, Fiscal Year and TotalPaid. The output will be stored both in:
- DataLake staging area which will be used by Synapse Analytics external table (`dirstaging` directory) 
- SQL DB table for the summary data (`NYC_Payroll_Summary` SQL table)

then:
- Create new data flow and name it `dataflow_summary`
- Add **source** as payroll 2020 data from SQL DB
- Add another **source** as payroll 2021 data from SQL DB
- Make sure to do any source to target mappings if required. This can be done by adding a **Select** activity before 
the `Union` activity
- Create a new **Union** activity and select both payroll datasets as the source
- After Union, add a **Filter** activity, go to Expression builder
  - Create a parameter named- dataflow_param_fiscalyear and give value 2020 or 2021 ([How to create parameters](https://github.com/Geodego/data_engineering_azure/blob/master/4-azure_data_pipelines/5-azure_pipelines_in_production.md#method-for-adding-parameters-to-a-dataflow))
  - Include expression to be used for filtering: toInteger(FiscalYear) >= $dataflow_param_fiscalyear
- Now, choose **Derived Column** after filter
  - Name the column: `TotalPaid`
  - Add following expression: `RegularGrossPaid` + `TotalOTPaid`+ `TotalOtherPay`
- Add an **Aggregate** activity to the data flow next to the TotalPaid activity
  - Under Group by, select `AgencyName` and `FiscalYear`
  - Set the expression to sum(`TotalPaid`)
- Add a **Sink** activity after the Aggregate
  - Select the sink as summary table created in SQL db
  - In `Settings`, tick `Truncate table`
- Add another **Sink** activity, this will create two sinks after Aggregate
  - Select the sink as `dirstaging` in Azure DataLake Gen2 storage
  - In `Settings`:
    - tick `Clear the folder`
    - choose `Output to single file` and give the file name as `summary.csv`
    

#### Check list
- Capture screenshot of aggregate dataflow in Data Factory
- Save configs of aggregate dataflow from Data Factory

### Task 6: Create and Run Pipeline

#### Pipeline creation
Now, that you have the data flows created it is time to bring the pieces together and orchestrate the flow.

We will create a pipeline to load data from Azure DataLake Gen2 storage in SQL db for individual datasets. 
We will perform aggregations and store the summary results back into SQL db destination table and datalake staging 
storage directory which will be consumed by Synapse Analytics via CETAS.

- Create a new pipeline
- In `Move & Transform` section, add the dataflows.
- Include dataflows for Agency, Employee and Title to be parallel
- Add dataflows for payroll 2020 and payroll 2021. These should run only after the initial 3 dataflows have completed
- After payroll 2020 and payroll 2021 dataflows have completed, dataflow for aggregation should be started.

<img src="./0-images/chap6/pipeline_project.jpeg" alt="ci-cd.png" width=590 />

#### Trigger and Monitor Pipeline
- Select Add trigger option from pipeline view in the toolbar
- Choose trigger now to initiate pipeline run
- You can go to monitor tab and check the Pipeline Runs
- Each dataflow will have an entry in Activity runs list

#### Verify Pipeline run artifacts
- Query data in SQL DB summary table (destination table). This is one of the sinks defined in the pipeline.
  - Select the Azure SQL ressource you created. Select the `Query editor` tab.
  - create the SQL script:
    ```sql
    SELECT TOP 10 * FROM [dbo].[NYC_Payroll_Summary]
    ```
- Check the dirstaging directory in Datalake if files got created. This is one of the sinks defined in the pipeline
- Query data in Synapse external table that points to the dirstaging directory in Datalake.
  - In synapse:
     ```sql
      SELECT TOP 10 * FROM [dbo].[NYC_Payroll_Summary]
      ```

#### Check list
- Capture screenshot of pipeline resource from Data Factory
- Save configs of pipeline from Data Factory
- Capture screenshot of successful pipeline run. All activity runs and dataflow success indicators should be visible.
- Capture screenshot of query from SQL DB summary table
- Capture screenshot of `dirstaging` directory in DataLake Gen2 storage that shows file saved after pipeline run.
- Capture screenshot of query from Synapse summary external table.

### Task 7: Connect your Project to Github
In this step, you'll connect Azure Data Factory to Github
- Login to your Github account and create a new Repo in Github
- Connect Azure Data Factory to Github
- Select your Github repository in Azure Data Factory
- Publish all objects to the repository in Azure Data Factory


