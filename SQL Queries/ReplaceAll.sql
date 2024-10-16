USE DW_P360;

DROP TABLE Structure_Feature_Langs;
DROP TABLE Structure_Feature_Preset_Values;
DROP TABLE Structure_Features;
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
DROP TABLE Article_Applications;
DROP TABLE Article_Assets;
DROP TABLE Article_Attribute_Values;
DROP TABLE Article_Attributes;
DROP TABLE Article_Langs;
DROP TABLE Article_Product_Lines;
DROP TABLE Article_References;
DROP TABLE Article_Region_Limit_Markets;
DROP TABLE Article_Regions;
DROP TABLE Article_Sale_Price_Group_Ids;
DROP TABLE Article_Sales;
DROP TABLE Article_Structure_Groups;
DROP TABLE Articles;
DROP TABLE Structure_Group_Langs;
DROP TABLE Structure_Group_Narratives;
DROP TABLE Structure_Group_Bullets;
DROP TABLE Structure_Group_Assets;
DROP TABLE Structure_Group_Facets;
DROP TABLE Structure_Group_Attribute_Preset_Values;
DROP TABLE Structure_Group_Attribute_Values;
DROP TABLE Structure_Group_Attributes;
DROP TABLE Structure_Groups;
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

USE DW_P360;



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
    [LanguageStatus] VARCHAR(15),
    [Name] VARCHAR(300),
    [Abstract] VARCHAR(400),
    [Content] VARCHAR(max),

    FOREIGN KEY ([StructureGroupIdentifier])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Structure_Group_Narratives (
    [StructureGroupIdentifier] VARCHAR(50),
    [Language] VARCHAR(10),
    [Narrative] NVARCHAR(1500),
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
    [AssetId] VARCHAR(50),
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

USE DW_P360;



CREATE TABLE Structure_Features (
    [Identifier] VARCHAR(30) PRIMARY KEY,
    [StructureReference] VARCHAR(15),
    [Modified] DATETIME,
    [NameInKeyLanguage] VARCHAR(120),
    [Datatype] VARCHAR(30),
    [Purpose] VARCHAR(120),
    [Unit] VARCHAR(40),
    [Annotation] VARCHAR(30),

    FOREIGN KEY ([Unit])
    REFERENCES Units([Code])
    ON DELETE NO ACTION
);

CREATE TABLE Structure_Feature_Langs (
        [StructureFeatureIdentifier] VARCHAR(30),
        [Language] VARCHAR(10),
        [Description] VARCHAR(150),

        FOREIGN KEY (StructureFeatureIdentifier)
        REFERENCES Structure_Features([Identifier])
        ON DELETE CASCADE
);

CREATE TABLE Structure_Feature_Preset_Values (
        [StructureFeatureIdentifier] VARCHAR(30),
        [StructureValueProxy] VARCHAR(200),
        [Identifier] VARCHAR(30),
        [DisplayOrder] INT,
        [AssetId] VARCHAR(60),

        FOREIGN KEY (StructureFeatureIdentifier)
        REFERENCES Structure_Features([Identifier])
        ON DELETE CASCADE
);

USE DW_P360;



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

CREATE TABLE Articles(
    [Identifier] VARCHAR(30) PRIMARY KEY,
    [Modified] DATETIME,
    [SupplierAltAID] VARCHAR(30),
    [ProductAssignment] VARCHAR(30),
    [Gtin] VARCHAR(20),
    [MarketToPublic] VARCHAR(20),
    [OrderUnit] VARCHAR(40),
    [ContentUnit] VARCHAR(40),
    [NoCUperOU] FLOAT,
    [QuantityInterval] FLOAT,
    [PrimaryStructureGroupMasterStatus] VARCHAR(20),
    [RealEAN] VARCHAR(20),
    [Step] VARCHAR(10),

    FOREIGN KEY ([OrderUnit])
    REFERENCES Units([Code])
    ON DELETE NO ACTION,

    FOREIGN KEY ([ContentUnit])
    REFERENCES Units([Code])
    ON DELETE NO ACTION
);

CREATE TABLE Article_Structure_Groups (
    [ArticleIdentifier] VARCHAR(30),
    [StructureGroup] VARCHAR(50),
    [Structure] VARCHAR(30),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE,
    
    FOREIGN KEY ([StructureGroup])
    REFERENCES Structure_Groups([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Regions (
    [ArticleIdentifier] VARCHAR(30),
    [Region] VARCHAR(20),
    [MarketToPublic] VARCHAR(20),
    [ReferenceCode] VARCHAR(20),
    [StockCode] VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE,

    PRIMARY KEY([ArticleIdentifier],[Region])
);

CREATE TABLE Article_Region_Limit_Markets (
    [ArticleIdentifier] VARCHAR(30),
    [Region] VARCHAR(20),
    [Market] VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier],[Region])
    REFERENCES Article_Regions([ArticleIdentifier],[Region])
    ON DELETE CASCADE
);

CREATE TABLE Article_Product_Lines (
    [ArticleIdentifier] VARCHAR(30),
    [ProductLine] VARCHAR(20),
    [ProductLineTag] VARCHAR(20),
    [LabelEnglish] VARCHAR(20),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Applications(
    [ArticleIdentifier] VARCHAR(30),
    [Application] VARCHAR(40),
    [ApplicationTag] VARCHAR(10),
    [LabelEnglish] VARCHAR(50),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Assets(
    [ArticleIdentifier] VARCHAR(30),
    [AssetId] VARCHAR(50),
    [AssetType] VARCHAR(20),
    [Sequence] INT,

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);


CREATE TABLE Article_Langs(
    [ArticleIdentifier] VARCHAR(30),
    [DescriptionSystem] VARCHAR(100),
    [DescriptionShort] VARCHAR(250),
    [Language] VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Attributes(
    [ArticleIdentifier] VARCHAR(30),
    [NameInKeyLanguage] VARCHAR(80),
    [CombinedValue] VARCHAR(600),
    [CombinedValueWithUnit] VARCHAR(200),
    [SortValue] VARCHAR(150),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE,

    PRIMARY KEY([ArticleIdentifier], [NameInKeyLanguage])
);

CREATE TABLE Article_Attribute_Values(
    [ArticleIdentifier] VARCHAR(30),
    [AttributeNameInKeyLanguage] VARCHAR(80),
    [Identifier] INT,
    [Language] VARCHAR(10),
    [Value] VARCHAR(100),

    FOREIGN KEY ([ArticleIdentifier], [AttributeNameInKeyLanguage])
    REFERENCES Article_Attributes([ArticleIdentifier], [NameInKeyLanguage])
    ON DELETE CASCADE
);

CREATE TABLE Article_Sales(
    [ArticleIdentifier] VARCHAR(30),
    [Customer] VARCHAR(20),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE,

    PRIMARY KEY ([ArticleIdentifier], [Customer])
);

CREATE TABLE Article_Sale_Price_Group_Ids(
    [ArticleIdentifier] VARCHAR(30),
    [SalesCustomer] VARCHAR(20),
    [Identifier] VARCHAR(20),
    [Code] VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier], [SalesCustomer])
    REFERENCES Article_Sales([ArticleIdentifier], [Customer])
    ON DELETE CASCADE
);

CREATE TABLE Article_References(
    [ArticleIdentifier] VARCHAR(30),
    [Object] VARCHAR(30),
    [ObjectType] VARCHAR(20),
    [Type] VARCHAR(20),
    [DisplayOrder] INT,

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);