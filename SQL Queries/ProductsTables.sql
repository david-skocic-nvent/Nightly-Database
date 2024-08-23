USE DW_P360;

DROP TABLE Product2G_Applications;
DROP TABLE Product2G_Assets;
DROP TABLE Product2G_Bullets;
DROP TABLE Product2G_Footnotes;
DROP TABLE Product2G_Langs;
DROP TABLE Product2G_Narratives;
DROP TABLE Product2G_Product_Lines;
DROP TABLE Product2G_References;
DROP TABLE Product2G_Region_Limit_Markets;
DROP TABLE Product2G_Regions;
DROP TABLE Product2G_Structure_Groups;
DROP TABLE Product2Gs;

CREATE TABLE Product2Gs (
    [Identifier] VARCHAR(30) PRIMARY KEY,
    [Modified] DATETIME,
    [MarketToPublic] VARCHAR(30),
    [PrimaryStructureGroupMasterStatus] VARCHAR(20),
    [DisplayOrder] INT,
);

CREATE TABLE Product2G_Structure_Groups (
    [ProductIdentifier] VARCHAR(30),
    [Structure] VARCHAR(30),
    [StructureGroup] VARCHAR(80),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Regions (
    [ProductIdentifier] VARCHAR(30),
    [Region] VARCHAR(20),
    [MarketToPublic] VARCHAR(30),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE,

    PRIMARY KEY([ProductIdentifier], [Region])
);

CREATE TABLE Product2G_Product_Lines (
    [ProductIdentifier] VARCHAR(30),
    [ProductLine] VARCHAR(10),
    [ProductLineTag] VARCHAR(10),
    [LabelEnglish] VARCHAR(10),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Applications (
    [ProductIdentifier] VARCHAR(30),
    [Application] VARCHAR(40),
    [ApplicationTag] VARCHAR(10),
    [LabelEnglish] VARCHAR(80),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Assets (
    [ProductIdentifier] VARCHAR(30),
    [AssetType] VARCHAR(50),
    [Sequence] INT,
    [AssetId] VARCHAR(80),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Langs (
    [ProductIdentifier] VARCHAR(30),
    [Language] VARCHAR(10),
    [DescriptionShort] VARCHAR(300),
    [Abstract] VARCHAR(700),
    [Keyword] VARCHAR(600),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Narratives (
    [ProductIdentifier] VARCHAR(30),
    [Language] VARCHAR(10),
    [Sequence] INT,
    [Narrative] VARCHAR(1800),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Bullets (
    [ProductIdentifier] VARCHAR(30),
    [Language] VARCHAR(10),
    [Sequence] INT,
    [Bullet] VARCHAR(600),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Footnotes (
    [ProductIdentifier] VARCHAR(30),
    [Language] VARCHAR(10),
    [Sequence] INT,
    [Footnote] VARCHAR(800),

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_References (
    [ProductIdentifier] VARCHAR(30),
    [Object] VARCHAR(30),
    [ObjectType] VARCHAR(20),
    [Type] VARCHAR(20),
    [DisplayOrder] INT,

    FOREIGN KEY ([ProductIdentifier])
    REFERENCES Product2Gs([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Product2G_Region_Limit_Markets (
    [ProductIdentifier] VARCHAR(30),
    [Region] VARCHAR(20),
    [Market] VARCHAR(10),

    FOREIGN KEY ([ProductIdentifier], [Region])
    REFERENCES Product2G_Regions([ProductIdentifier], [Region])
    ON DELETE CASCADE
);