IF OBJECT_ID('dbo.fact_payments') IS NOT NULL
BEGIN
    DROP EXTERNAL TABLE [dbo].[fact_payments];
END
GO

CREATE EXTERNAL TABLE dbo.fact_payments
WITH (
	LOCATION    = 'fact_payments',
	DATA_SOURCE = [data_uproject2_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormatWithHeader]
)
AS
SELECT rs.rider_id,
       CONVERT(DATETIME, LEFT(ps.[date], 23)) AS payment_date,
	   CAST(REPLACE(LEFT(ps.date, 10), '-', '') AS INT) AS date_key,
	   ps.amount as payment_amount
FROM [dbo].[payment_stage] ps
INNER JOIN [dbo].[rider_stage] rs ON ps.rider_id = rs.rider_id;
GO