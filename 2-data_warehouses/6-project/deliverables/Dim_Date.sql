IF OBJECT_ID('dbo.dim_date') IS NOT NULL
BEGIN
    DROP EXTERNAL TABLE [dbo].[dim_date];
END
GO

CREATE EXTERNAL TABLE dbo.dim_date
WITH (
	LOCATION    = 'dim_date',
	DATA_SOURCE = [data_uproject2_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormatWithHeader]
)
AS
SELECT DISTINCT
    CAST(REPLACE(LEFT(start_at, 10), '-', '') AS INT) AS date_key,
    DATEPART(WEEKDAY, CONVERT(DATETIME, LEFT([start_at], 23))) AS week_day,
	DATEPART(MONTH, CONVERT(DATETIME, LEFT([start_at], 23))) AS month,
    DATEPART(QUARTER, CONVERT(DATETIME, LEFT([start_at], 23))) AS quarter
FROM [dbo].[trip_stage]
UNION
SELECT DISTINCT
    CAST(REPLACE(LEFT([date], 10), '-', '') AS INT) AS date_key,
    DATEPART(WEEKDAY, CONVERT(DATETIME, LEFT([date], 23))) AS week_day,
	DATEPART(MONTH, CONVERT(DATETIME, LEFT([date], 23))) AS month,
    DATEPART(QUARTER, CONVERT(DATETIME, LEFT([date], 23))) AS quarter
FROM [dbo].[payment_stage];
GO

SELECT TOP 100 * FROM dbo.dim_date
GO