USE DW_P360;

DROP TABLE Structure_Group_Langs;
DROP TABLE Structure_Group_Narratives;
DROP TABLE Structure_Group_Bullets;
DROP TABLE Structure_Group_Assets;
DROP TABLE Structure_Group_Facets;
DROP TABLE Structure_Group_Attribute_Preset_Values;
DROP TABLE Structure_Group_Attribute_Values;
DROP TABLE Structure_Group_Attributes;
DROP TABLE Structure_Groups;

CREATE TABLE Structure_Groups(
    [Identifier] VARCHAR(50) PRIMARY KEY,
    [StructureReference] VARCHAR(20),
    [Modified] DATETIME,
    [DisplayOrder] INT,
    [NodeType] VARCHAR(10),
    [Level] SMALLINT,
    [MasterStatus] VARCHAR(20),
    [ShowProducts] VARCHAR(10),
    [ParentIdentifier] VARCHAR(50),
    [Brand] VARCHAR(15),
    [ChartSort] VARCHAR(10),
    [ChartPackingQuantity] VARCHAR(10),
    [ChartStyle] VARCHAR(20),
    [RestrictUnits] VARCHAR(10),
);

CREATE TABLE Structure_Group_Attributes (
    [StructureGroupIdentifier] VARCHAR(50),
    [NameInKeyLanguage] VARCHAR(60),
    [DisplayOrder] INT,
    [Unit] VARCHAR(40),
    [FacetType] VARCHAR(10),
    [ShowFractions] VARCHAR(10),
    [ChartDisplay] VARCHAR(20),
    [ShowDecimals] INT,

    PRIMARY KEY ([StructureGroupIdentifier],[NameInKeyLanguage]),

    FOREIGN KEY (StructureGroupIdentifier)
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

    FOREIGN KEY ([StructureGroupIdentifier], [AttributeNameInKeyLanguage])
    REFERENCES Structure_Group_Attributes([StructureGroupIdentifier], [NameInKeyLanguage])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Attribute_Values(
    [Identifier] VARCHAR(10),
    [StructureGroupIdentifier] VARCHAR(50),
    [AttributeNameInKeyLanguage] VARCHAR(60),
    [Value] VARCHAR(280),
    [Language] VARCHAR(10),

    FOREIGN KEY ([StructureGroupIdentifier], [AttributeNameInKeyLanguage])
    REFERENCES Structure_Group_Attributes([StructureGroupIdentifier], [NameInKeyLanguage])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Langs (
    [StructureGroupIdentifier] VARCHAR(50),
    [Language] VARCHAR(10),
    [Name] VARCHAR(100),
    [Abstract] VARCHAR(400),
    [Content] VARCHAR(max),

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

