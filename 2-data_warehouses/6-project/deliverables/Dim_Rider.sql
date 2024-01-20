IF OBJECT_ID('dbo.dim_rider') IS NOT NULL
BEGIN
    DROP EXTERNAL TABLE [dbo].[dim_rider];
END
GO

CREATE EXTERNAL TABLE dbo.dim_rider
WITH (
	LOCATION    = 'dim_rider',
	DATA_SOURCE = [data_uproject2_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormatWithHeader]
)
AS
SELECT [rider_id],
	   [address],
       [first],
       [last],
       CONVERT(DATETIME, LEFT([birthday], 23)) AS birthday,
       [is_member],
	   DATEDIFF(year, CONVERT(DATETIME, LEFT([birthday], 23)), CONVERT(DATETIME, LEFT([account_start_date], 23))) AS age_at_account_start
FROM [dbo].[rider_stage];
GO


SELECT TOP 100 * FROM dbo.dim_rider
GO