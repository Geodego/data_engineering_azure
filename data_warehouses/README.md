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

Reference constraints in a star schema, are crucial for maintaining data integrity and ensuring accurate, reliable 
reporting:
- **Reference Constraints**: Rules established to maintain consistent relationships between the tables in a star schema, 
often implemented as foreign key constraints.

- **Foreign Key Constraints**: Ensure that each entry in the fact table corresponds to a valid record in a dimension 
table, linking data like sales records in the fact table to specific entities in dimension tables such as products and customers.

- **Data Integrity**: These constraints prevent orphan records in the fact table and ensure that data in dimension 
tables can't be deleted or altered in a way that invalidates the relationships.

- **Simplified Queries and Analysis**: By enforcing clear relationships between different data elements, these 
constraints make it easier to write queries and perform analysis.

- **Performance Optimization**: While adding overhead during data loading, reference constraints often improve query 
performance by enabling the database to optimize query execution plans more effectively.


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

### DWH Architectures

#### Kimball's Bus Architecture

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

#### Independent Data Marts


A data mart is a subset of a data warehouse that is usually oriented to a specific business line or team. Whereas data 
warehouses have enterprise-wide depth, the information in data marts pertains to a single department or business unit.

Data marts are small in size and are more flexible than a data warehouse but are limited in the scope of information. 
They are used by small groups within an organization to analyze and report on specific business functions. For instance, 
the marketing department of a large company might use a data mart to track web analytics or sales performance.

- Departments have separate ETL processes & dimensional models
- These separate dimensional models are called “Data Marts”
- Different fact tables for the same events, no conformed dimensions
- Uncoordinated efforts can lead to inconsistent views
- Despite awareness of the emergence of this architecture from departmental autonomy, it is generally discouraged
- 
![independent_DMarts](./0-images/independent_DMarts.png "independent_DMarts.png")

#### Inmon's Corporate Information Factory

- 2 ETL Process
  - Source systems → 3NF database (data acquisition)
  - 3NF database → Departmental Data Marts (data delivery)
- The 3NF database acts as an enterprise-wide data store.
  - Single integrated source of truth for data-marts
  - Could be accessed by end-users if needed
- Data marts are dimensionally modeled & unlike Kimball’s dimensional models, they are mostly aggregated

![inmon_cif](./0-images/inmon_cif.png "inmon_cif.png")

#### Best of Both Worlds: Hybrid Kimball Bus & Inmon CIF

- Removes Data Marts
- Exposes the enterprise data warehouse

![hybrid_kimball_inmon](./0-images/hybrid_kimball_inmon.png "hybrid_kimball_inmon.png")

### OLAP cubes

Once we have a star schema, we can create OLAP cubes.

- An OLAP cube is an aggregation of at a number of dimensions
  - Movie, Branch, Month
- Easy to communicate to business users

![olap_cubes](./0-images/olap_cubes.png "olap_cubes.png")

#### Roll Up and Drill Down

- Roll-up: Sum up the sales of each city by Country: e.g. US, France (less columns in branch dimension)
- Drill-Down: Decompose the sales of each city into smaller districts (more columns in branch dimension)
- The OLAP cubes should store the finest grain of data (atomic data), in case we need to drill-down to the lowest level, 
e.g Country -> City -> District -> street ...

#### Slice and Dice

- Slice: Reducing N dimensions to N-1 dimensions by restricting one dimension to a single value
- Dice: Same dimensions but computing a sub-cube by restricting, some of the values of the dimensions

#### Query Optimization

- Do one pass through the facts table (e.g. with "GROUP BY CUBE(movie, branch, month)"). 
- This will aggregate all possible combinations of grouping.







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