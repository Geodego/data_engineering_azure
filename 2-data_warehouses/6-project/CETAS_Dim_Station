IF OBJECT_ID('dbo.dim_station') IS NOT NULL
BEGIN
    DROP EXTERNAL TABLE [dbo].[dim_station];
END
GO

CREATE EXTERNAL TABLE dbo.dim_station
WITH (
	LOCATION    = 'dim_station',
	DATA_SOURCE = [data_uproject2_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormatWithHeader]
)
AS
SELECT [station_id], [name], [latitude], [longitude]
FROM [dbo].[station_stage];
GO


SELECT TOP 100 * FROM dbo.dim_station
GO