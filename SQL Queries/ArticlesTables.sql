CREATE TABLE Articles(
    [Identifier] VARCHAR(30) PRIMARY KEY,
    [Modified] DATETIME,
    [SupplierAltAID] VARCHAR(30),
    [ProductAssignment] VARCHAR(30),
    [Gtin] VARCHAR(20),
    [MarketToPublic] VARCHAR(20)
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

CREATE TABLE Atricle_Structure_Groups (
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
    [Region] VARCHAR(15),
    [MarketToPublic] VARCHAR(20),
    [ReferenceCode] VARCHAR(20),
    [StockCode] VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Region_Limit_Markets (
    [ArticleIdentifier] VARCHAR(30),
    [Region] VARCHAR(15),
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
    [CombinedValue] VARCHAR(200),
    [CombinedValueWithUnit] VARCHAR(200),
    [SortValue] VARCHAR(150),

    SortValueLanguage VARCHAR(10),
    [Value] VARCHAR(20),
    ValueLanguage VARCHAR(10),
    ValueIdentifier VARCHAR(10),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Article_Attribute_Values(
    [ArticleIdentifier] VARCHAR(30),
    [AttributeNameInKeyLanguage] VARCHAR(80),
    [Identifier] INT,
    [Language] VARCHAR(10),
    [Value] VARCHAR(100),

    FOREIGN KEY ([ArticleIdentifier], [AttributeNameInKeyLanguage])
    REFERENCES Article_Attributes([ArticleIdentifier], [AttributeNameInKeyLanguage])
    ON DELETE CASCADE
);

CREATE TABLE Article_Sales(
    [ArticleIdentifier] VARCHAR(30),
    [Customer] VARCHAR(20),

    FOREIGN KEY ([ArticleIdentifier])
    REFERENCES Articles([Identifier])
    ON DELETE CASCADE
);

CREATE TABLE Atricle_Sale_Price_Group_Ids(
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