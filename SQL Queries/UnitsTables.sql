USE DW_P360;
DROP TABLE Unit_Langs;
DROP TABLE Units;

CREATE TABLE Units (
    [Code] VARCHAR(40) PRIMARY KEY,
	[BaseUnitFactor] FLOAT,
	[MeasurementSystem] VARCHAR(10),
	[BaseUnit] VARCHAR(40),
    [Modified] DATETIME,
);

CREATE TABLE Unit_Langs (
    [UnitCode] VARCHAR(40),
    [Language] VARCHAR(10),
	[Symbol] NVARCHAR(20),
    [Name] VARCHAR(50),

    FOREIGN KEY ([UnitCode])
    REFERENCES Units([Code])
    ON DELETE CASCADE
);