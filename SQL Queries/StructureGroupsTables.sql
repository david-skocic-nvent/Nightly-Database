CREATE TABLE Structure_Groups(
    [Identifier] VARCHAR(50) PRIMARY KEY,
    [StructureReference] VARCHAR(20),
    [Modified] DATETIME,
    [DisplayOrder] INT,
    [NodeType] VARCHAR(10),
    [Level] SMALLINT,
    [MasterStatus] VARCHAR(20),
    [ShowProducts] BOOLEAN,
    [ParentIdentifier] VARCHAR(50),
    [Brand] VARCHAR(15),
    [ChartSort] VARCHAR(10),
    [ChartPackingQuantity] BOOLEAN,
    [ChartStyle] VARCHAR(20),
    [RestrictUnits] VARCHAR(10),
);

CREATE TABLE Structure_Group_Attributes (
    [StructureGroupIdentifier] VARCHAR(50),
    [NameInKeyLanguage] VARCHAR(60),
    [DisplayOrder] INT,
    [Unit] VARCHAR(40),
    [FacetType] VARCHAR(10),
    [ShowFractions] BOOLEAN,
    [ChartDisplay] VARCHAR(20),
    [ShowDecimals] INT,

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups(Identifier)
    ON DELETE CASCADE,

    FOREIGN KEY ([Unit])
    REFERENCES Units(Code)
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Group_Attribute_Preset_Values(
    [Identifier] VARCHAR(30),
    [StructureGroupIdentifier] VARCHAR(50),
    [AttributeNameInKeyLanguage] VARCHAR(60),
    [StructureValueProxy] VARCHAR(100),
    [DisplayOrder] INT,

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Group_Attributes(Identifier)
    ON DELETE CASCADE,

    FOREIGN KEY ([AttributeNameInKeyLanguage])
    REFERENCES Structure_Group_Attributes(NameInKeyLanguage)
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Group_Attributes_Values(
    [Identifier] VARCHAR(10),
    [StructureGroupIdentifier] VARCHAR(50),
    [AttributeNameInKeyLanguage] VARCHAR(60),
    [Value] VARCHAR(280),
    [Language] VARCHAR(10),

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Group_Attributes(Identifier)
    ON DELETE CASCADE,

    FOREIGN KEY ([AttributeNameInKeyLanguage])
    REFERENCES Structure_Group_Attributes(NameInKeyLanguage)
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Group_Langs (
    [StructureGroupIdentifier] VARCHAR(50),
    [Language] VARCHAR(10),
    [Name] VARCHAR(100),
    [Abstract] VARCHAR(400),
    [Content] VARCHAR(14000),

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Narratives (
    [StructureGroupIdentifier] VARCHAR(50),
    [Language] VARCHAR(10),
    [Narrative] VARCHAR(1200),
    [Sequence] INT,

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Bullets (
    [StructureGroupIdentifier] VARCHAR(50),
    [Language] VARCHAR(10),
    [Bullet] NVARCHAR(400),
    [Sequence] INT,

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Assets (
    [StructureGroupIdentifier] VARCHAR(50),
    [AssetID] VARCHAR(50),
    [Sequence] INT,
    [AssetType] VARCHAR(30),

    
    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Facets (
    [StructureGroupIdentifier] VARCHAR(50),
    [Facet] VARCHAR(15),
    [Sequence] INT,

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

