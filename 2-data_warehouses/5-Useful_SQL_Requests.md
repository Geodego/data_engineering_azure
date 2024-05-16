# Useful SQL instructions

## Table of Contents
1. [TO_CHAR](#to_char)
   - [Example of Usage](#example-of-usage)
   - [Explanation of the Query](#explanation-of-the-query)
2. [CASE WHEN](#case-when)
   - [Basic Example Usage](#basic-example-usage)
3. [ISODOW](#isodow)
   - [Example](#example)
4. [ETL the Data from 3NF Tables to Facts & Dimension Tables](#etl-the-data-from-3nf-tables-to-facts--dimension-tables)
5. [GROUP BY CUBE](#group-by-cube)
   - [Key Features](#key-features)
   - [Example](#example-1)
6. [GROUPING SETS](#grouping-sets)
   - [Usage Example](#usage-example)
   - [Grouping Set Example](#grouping-set-example)
   - [Warning](#warning)


### TO_CHAR
Example of usage:
```sql
SELECT DISTINCT(TO_CHAR(payment_date :: DATE, 'yyyyMMDD')::integer) AS date_key
FROM payment;
```
Explanation of the query:
- **`TO_CHAR(payment_date :: DATE, 'yyyyMMDD')`**:
  - Converts the `payment_date` column to a string.
  - The `:: DATE` casts the `payment_date` to a date type.
  - `TO_CHAR` formats it as a string in the 'yyyyMMdd' format, e.g., '20240101' for January 1st, 2024.

- **`::integer`**:
  - Converts the formatted date string to an integer. 
  - E.g., '20240101' becomes 20240101.

- **`SELECT DISTINCT`**:
  - Selects unique values only from the converted dates.
  - Ensures that each date appears only once in the output, even if it occurs multiple times in the `payment_date` column.

- **`AS date_key`**:
  - Renames the output column of the query to `date_key`.

The overall purpose of this query is to extract unique dates from the `payment` table, format them as integers in 'yyyyMMdd' format, and list them under the column `date_key`.

### CASE WHEN
The `CASE WHEN` statement in SQL is used for implementing conditional logic within a query. It's akin to if-else 
conditions in other programming languages. There are two types of `CASE` expressions.
Here's a basic example of a CASE WHEN in use:
```sql
SELECT 
    EmployeeName, 
    CASE 
        WHEN Salary > 50000 THEN 'High'
        ELSE 'Low'
    END as SalaryLevel
FROM Employees;
```
### ISODOW
The `ISODOW` function in SQL is used for extracting the ISO weekday number from a date. In the ISO-8601 standard, 
the week starts on Monday (denoted as 1) and ends on Sunday (denoted as 7).

Example:
```sql
SELECT OrderDate, EXTRACT(ISODOW FROM OrderDate) AS ISOWeekday
FROM Orders;
```
In SQL, the EXTRACT function is used to retrieve specific parts of a date or timestamp, such as the year, month, day, 
hour, etc. This function is part of the SQL standard and is available in many SQL database systems, including 
PostgreSQL, which supports a variety of date/time functions and formats.

### ETL the data from 3NF tables to Facts & Dimension Tables
```sql
INSERT INTO dimDate (date_key, date, is_weekend)
SELECT DISTINCT(TO_CHAR(payment_date :: DATE, 'yyyyMMDD')::integer) AS date_key,
       date(payment_date)                                           AS date,
       CASE WHEN EXTRACT(ISODOW FROM payment_date) IN (6, 7) THEN true ELSE false END AS is_weekend
FROM payment;
```

### GROUP BY CUBE

The `CUBE` function in SQL is a tool used in `GROUP BY` clauses. It enables the creation of subtotals and 
grand totals across multiple dimensions. The key features of `CUBE` are:
- **Comprehensive Aggregations**: `GROUP BY CUBE (dim1, dim2, ...)` computes all possible combinations of aggregations 
for the specified dimensions. It generates subtotals for all combinations, along with a grand total.
- **Efficiency in Reporting**: By materializing the view created with `CUBE`, you can significantly reduce repetitive 
aggregation queries, streamlining reporting and analysis processes.

example: 
```SQL
SELECT dimDate.month,dimStore.country,sum(sales_amount) as revenue
FROM factSales
JOIN dimDate  on (dimDate.date_key   = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP by cube(dimDate.month,  dimStore.country);
```
Example output:
The following table provides a summary of sales revenue across different months and countries, including sub-totals and 
grand total.

| Month    | Country | Revenue |
|----------|---------|---------|
| January  | USA     | 1000    |
| January  | Canada  | 1500    |
| February | USA     | 1200    |
| February | Canada  | 1300    |
| January  | **ALL** | 2500    | <!-- Sub-total for January -->
| February | **ALL** | 2500    | <!-- Sub-total for February -->
| **ALL**  | USA     | 2200    | <!-- Sub-total for USA -->
| **ALL**  | Canada  | 2800    | <!-- Sub-total for Canada -->
| **ALL**  | **ALL** | 5000    | <!-- Grand total -->

Notes:
- `ALL` indicates the sub-totals for all months or all countries.


### GROUPING SETS

GROUPING SETS in SQL offer a way to control the granularity of groupings in data aggregation. This feature allows for 
specifying exact groupings of interest in a query.

For instance, consider the SQL query:
```sql
GROUP BY GROUPING SETS ((A), (B), (A, B))
```
This query enables aggregation by A, by B, and then by both A and B. It's important to note that, unlike the CUBE 
operation, GROUPING SETS do not automatically include a grand total aggregation.

The grouping set equivalent of the above `CUBE` example would be:
```SQL
SELECT dimDate.month, dimStore.country, sum(sales_amount) as revenue
FROM factSales
JOIN dimDate  on (dimDate.date_key   = factSales.date_key)
JOIN dimStore on (dimStore.store_key = factSales.store_key)
GROUP BY GROUPING SETS (
    (dimDate.month, dimStore.country), -- Combination of month and country
    (dimDate.month),                   -- Only by month
    (dimStore.country),                -- Only by country
    ()                                 -- Grand total (no grouping)
);
```

**Warning**: before using grouping sets or CUBE, clean your data to avoid any confusion between the `none` used in the 
grouping, meaning the general aggregation, and any `none`in the data. 
