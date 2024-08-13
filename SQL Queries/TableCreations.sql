
CREATE TABLE Product2Gs (
    MetaID INT,
    P2GTableID INT PRIMARY KEY IDENTITY(1,1),
    MarketToPublic VARCHAR(20),
	PrimaryStructureGroupMasterStatus VARCHAR(15),
	ProductLine VARCHAR(10),
	ProductLineTag VARCHAR(5),
    Identifier VARCHAR(20),
	ProductLineLabelEnglish VARCHAR(10),
	DisplayOrder INT,
    FOREIGN KEY MetaID REFERENCES Metadata(MetaID)
);

CREATE TABLE Product2GStructureGroups (
    P2GTableID INT,
    StructureGroup VARCHAR(20),
    Structure VARCHAR(10),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsRegions (
    P2GTableID INT,
    Region VARCHAR(15),
    MarketToPublic VARCHAR(15),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsAssets (
    P2GTableID INT,
    [Sequence] INT,
    AssetID VARCHAR(40),
    AssetType VARCHAR(25),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsLangs (
    P2GTableID INT,
    [Language] VARCHAR(10),
    Keyword VARCHAR(200),
    DescriptionShort VARCHAR(200),
    Abstract VARCHAR(200),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsBullets (
    P2GTableID INT,
    [Language] VARCHAR(10),
    Sequence INT,
    Bullet VARCHAR(200),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsFootNotes (
    P2GTableID INT,
    [Language] VARCHAR(10),
    Sequence INT,
    FootNote VARCHAR(200),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsNarratives (
    P2GTableID INT,
    [Language] VARCHAR(10),
    Sequence INT,
    Narrative VARCHAR(500),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsReferences (
    P2GTableID INT,
    DisplayOrder INT,
    [TYPE] VARCHAR(20),
    ObjectType VARCHAR(20),
    [Object] VARCHAR(25),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

CREATE TABLE Product2GsApplications (
    P2GTableID INT,
    LabelEnglish VARCHAR(50),
    ApplicationTag VARCHAR(10),
    [Application] VARCHAR(30),

    FOREIGN KEY (P2GTableID) REFERENCES Product2Gs(P2GTableID)
);

/*
**********************************************************************
*/
