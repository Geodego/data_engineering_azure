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
[Download these .csv files](https://video.udacity-data.com/topher/2022/May/6283aff5_data-nyc-payroll/data-nyc-payroll.zip) that provide the data for the project.

