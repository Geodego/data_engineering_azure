# Project questions


## Task 1: Create your Azure resources
- create Postgres Azure Database
- Create Azure Synapse workspace
- Set-up needed to use serverless SQL pool and database?

## Task 3
-  host, username, and password information for your PostgresSQL database:
   - Local database:
     - host: localhost
     - Port: The default PostgreSQL port is 5432. 
     - username: your PostgreSQL username. 
     - password: The password for the above username. 
     - database: The name of the database you want to connect to.
   - Azure Database:
     - host: Enter the host name of your Azure PostgreSQL database. You can find this in your Azure portal under the 
      properties of your PostgreSQL server. It typically follows the format <your-database-name>.postgres.database.azure.com.
     - Port: The default PostgreSQL port is 5432.
     - user: Your username followed by @<your-database-name>, which is the format Azure uses for PostgreSQL database usernames.
     - Password: The password you set for the PostgreSQL database in Azure.
     - SSL: Azure PostgreSQL requires SSL for connections. You might need to enable SSL in your connection settings and 
    possibly specify a path to the SSL certificate.

### for dbbeaver:
#### Step 1: Create New Connection
- Navigate to the 'Database' menu and choose 'New Database Connection'. Alternatively, click the 'New' icon (a plus sign) in the Database Navigator view.

#### Step 2: Choose PostgreSQL
- In the 'Connect to a database' window, find and select 'PostgreSQL'.
- Click 'Next'.

#### Step 3: Enter Connection Details
- **Host**: Input your Azure PostgreSQL server host name. This is typically in the format `<your-database-name>.postgres.database.azure.com` and can be found in your Azure portal.
- **Port**: Use `5432`, which is the default port for PostgreSQL.
- **Database**: Enter the name of the database you want to connect to.
- **User Name**: Your Azure PostgreSQL username, usually `username@your-database-name`.
- **Password**: The password associated with your PostgreSQL database user.

#### Step 4: Configure SSL Settings
- Switch to the 'SSL' tab in the connection settings.
- Ensure 'Use SSL' is set to true.
- For 'SSL Factory', use the default setting or specify `org.postgresql.ssl.DefaultJavaSSLFactory` if necessary.
- You may need to download and specify an SSL certificate from Azure.

## Task 4
- [How to use the ingest wizard](https://github.com/Geodego/data_engineering_azure/blob/master/2-data_warehouses/8-Azure_tools_configuration.md#ingesting-data-into-azure-synapse-analytics-workspace)

## Task 5
- put dates into a varchar field 
- prepare script in advance to be able to rename columns


## Task 6
- is it the serverless SQL pool that is used for the TRANSFORM step?
- Does it mean that the tables in the final star schema are not persistent tables? Is it a standard practice when using 
these Azure tools or it is specific to the Udacity workspace constraints.
- Get a deeper understanding of CETAS
- IS CETAS Azure specific
- explain: Tip: For creating fact tables out of join between dimensions and staging tables, you can use CETAS to 
materialize joined reference tables to a new file and then join to this single external table in subsequent queries.
- Read the 3 docs in Reference for SQL serverless pool.

## notes
synapse: from home select in resources your synapse resource
in Getting started click 'Open Synapse studio'