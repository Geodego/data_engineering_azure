# Azure Tools Configuration

This document describes how to configure some of the tools used in Azure data warehouse development.

## Table of Contents


## Azure Synapse

### Create a Synapse workspace

- From Azure portal Home space click on `Create a resource`
- There is a space for looking for resources: type 'azure synapse'
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
    - `Server admin login`: e.g. 'sqladminuser'
    - `Password`: define a password for the admin user
    - once  you have configured the server, click on `OK` and you'll be back to the `Create SQL Database` wizard
  - In the server dropdown, we see the server we just created. Select it.
  - Then in `General purpose` select `Configure database` to configure your database with regard to compute and storage.
    - In `Service tier` select `Basic
    - select `Apply`
    - Now it shows that your a configured for `Basic` `compute + storage
  - we can leave the rest of the settings as default and go directly to the tab `Review + create`
  - Click on `Create`

## Azure Blob Storage
- From Azure portal Home space click on `Create a resource`
- Select `Storage account` from the list of resources
- Click on `Create`
- This brings you to the 'Create storage account' wizard.
- `Basics`:
  - `Subscription`: select the subscription you want to use
  - `Resource group`: select the resource group you want to use
  - `Storage account name`: e.g. 'udacitydemoc2dend'.
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
  - 'Firewall rules': select `Allow public access from anay Azure service within Azure to this server`
- We can leave the rest of the settings as default and go directly to the tab `Review + create`
- Click on `Create`

## Ingesting data into Azure Synapse Analytics Workspace
This show how to create linked services to ingest data into Azure Synapse Analytics Workspace. 
- Withing the workspace use the left hand menu to navigate to the `Manage` tab. 
- Then select `Linked services`. 
- To add a new linked service, click on the `+` sign on the top of the screen.
- PostgreSQL:
  - Search for `PostgreSQL` and select `Azure Database for PostgreSQL` (which you've already created) from the 2 possible 
  options.
  - In `Account Selection Method` select `From Azure subscription`

  
    

