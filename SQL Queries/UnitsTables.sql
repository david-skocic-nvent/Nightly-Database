CREATE TABLE Unit_Metadata(
    [Type] VARCHAR(20),
    [Version] VARCHAR(15),
    Mode VARCHAR(10),
    StartTime DATETIME,
    TimeCity VARCHAR(10),
    Environment VARCHAR(10)
);

CREATE TABLE Units (
    Code VARCHAR(40) PRIMARY KEY,
	BaseUnitFactor FLOAT,
	MeasurementSystem VARCHAR(10),
	BaseUnit VARCHAR(40),
    Modified DATETIME,
	[Name] VARCHAR(50),
	[Language] VARCHAR(10),
	Symbol NVARCHAR(20)
);