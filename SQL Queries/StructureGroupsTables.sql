CREATE TABLE Structure_Group_Metadata(
    [Type] VARCHAR(20),
    [Version] VARCHAR(15),
    Mode VARCHAR(10),
    StartTime DATETIME,
    TimeCity VARCHAR(10),
    Environment VARCHAR(10)
);

CREATE TABLE Structure_Groups(
    StructureGroupTableID INT PRIMARY KEY IDENTITY(1,1),
    Facet VARCHAR(20),
    NodeType VARCHAR(10),
    ShowProducts VARCHAR(10),
    FacetSequence INT,
    Identifier VARCHAR(50),
    Brand VARCHAR(15),
    DisplayOrder INT,
    [Level] SMALLINT,
    ChartSort VARCHAR(10),
    ChartStyle VARCHAR(20),
    ChartPackingQuantity VARCHAR(10),
    StructureReference VARCHAR(20),
    Modified DATETIME,
    MasterStatus VARCHAR(20),
    ParentIdentifier VARCHAR(30),
    RestrictUnits VARCHAR(10),
    CONSTRAINT UQ_Identifier UNIQUE (Identifier)
);

CREATE TABLE Structure_Group_Attributes (
    StructureGroupTableID INT,
    NameInKeyLanguage VARCHAR(60),
    [Value] VARCHAR(50),
    [Language] VARCHAR(40),
    ValueIdentifier VARCHAR(10),

    CONSTRAINT Fk_StructureGroupTableID_Attributes
        FOREIGN KEY (StructureGroupTableID)
        REFERENCES Structure_Groups(StructureGroupTableID)
        ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Langs (
    StructureGroupTableID INT,
    [Language] VARCHAR(10),
    Content VARCHAR(2000),
    [Name] VARCHAR(100),

    CONSTRAINT Fk_StructureGroupTableID_Langs
        FOREIGN KEY (StructureGroupTableID)
        REFERENCES Structure_Groups(StructureGroupTableID)
        ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Narratives (
    StructureGroupTableID INT,
    [Language] VARCHAR(10),
    Narrative VARCHAR(1000),
    [Sequence] VARCHAR(10),

    CONSTRAINT Fk_StructureGroupTableID_Narratives
        FOREIGN KEY (StructureGroupTableID)
        REFERENCES Structure_Groups(StructureGroupTableID)
        ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Bullets (
    StructureGroupTableID INT,
    [Language] VARCHAR(10),
    Bullet NVARCHAR(100),
    [Sequence] VARCHAR(10),

    CONSTRAINT Fk_StructureGroupTableID_Bullets
        FOREIGN KEY (StructureGroupTableID)
        REFERENCES Structure_Groups(StructureGroupTableID)
        ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Assets (
    StructureGroupTableID INT,
    AssetID VARCHAR(50),
    [Sequence] INT,
    AssetType VARCHAR(30),

    CONSTRAINT Fk_StructureGroupTableID_Assets
        FOREIGN KEY (StructureGroupTableID)
        REFERENCES Structure_Groups(StructureGroupTableID)
        ON DELETE CASCADE
);

