# Cloud Data Warehouses with Azure

## Introduction to  Data Warehouses 

### History of data warehousing

Data warehousing started in the 1960s, with the term being used starting in the 1970s by Bill Inmon.

Parallel processing led to the development of massively parallel processing architectures in the 1990s. By the early 
2000s, many data storage problems had been solved giving rise to the term "big data." In 2006, the Hadoop project was 
founded and ultimately led to the ability to incorporate semi-structured and unstructured data into modern data warehouses.

### Roles and stakeholders in data warehousing

You will encounter a broad range of stakeholders as a data engineer because this role sits at the center of many processes. These roles will typically fall into one of two categories, business or technical.

**Business**:
- Product owners
- Business analysts
- Project managers

**Technical**:
- Database and system administrators
- Data analysts
- Data scientists.
The data engineer is critical to all of these stakeholders.

### Operational vs Analytical Business Processes
Operational Processes: 
- Find goods & make orders (for customers)
- Stock and find goods (for inventory staff)
- Pick up & deliver goods (for delivery staff)

Analytical Processes: 
- Assess the performance of sales staff (for HR)
- See the effect of different sales channels (for marketing)
- Monitor sales growth (for management)

Operational databases:
- Excellent for operations
- No redundancy, high integrity (3NF)
- Too slow for analytics, too many joins
- Too hard to understand

Having the same data source for operational & analytical processes is not a good solution. The general solution is the 
warehouse. We connect to these operational databases and load them to the warehouse. Thats the idea of OLTP vs OLAP.

![oltp-olap_schema](./0-images/oltp-olap.png "OLTP OLAP schema")

### Data Warehouse: Technical Perspective
Goal:
- Easy to understand 
- performant
- quality assured
- handles new questions well
- secure

Technical paerspective:
- Extract the data from the source systems used for operations, transform the data, and load it into a dimensional model.
- Business-user-facing application are needed, with clear visuals - Business Intelligence (BI) apps

![dw-tech-perspective](./0-images/dw-tech-perspective.png "dw-tech-perspective.png")

### Dimensional model
Goals of the Star Schema:
- Easy to understand
- Fast analytical query performance

Fact Tables:
- Record business events, like an order, a phone call, a book review
- Fact tables columns record events recorded in quantifiable metrics like quantity of an item, duration of a call, 
a book rating. In most cases, a numerical and additive value.

Dimension Tables:
- Record the context of the business events, e.g. who, what, where, why, etc..
- Dimension tables columns contain attributes like the store at which an item is purchased, or the customer who made 
the call, etc.

### Example: The DVD Rentals Sample Database. From 3NF to Star schema

![dvd-rental-db](./0-images/dvd-rental-db.png "dvd-rental-db.png")

- To master the art of dimensional modelling, ones need to see a lot of schemas and think about how to design facts &
dimensions from them.
- the example considered here is called the Sakila database (small database)

**Naive Extract Transform and Load (ETL): From Third Normal Form to ETL**
- Extract:
  - Query the 3NF DB
- Transform:
  - Join tables together
  - Change types
  - Add new columns
- Load:
  - Insert into facts & dimension tables

### DWH Architecture, Kimball's Bus Architecture

ETL: A Closer Look
- Extracting:
  - Transfer data to the warehouse
  - Possibly deleting old states
- Transforming:
  - Integrates many sources together
  - Possibly cleansing: inconsistencies, duplication, missing values, etc..
  - Possibly producing diagnostic metadata
- Loading:
  - Structuring and loading the data into the dimensional data model

![kimball](./0-images/kimball.png "kimball.png")

### Definitions
- **Schema**: The structure of data described in a formal way supported by the database management system.

- **Data Warehouse**: 
  - A central storage of information that can be queried and used for analysis.
  - A data warehouse is a copy of transaction data specifically structured for query and analysis. - Kimball
  - A data warehouse is a subject-oriented, integrated, nonvolatile, and time-variant collection of data in support of 
  management's decisions. - Inmon
  - A data warehouse is a system that retrieves and consolidates data periodically from the source systems into a 
  dimensional or normalized data store. It usually keeps years of history and is queried for business intelligence 
  or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system. -



## ELT and Data Warehouse Technology in the Cloud

## Azure Data Warehouse Technology 