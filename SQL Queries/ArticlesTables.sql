CREATE TABLE Article_Metadata(
    [Type] VARCHAR(20),
    [Version] VARCHAR(15),
    Mode VARCHAR(10),
    StartTime DATETIME,
    TimeCity VARCHAR(10),
    Environment VARCHAR(10)
);

CREATE TABLE Articles(
    ArticleTableID INT IDENTITY(1,1) PRIMARY KEY,
    Customer VARCHAR(15),
    PriceGroupIDCode VARCHAR(10),
    PriceGroupIDIdentifier VARCHAR(10),
    QuantityInterval FLOAT,
    ProductLineTag VARCHAR(10),
    ArticleIdentifier VARCHAR(20),
    NoCUperOU FLOAT,
    Modified DATETIME,
    OrderUnit VARCHAR(40),
    Step VARCHAR(10),
    PrimaryStructureGroupMasterStatus VARCHAR(20),
    Gtin VARCHAR(20),
    ContentUnit VARCHAR(40),
    ProductLine VARCHAR(10),
    RealEAN VARCHAR(20),
    SupplierAltAID VARCHAR(20),
    ProductAssignment VARCHAR(20),
    ProductLineLabelEnglish VARCHAR(20),

    CONSTRAINT Fk_OrderUnit
        FOREIGN KEY (OrderUnit)
        REFERENCES Units(Code)
        ON DELETE NO ACTION,

    CONSTRAINT Fk_ContentUnit
        FOREIGN KEY (ContentUnit)
        REFERENCES Units(Code)
        ON DELETE NO ACTION
);

CREATE TABLE Atricle_Structure_Groups (
    ArticleTableID INT,
    StructureGroup VARCHAR(50),
    Structure VARCHAR(10),

    CONSTRAINT Fk_ArticleTableID_Structure_Groups
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE,
    CONSTRAINT Fk_StructureGroup
        FOREIGN KEY (StructureGroup)
        REFERENCES Structure_Groups(Identifier)
        ON DELETE CASCADE
);

CREATE TABLE Article_Regions (
    ArticleTableID INT,
    Region VARCHAR(15),
    MarketToPublic VARCHAR(20),
    ReferenceCode INT,
    StockCode VARCHAR(10),

    CONSTRAINT Fk_ArticleTableID_Regions
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);

CREATE TABLE Article_Applications(
    ArticleTableID INT,
    [Application] VARCHAR(40),
    ApplicationTag VARCHAR(10),
    LabelEnglish VARCHAR(50),

    CONSTRAINT Fk_ArticleTableID_Applications
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);

CREATE TABLE Article_Langs(
    ArticleTableID INT,
    DescriptionSystem VARCHAR(70),
    DescriptionShort VARCHAR(150),
    [Language] VARCHAR(10),

    CONSTRAINT Fk_ArticleTableID_Langs
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);

CREATE TABLE Article_Attributes(
    ArticleTableID INT,
    NameInKeyLanguage VARCHAR(60),
    SortValue FLOAT,
    SortValueLanguage VARCHAR(10),
    CombinedValue VARCHAR(20),
    CombinedValueLanguage VARCHAR(10),
    CombinedValueWithUnit VARCHAR(20),
    CombinedValueWithUnitLanguage VARCHAR(10),
    [Value] VARCHAR(20),
    ValueLanguage VARCHAR(10),
    ValueIdentifier VARCHAR(10),

    CONSTRAINT Fk_ArticleTableID_Attributes
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);

CREATE TABLE Article_Assets(
    ArticleTableID INT,
    AssetID VARCHAR(50),
    AssetType VARCHAR(20),
    [Sequence] INT,

    CONSTRAINT Fk_ArticleTableID_Assets
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);

CREATE TABLE Article_References(
    ArticleTableID INT,
    ObjectType VARCHAR(20),
    [Type] VARCHAR(20),
    [Object] VARCHAR(20),
    DisplayOrder INT,

    CONSTRAINT Fk_ArticleTableID_References
        FOREIGN KEY (ArticleTableID)
        REFERENCES Articles(ArticleTableID)
        ON DELETE CASCADE
);