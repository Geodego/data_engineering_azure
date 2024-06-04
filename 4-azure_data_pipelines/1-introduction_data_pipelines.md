#  Introduction to Data pipelines

## Table of Contents
- [Introduction to Data Pipelines in Azure](#introduction-to-data-pipelines-in-azure)
- [Business Stakeholders](#business-stakeholders)
- [Resources](#resources)

## Introduction to Data Pipelines in Azure

Data engineers are often responsible for moving data from one place to another.

An example is taking data from an OLTP system and making it available in a data warehouse for analytics or a data lake 
for machine learning. In order to accomplish this movement and data transformation, data will have to be loaded, 
transformed, and moved, in steps or stages, from the OLTP system data sources to the data warehouse or data lake.

This data movement and transformation in steps or stages is referred to as a data pipeline.

A data pipeline defines the flow of data from one part of a system to another, and what happens to the data as it moves 
through this flow.

The data moving through these pipelines can be from anywhere and at any scale

The data flow in a data pipeline is a visual representation of where the data comes from, the ways the data is changed 
in stages or steps through the flow, and where the data ends up. For example:
- In the beginning of the data flow, the diagram defines the data source and the schema of the data in the source, 
defining the structure of the source data as it is copied into datasets in the data pipeline
- The next part of this data flow defines some way the data will be joined with other data
- In the next stage of the data flow, this data is aggregated in some way
- And in this next part, the data is transformed in some way
- In the last part of the data flow, a mapping is defined between the data after it has been joined, aggregated, and 
transformed, and where the data will land, often called a sink.

This flow of data and what happens to it is the data pipeline.

There are two main tools in the Microsoft Azure cloud platform used to create data pipelines
- The first one is called Azure Data Factory.
- And the other one is Synapse Analytics, referred to as Synapse Pipelines in the Synapse workspace.



## Business Stakeholders

As a data engineer who works with data pipelines, you will encounter a broad range of individuals because this role sits 
at the center of many processes.

On the business side, you will likely encounter product owners, business analysts, and project managers. On the 
technical side, you will likely encounter database and system administrators, data analysts, and data scientists. 
The data engineer is critical to all of these stakeholders.

## Resources
- [Introduction to data pipelines in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/introduction)
- [Microsoft Azure Fundamentals: Describe core Azure concepts](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/)
- [Explore Azure database and analytics services](https://docs.microsoft.com/en-us/learn/modules/azure-database-fundamentals/)
- [Azure Introduction to Apache Spark](https://docs.microsoft.com/en-us/azure/databricks/getting-started/spark/)



