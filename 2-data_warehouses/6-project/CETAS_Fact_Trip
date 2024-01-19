IF OBJECT_ID('dbo.fact_trip') IS NOT NULL
BEGIN
    DROP EXTERNAL TABLE [dbo].[fact_trip];
END
GO

CREATE EXTERNAL TABLE dbo.fact_trip
WITH (
	LOCATION    = 'fact_trip',
	DATA_SOURCE = [data_uproject2_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormatWithHeader]
)
AS
SELECT
    ts.trip_id,
    ts.start_station_id,
    ts.end_station_id,
	rs.rider_id,
    DATEDIFF(minute, CONVERT(DATETIME, LEFT(ts.start_at, 23)), CONVERT(DATETIME, LEFT(ts.ended_at, 23))) AS duration_in_minutes,
    DATEDIFF(year, CONVERT(DATETIME, LEFT(rs.birthday, 23)), CONVERT(DATETIME, LEFT(ts.start_at, 23))) AS rider_age,
    CONVERT(DATETIME, LEFT(ts.start_at, 23)) AS started_at,
    CONVERT(DATETIME, LEFT(ts.ended_at, 23)) AS ended_at,
    CAST(REPLACE(LEFT(ts.start_at, 10), '-', '') AS INT) AS date_key,
    DATEPART(hour, CONVERT(DATETIME, LEFT(ts.start_at, 23))) AS starting_hour
FROM [dbo].[trip_stage] ts
INNER JOIN [dbo].[rider_stage] rs ON ts.rider_id = rs.rider_id;
GO


SELECT TOP 10 * FROM dbo.fact_trip
GO