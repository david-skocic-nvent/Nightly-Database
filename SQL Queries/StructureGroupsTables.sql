CREATE TABLE Structure_Group_Metadata(
    [Type] VARCHAR(20),
    [Version] VARCHAR(15),
    Mode VARCHAR(10),
    StartTime DATETIME,
    TimeCity VARCHAR(10),
    Environment VARCHAR(10)
);

CREATE TABLE Structure_Groups(
    Identifier VARCHAR(50) PRIMARY KEY,
    Facet VARCHAR(20),
    NodeType VARCHAR(10),
    ShowProducts VARCHAR(10),
    FacetSequence INT,
    Brand VARCHAR(15),
    DisplayOrder INT,
    [Level] SMALLINT,
    ChartSort VARCHAR(10),
    ChartStyle VARCHAR(20),
    ChartPackingQuantity VARCHAR(10),
    StructureReference VARCHAR(20),
    Modified DATETIME,
    MasterStatus VARCHAR(20),
    ParentIdentifier VARCHAR(50),
    RestrictUnits VARCHAR(10),
);

CREATE TABLE Structure_Group_Attributes (
    Identifier VARCHAR(50),
    NameInKeyLanguage VARCHAR(60),
    DisplayOrder INT,
    Unit VARCHAR(40),
    ValueIdentifier VARCHAR(10),

    FOREIGN KEY (Identifier)
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE,

    FOREIGN KEY (Unit)
    REFERENCES Units(Code)
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Group_Langs (
    Identifier VARCHAR(50),
    [Language] VARCHAR(10),
    Content VARCHAR(2000),
    [Name] VARCHAR(100),

    FOREIGN KEY (Identifier)
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Narratives (
    Identifier VARCHAR(50),
    [Language] VARCHAR(10),
    Narrative VARCHAR(1000),
    [Sequence] VARCHAR(10),

    FOREIGN KEY (Identifier)
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Bullets (
    Identifier VARCHAR(50),
    [Language] VARCHAR(10),
    Bullet NVARCHAR(100),
    [Sequence] VARCHAR(10),

    FOREIGN KEY (Identifier)
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Assets (
    Identifier VARCHAR(50),
    AssetID VARCHAR(50),
    [Sequence] INT,
    AssetType VARCHAR(30),

    
    FOREIGN KEY (Identifier)
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE
);

