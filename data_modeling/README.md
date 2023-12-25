# Data Modeling



# Table of Contents
- [Introduction to Data Modeling](#introduction-to-data-modeling)
  - [Key concepts](#key-concepts)
    - [Relational Databases](#relational-databases)
      - [Advantages of Using a Relational Database](#advantages-of-using-a-relational-database)
      - [ACID transactions](#acid-transactions)
      - [When Not to Use a Relational Database](#when-not-to-use-a-relational-database)
    - [Introduction to NoSQL Databases](#introduction-to-nosql-databases)
      - [NoSQL Database Implementations](#nosql-database-implementations)
      - [When to use a NoSQL Database](#when-to-use-a-nosql-database)
  - [Installation of PostgreSQL and Cassandra](#installation-of-postgresql-and-cassandra)
    - [Installation of PostgreSQL on Mac OS X](#installation-of-postgresql-on-mac-os-x)
      - [Starting and Stopping PostgreSQL](#starting-and-stopping-postgresql)
      - [Interacting with PostgreSQL](#interacting-with-postgresql)
      - [Creating a Database](#creating-a-database)
    - [Cassandra](#cassandra)
      - [Starting and Stopping Cassandra](#starting-and-stopping-cassandra)
- [Relational Data Models](#relational-data-models)
   - [OLAP vs OLTP](#olap-vs-oltp)
      - [Online Analytical Processing (OLAP)](#online-analytical-processing-olap)
      - [Online Transactional Processing (OLTP)](#online-transactional-processing-oltp)
   - [Normalization for Transactional Databases (OLTP)](#normalization-for-transactional-databases-oltp)
      - [Objectives of Normal Form](#objectives-of-normal-form)
      - [Normal Forms](#normal-forms)
   - [Denormalization for Analytical Databases (OLAP)](#denormalization-for-analytical-databases-olap)
      - [Denormalization](#denormalization)
      - [Star Schema and Snowflake Schema](#star-schema-and-snowflake-schema)
         - [Fact and Dimension Tables](#fact-and-dimension-tables)
            - [Fact Table](#fact-table)
            - [Dimension Table](#dimension-table)
         - [Star Schema](#star-schema)
            - [Benefits of Star Schema](#benefits-of-star-schema)
            - [Drawbacks of Star Schema](#drawbacks-of-star-schema)
         - [Snowflake Schema](#snowflake-schema)
- [Upsert in PostgreSQL](#upsert-in-postgresql)
   - [INSERT Statement](#insert-statement)
      - [Example: Creating a Customer Address Table](#example-creating-a-customer-address-table)
      - [Inserting Data](#inserting-data)
   - [Handling Conflicts with ON CONFLICT](#handling-conflicts-with-on-conflict)
      - [Scenario: Avoiding Duplicate Customer IDs](#scenario-avoiding-duplicate-customer-ids)
      - [Scenario: Updating Existing Details](#scenario-updating-existing-details)

# Introduction to Data Modeling

## Key concepts

### Relational Databases
#### Advantages of Using a Relational Database

- Flexibility for writing in SQL queries: With SQL being the most common database query language.
- Modeling the data not modeling queries
- Ability to do JOINS
- Ability to do aggregations and analytics
- Secondary Indexes available : You have the advantage of being able to add another index to help with quick searching.
- Smaller data volumes: If you have a smaller data volume (and not big data) you can use a relational database for its simplicity.
- ACID Transactions: Allows you to meet a set of properties of database transactions intended to guarantee validity even 
in the event of errors, power failures, and thus maintain data integrity.
- Easier to change to business requirements

#### ACID transactions
Properties of database transactions intended to guarantee validity even in the event of errors or power failures.

- Atomicity: The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created. Source Wikipedia for a detailed description of this example.

- Consistency: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables. Check out additional information about consistency on Wikipedia.

- Isolation: Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other. Source: Wikipedia

- Durability: Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs. Source: Wikipedia.

#### When Not to Use a Relational Database
- Have large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.
- Need to be able to store different data type formats: Relational databases are not designed to handle unstructured data.
- Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.
- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
- Need high availability: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.

### Introduction to NoSQL Databases

#### NoSQL Database Implementations:

- Apache Cassandra (Partition Row store)
- MongoDB (Document store)
- DynamoDB (Key-Value store)
- Apache HBase (Wide Column Store)
- Neo4J (Graph Database)

#### When to use a NoSQL Database
- Need to be able to store different data type formats: NoSQL was also created to handle different data configurations: structured, semi-structured, and unstructured data. JSON, XML documents can all be handled easily with NoSQL.
- Large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. NoSQL databases were created to be able to be horizontally scalable. The more servers/systems you add to the database the more data that can be hosted with high availability and low latency (fast reads and writes).
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data
- Need high throughput: While ACID transactions bring benefits they also slow down the process of reading and writing data. If you need very fast reads and writes using a relational database may not suit your needs.
- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
- Need high availability: Relational databases have a single point of failure. When that database goes down, a failover to a backup system must happen and takes time.


## Installation of PostgreSQL and Cassandra
### Installation of PostgreSQL on Mac OS X

To install Postgres on Mac OS X, follow the instructions provided [here](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb).

#### Starting and Stopping PostgreSQL

To **start** PostgreSQL, use the following command in your terminal:

```bash
brew services start postgresql
```
To stop PostgreSQL, use:

```bash
brew services stop postgresql
```

you can also start postgres manually by running the following command:
    
```bash 
pg_ctl -D /usr/local/var/postgres -l logfile start
```
After running the pg_ctl command, you can verify that PostgreSQL has started successfully by using the command:

```bash
ps aux | grep postgres
```




#### Interacting with PostgreSQL

After starting the PostgreSQL server, you can use the `psql` command-line tool to interact with the database.

When connecting to PostgreSQL for the first time, especially when no specific database has been created yet, you can 
connect to the default database provided by PostgreSQL. This database is usually named postgres, which is a default 
administrative database.
    
```bash
psql -U your_username -d postgres
```
Replace [username] with your PostgreSQL username. If you haven't created any users yet, PostgreSQL typically creates a
default user with the same name as your operating system's current user.

Once you are in the command-line interface of PostgreSQL (psql), you can exit by typing the following command:

```bash
\q
```
Just type \q and then press Enter. This will quit the psql interface and return you to the standard Mac terminal prompt.

With PostgreSQL running, you can connect to it for a specific database using the psql command-line tool:

```bash
psql -U your_username -d your_database
```

#### Creating a Database
To create a database called 'studentdb', use the following command:

```bash 
CREATE DATABASE studentdb;
```
To create a user called 'student' with password 'student', use the following command:

```bash
CREATE USER student WITH PASSWORD 'student';
GRANT ALL PRIVILEGES ON DATABASE studentdb TO student;
```

### Casssandra

#### starting and stopping cassandra

to start cassandra, run the following command:

```bash
cassandra -f
```
To stop Apache Cassandra running on your Mac, use one of the following methods:

- If Cassandra is Running in the Foreground
  - Press `Ctrl + C` in the Terminal where Cassandra is running.
- If Cassandra is Running in the Background
  - Use the following command in Terminal:
    ```bash
    pkill -f CassandraDaemon
    ```

# Relational Data Models

## OLAP vs OLTP

### Online Analytical Processing (OLAP)
- Databases optimized for OLAP workloads are designed for complex analytical and ad hoc queries, including aggregations.
- These databases are primarily optimized for read operations, making them suitable for data analysis and reporting.

### Online Transactional Processing (OLTP)
- OLTP databases are optimized for handling large volumes of less complex queries.
- They support a mix of read, insert, update, and delete operations.
- The key distinction is analytics (A) vs transactions (T): OLTP is used for direct transactions (e.g., checking the price of a shoe), while OLAP is used for analytical queries (e.g., calculating the total stock of shoes sold by a store).

## Normalization for Transactional Databases (OLTP)
Normalization in OLTP databases focuses on data integrity and minimizing redundancy.
- It organizes columns and tables to enforce dependencies through database integrity constraints.
- Normalization aims to eliminate data redundancy and maintain data integrity, ensuring updates occur in a single location.

### Objectives of Normal Form
- 3NF (Third Normal Form) is often the starting point for designing OLTP databases.
- Objectives include avoiding unwanted insertions, updates, and deletion dependencies, reducing the need for refactoring with new data types, making the model informative and neutral to query statistics.

### Normal Forms
- **First Normal Form (1NF)**:
  - Atomic values: each cell contains unique and single values.
  - Ability to add data without altering tables.
  - Separation of different relations into different tables.
  - Maintenance of relationships between tables using foreign keys.
- **Second Normal Form (2NF)**:
  - Fulfillment of all 1NF criteria.
  - All columns in the table must rely on the Primary Key.
- **Third Normal Form (3NF)**:
  - Fulfillment of all 2NF criteria.
  - No transitive dependencies.

## Denormalization for analytical databases (OLAP)

### Denormalization
Denormalization is a database optimization strategy that can be applied in different contexts. Initially, many 
operational databases are designed in a normalized form, typically adhering to the Third Normal Form (3NF), to ensure 
data integrity and reduce redundancy. In such databases, denormalization may occur as a subsequent step, where additional 
tables are created or existing ones are modified to improve read performance. This is often done by combining data from 
multiple normalized tables into a single, larger table, thereby simplifying query patterns that frequently involve 
complex joins.

However, denormalization is not solely a post-normalization process. It is also a foundational design principle in the 
construction of data warehouses for Online Analytical Processing (OLAP) systems. In these scenarios, denormalization 
is an intentional part of the design from the outset, aiming to optimize for query speed and analytical processing. 
Data warehouses often employ structures such as Star or Snowflake schemas, which inherently include denormalized data 
for efficient querying and analysis.

In both cases, whether applied to an existing 3NF database or used in designing data warehouses from scratch, 
denormalization involves trade-offs. It simplifies and speeds up read operations but can complicate write operations.
When data is denormalized, maintaining data integrity becomes more challenging, as updates may need to be reflected 
across multiple tables. Additionally, it can increase storage requirements due to data redundancy.

Thus, the decision to denormalize should consider the specific needs of the system – balancing query efficiency against 
factors like data integrity, write performance, and storage overhead. Effective denormalization requires thoughtful 
planning and a clear understanding of the system's usage patterns and performance objectives.

### Star Schema and Snowflake Schema
Two of the most common types of schemas are star and snowflake. The type of schema used depends on the business use case.

#### Fact and Dimension Tables

##### Fact Table
- Fact table contains the measurements, metrics or facts of a business process (e.g., sales amount, quantity sold in a sales process).
- It is located at the center of a star schema or a snowflake schema, surrounded by dimension tables.
- A fact table typically has two types of columns: 
    - Those that contain fact data.
    - Those that are foreign keys to dimension tables.

##### Dimension Table
- A structure that categorizes facts and measures in order to enable users to answer business questions.
- Dimensions are often descriptive data like people, products, place, and time.
- Dimension table contains the reference information about the data in the fact table and may include hierarchies and 
additional descriptive data.

#### Star Schema

- Star schema is the simplest style of data mart schema and is widely used in data warehousing systems.
- It consists of one central fact table surrounded by dimension tables.
- The schema gets its name due to its resemblance to a star shape, where the fact table is at the center and dimension
tables represent the star's points.

##### Benefits of Star Schema

- **Simplified Queries and Design**: The denormalization of tables in a star schema leads to simpler database design 
and easier-to-write queries, enhancing understanding and maintenance.
- **Improved Performance**: Denormalized tables reduce the need for complex joins and allow for faster query execution,
particularly beneficial for large-scale data analysis and aggregation.
- **Fast Aggregations**: The structure of the star schema supports quicker aggregations and summarization of data, 
making it suitable for OLAP (Online Analytical Processing) operations.

#### Drawbacks of Star Schema

- **Complexity in Hierarchical Data**: Star schemas can struggle with representing hierarchical data. Complex hierarchies 
often require multiple dimension tables, which can complicate query design and execution.
- **Data Redundancy**: Due to its denormalized nature, a star schema can lead to data redundancy. This can increase 
storage requirements and impact the efficiency of the database.
- **Maintenance Challenges**: As business requirements change, maintaining and updating a star schema can become 
challenging. Adding new dimensions or facts often requires significant restructuring.
- **Query Performance**: While star schemas generally improve query performance, they can still suffer from performance 
issues, especially with very large datasets or highly complex queries.
- **Limited Historical Data Handling**: Star schemas are not always the best at handling historical data, especially 
when dealing with slowly changing dimensions. This can complicate trend analysis over time.

#### Snowflake Schema

- The snowflake schema is an extension of the star schema used in data warehousing, characterized by a more complex structure.
- It consists of a central fact table connected to multiple dimension tables, which are further normalized into 
sub-dimension tables, resembling a snowflake pattern.
- The process of normalizing dimension tables in a snowflake schema typically involves breaking them down to achieve 
normalization up to the Second Normal Form (2NF). This reduces redundancy in the data.
- While a snowflake schema can sometimes be normalized to the Third Normal Form (3NF), it is most commonly associated with 
2NF due to its focus on reducing redundancy without overly complicating the schema.
- The additional levels of normalization in snowflake schemas can lead to more complex query structures and potentially 
slower query performance due to the increased number of joins.

# Upsert in PostgreSQL

In RDBMS language, the term "upsert" refers to inserting a new row in an existing table, or updating the row if it already exists. This is often achieved in PostgreSQL using the `INSERT` statement combined with the `ON CONFLICT` clause.

## INSERT Statement

The `INSERT` statement adds new rows to a table. Values for specific target columns can be added in any order.

### Example: Creating a Customer Address Table

First, let's define a customer address table:

```sql
CREATE TABLE IF NOT EXISTS customer_address (
    customer_id int PRIMARY KEY,
    customer_street varchar NOT NULL,
    customer_city text NOT NULL,
    customer_state text NOT NULL
);
```

### Inserting Data

Now, let's insert data into this table:

```sql

INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
VALUES
    (432, '758 Main Street', 'Chicago', 'IL');
```
## Handling Conflicts with ON CONFLICT

### Scenario: Avoiding Duplicate Customer IDs

If we don't want to update the row if it already exists, we can use the `ON CONFLICT` clause with the `DO NOTHING` option:

```sql
INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
VALUES
    (432, '923 Knox Street', 'Albany', 'NY')
ON CONFLICT (customer_id) 
DO NOTHING;
```

### Scenario: Updating Existing Details

For updating details of an existing customer:

```sql
INSERT INTO customer_address (customer_id, customer_street)
VALUES
    (432, '923 Knox Street, Suite 1')
ON CONFLICT (customer_id) 
DO UPDATE
    SET customer_street = EXCLUDED.customer_street;
```
when this UPSERT operation is executed, PostgreSQL will first try to insert the row (432, '923 Knox Street, Suite 1') 
into the customer_address table. If a row with customer_id = 432 already exists, it will not insert a new row. Instead, 
it will update the existing row's customer_street column with the value '923 Knox Street, Suite 1'.

