# Azure Tools Configuration

This document describes how to configure some of the tools used in Azure data warehouse development.

## Table of Contents

1. [Azure Synapse](#azure-synapse)
   - [Create a Synapse Workspace](#create-a-synapse-workspace)
     - [Basics](#basics)
     - [Security](#security)
     - [Networking](#networking)
     - [Tags](#tags)
     - [Review + Create](#review--create)
   - [Azure Synapse Workspace Tour](#azure-synapse-workspace-tour)
2. [Azure SQL Database](#azure-sql-database)
3. [Azure Blob Storage](#azure-blob-storage)
4. [Azure PostgreSQL Database](#azure-postgresql-database)
5. [Ingesting Data into Azure Synapse Analytics Workspace](#ingesting-data-into-azure-synapse-analytics-workspace)
6. [Ingesting Data into Blob Storage](#ingesting-data-into-blob-storage)
7. [Creating Staging Tables using Azure Synapse](#creating-staging-tables-using-azure-synapse)




## Azure Synapse

### Create a Synapse workspace

- From Azure portal Home space click on `Create a resource`
- There is a space for looking for resources: type 'azure synapse', and select `Azure Synapse Analytics`
- Check that the right resource has been selected and press `create`
- That brings you to Azure Wizard for creating resources. At the top of the Wizard you see the steps you need to walk
through (Basics, Security, Networking...). `Basics` and `Security` have a star in front of them indicating they are
required fields.
  
#### Basics
- you should have a subscription
- in `managed resource group` select the resource group already created.
- `Worspace name`: e.g. 'udacitydemo2'
- select a 'Region'
- `Select Data Lake Storage Gen2`: 
    - select 'from subscription'
    - `Account name`: This is the storage account where 'file system' 
  will be created or is already created. Select `new` and type a name. e.g. 'udacitydemo2'. 
    - `File system`: Container that will be the default data lake storage that Synapse Analytics will use. 
  Select `new` and type a name. e.g. 'udacitydemo2'
    - All the rest of the settings can be left as default.

#### Security
- `SQL Server admin login`: e.g. 'sqladminuser'
- define a password for the admin user
- Leave the rest of the settings as default

#### Networking
- Leave the settings as default

#### Tags
We don't need to add tags

#### Review + create
- At the top of the page you can see an estimation of the costs
- Double check the settings
- Click on `Create`

### Azure Synapse workspace tour

Now that we have created a Synapse workspace, let's take a tour of the Synapse workspace.
- In `Overview` select the `Resources` tab. Select the synapse workspace you just created: 'udacitydemo2'.
- Selecting that resource takes you to the azure portal panel for that resource.
- Open `Azure Synapse Studio` to access all the features.
- This will load the Azure Synapse Analytics workspace. Here you find shortcuts to all the features of the workspace: 
Ingest, Explore and analyze, Visualize.
- On the left you have different tabs:
  - `Data`: Here you can see the data you have ingested into the workspace. You can also create new databases and tables.
 There could also be data sources that are linked to our workspace.
  - `Develop`: This is where you can write code against your data. To create a new notebook, click on the `+` sign on 
  the top of the screen.
  - `Integrate`: This is where you can create pipelines to integrate data from different sources. These data sources can
  be linked data sources or data sources that are part of the workspace.
  - `Monitor`: This is where you can monitor all the things that are happening in your workspace.
  - `Manage`: This is where you can manage all the resources in your workspace. This is where you can configure the
  components of your workspace.

## Azure SQL Database
- From Azure portal Home space click on `Create a resource`
- Select `SQL Database` from the list of resources
- Click on `Create`
- This brings you to the 'Create SQL Database' wizard.
- `Basics`:
  - `Subscription`: select the subscription you want to use
  - `Resource group`: select the resource group you want to use
  - `Database name`: e.g. 'demo', this names needs only to e unique within the server
  - `Server`: select `Create new`, this brings you to the `Create SQL Database server` wizard
    - `Server name`: e.g. 'udacitydemoc2dend'. This will be part of a URL. That means this name must be unique across all 
    of Azure. You should use a name that will help you identify the server among all of the ressources in your portal.
    - select `use sql authentication`:
      - `Server admin login`: e.g. 'sqladminuser'
      - `Password`: define a password for the admin user
    - once  you have configured the server, click on `OK` and you'll be back to the `Create SQL Database` wizard
  - In the server dropdown, we see the server we just created. Select it.
  - Then in `General purpose` select `Configure database` to configure your database with regard to compute and storage.
    - In `Service tier` select `Basic
    - select `Apply`
    - Now it shows that your a configured for `Basic` `compute + storage
  - select `Locally-redundant backup storage`
  - In the `Additional settings` tab select:
    - `Sample`
  - we can leave the rest of the settings as default and go directly to the tab `Review + create`
  - Click on `Create`
  - To be able to access the database with your IP, go to the server and in `Security` select `Networking`,
    - In `public access` select `Selected Networks`
    - In `Firewall rules` select `Add client IP` and click on `Save`

## Azure Blob Storage
- From Azure portal Home space click on `Create a resource`
- Select `Storage account` from the list of resources
- Click on `Create`
- This brings you to the 'Create storage account' wizard.
- `Basics`:
  - `Subscription`: select the subscription you want to use
  - `Resource group`: select the resource group you want to use
  - `Storage account name`: e.g. 'udacitydemoc2dend'.
- In `Redundancy` select `LRS (Locally-redundant storage)`
- We can leave the rest of the settings as default and go directly to the tab `Review + create`
- Click on `Create`

## Azure PostgreSQL Database
- From Azure portal Home space click on `Create a resource`
- Select `Azure Database for PostgreSQL` from the list of resources
- Click on `Create`
- Here we have two options:
  - `Single server`: This is a single server that will host one or more databases. 
  - `Flexible server`: This is a serverless option that will automatically scale up and down based on demand. This is
  the option we will use.
- `Basics`:
  - `Subscription`: select the subscription you want to use
  - `Resource group`: select the resource group you want to use
  - `Server name`: e.g. 'udacitydemo2'
  - `Workload type`: select `Development`
  - In `Compute + storage` you can select `configure server` to configure your server with regard to compute and storage.
    - choose `Burstable`, `Standard_B1ms(1vCore, 2GB memory, 640 max IOPS)`
    - leave the rest of the settings as default
  - In `Administrator Account`:
    - `Admin Username`: e.g. 'udacity'
    - `Password`: define a password for the admin user
- `Networking`:
  - 'Firewall rules': select `Allow public access from any Azure service within Azure to this server`
- We can leave the rest of the settings as default and go directly to the tab `Review + create`
- Click on `Create`

### Connecting to Azure PostgreSQL Database
- In Azure portal autorize the IP address of your computer to access the Azure PostgreSQL database:
  - In the Azure portal, navigate to your Azure Database for PostgreSQL server.
  - Select Connection security.
  - Select Add client IP.
  - Select Save.
- host: Enter the host name of your Azure PostgreSQL database. You can find this in your Azure portal under the 
      properties of your PostgreSQL server. It typically follows the format <your-database-name>.postgres.database.azure.com.
- Port: The default PostgreSQL port is 5432.
- user: Your username followed by @<your-database-name>, which is the format Azure uses for PostgreSQL database usernames.
- Password: The password you set for the PostgreSQL database in Azure.

## Ingesting data into Azure Synapse Analytics Workspace

### Creating linked services
This show how to create linked services to ingest data into Azure Synapse Analytics Workspace. 
- Withing the workspace use the left hand menu to navigate to the `Manage` tab. 
- Then select `Linked services`. 
- To add a new linked service, click on the `+` sign on the top of the screen.
- **Linked service to PostgreSQL**:
  - Search for `PostgreSQL` and select `Azure Database for PostgreSQL` (which you've already created) from the 2 possible 
  options. click on `Continue`
  - keep the default name 
  - Back to the 'New linked service' screen, in `Account Selection Method` select `From Azure subscription`.
  - By selecting my subscription in `Azure subscription`, I can find my PostgreSQL server name in `Server name`.
  - In `Database name` I can select the database I want to connect to.
  - In `User name` I can input the user which comes from my PostgreSQL resource ('udacity' in our example).
  - In `Password` I can input the password for `Admin Username` which comes from my PostgreSQL resource.
  - `Encryption method`: choose `RequestSSL`
  - Test the connection by clicking on the `Test connection` button
  - click on `Create`
- **Linked service to Azure Blob Storage**:
  - select `Azure Blob Storage` from the list of options and click on `Continue`
  - keep the default name
  - In `Account Selection Method` select `From Azure subscription`.
  - In `Storage account name` select the storage account you want to connect to. In our case it is 'udacitydemo2'.
  - test the connection by clicking on the `Test connection` button
  - click on `Create`

### Ingesting Data into Blob Storage
Now that we have created our linked services, we have a link to Azure Blob Storage and a link to Azure PostgreSQL. We
want to ingest data from PostgresSQL into Blob Storage. To do this we can use a shortcut in the home screen.
- In the home screen, select `Ingest`. This is to perform a onetime or scheduled data load.
- Select `Run once now` and click on `Next`
- in `Source type`: 
  - select `Azure Database for PostgreSQL`
  - in `Connection` select the PostgreSQL linked service we created earlier
  - Select the tables you want to ingest
  - click on `Next` and preview the data
  - close the preview and click on `Next`
- in `Target type`, select `Azure Blob Storage`
  - in `Connection` select the Blob Storage linked service we created earlier
  - in `Folder path` select the folder where you want to store the data. In our case 'udacitydemo2'.
  - add a file name e.g. 'publicpaymentimport.csv' and click on `Next`
  - That brings you to `File format settings`. Here you can configure the format of the file you want to create.
    - We want to create a CSV file. So select `Delimited text` in `Format type`
    - in `Column delimiter` select `Comma`
    - in `Row delimiter` select `Default(\r\n)`
    - click on `Next`
- in `Settings`, leave the default name and click on `Next`
- Review the settings and click on `Next` to run the deployment
- click on `Finish`
- Back to the home screen, select `Data` from the left hand menu.
- Here you see your linked services and you should have data in your blob storage.

## Creating Staging Tables using Azure Synapse

You can create staging tables using Azure Synapse Analytics. These tables are external tables that represent the load 
stage of an ELT process. In this example we use a dedicated SQL pool in Synapse studio. In the project we'll use the 
default built-in serverless SQL pool.
- From the left-hand navigation menu, select the `Manage` tab, to see the resources we have available:
  - Select `SQL pools`: 
    - there's a Built-in SQL pool and a Dedicated SQL pool. We will use the Dedicated SQL pool.
    - Check if the dedicated SQL pool is running. If not, click on `Start` to start it.
  - Select `Linked services`:
      - Here you see the 2 linked services we created earlier when we ingested data.
      - There is also an Azure Synapse Analytics and Azure Data Lake Storage Gen2 linked service that were created when the
    Synapse Analytics workspace was created.
- From Azure Synapse left hand menu, select `Data`: 
  - Select the `Workspace` tab. We can see our SQL database in which we have tables and external tables.
  Our staging data is going to go to the external tables.
  - Select the `Linked` tab. Here we can see the Azure Blob Storage we created previously. In the `Azure Data Lake Storage Gen2`
  we notice that the Blob Storage container name automatically shows up in our Data Lake. 
  - Within the container we see the CSV file that we created previously. In order to create our external table from this
    CSV file, we'll use the `New SQL script` button at the top of the screen. Hitting the dropdown, we have three options.
    We choose `Create external table`.
  - This brings us to a wizard which determines from the file its format. We check that this is a CSV file and accept
  all the defaults. We click on `Continue`.
  - In the next step I need to select the target database. In `Select SQL pool` I select the dedicated SQL pool (udacitydemo2).
  I can also select the database. We call the external table `staging_payment`.
  - Next, I can choose to create the external table automatically or I can use a SQL script. We choose to use a SQL script.
    - click on `Open script` button. Azure automatically generates the SQL script to create the external table. Looking at
      the script:
      - In the first step it's creating an external file format.
      - Next it's creating an external data source. This is the location of our Azure blob storage.
      - Next it's creating an external table:
        - 'LOCATION' is our csv file 'publicpaymentimport.csv'.
        - 'DATA_SOURCE' is the external data source we just created.
        - 'FILE_FORMAT' is the external file format we just created.
        - The column names are 'C1', 'C2',... that's because the csv file did not have column names. We should replace
        these names with the meaningful column names.
        - If we run the script as such we get an Hadoop error. That's because in the csv file the DateTime is represented 
        as a varchar. We need to import the data into the external table as a varchar(50).
  - We can check that the external table has been created by going to the `Workspace` tab and in `SQL databases` select
  `External tables` in our database. If you need to run this script again you need to drop this table first:
    - Select the 3 dots near the table and select `New SQL script` and `DROP`. You can simply run the script and it will
    drop the table.

**Note**: 
- This example use a dedicated SQL pool. For this project we will use the default built-in serverless SQL pool.
It can be used by selecting the `built-in` pool in `Manage`, `SQL pools`.
- The serverless SQL pool won't allow you to create persistent tables in the database, as it has no local 
storage. So, use `CREATE EXTERNAL TABLE AS SELECT` (CETAS) instead. CETAS is a parallel operation that creates external 
table metadata and exports the SELECT query results to a set of files in your storage account. Therefore, use an 
external table or a T-SQL view to create SQL tables in Synapse Built-in Serverless SQL pool.


  
    

