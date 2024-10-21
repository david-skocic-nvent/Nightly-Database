DATA_DUMP_FOLDER = "F:\\P360Data\\NightlyP360Data"
#TEMP_DATA_FOLDER = "F:\\P360Data\\temp"
TEMP_DATA_FOLDER = "C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\temp"
DATA_ARCHIVE_FOLDER = "F:\\P360Data\\Archive"
ARTICLES_FILEPATH = TEMP_DATA_FOLDER +"\\catalogdata-articles.xml"
PRODUCT2GS_FILEPATH = TEMP_DATA_FOLDER +"\\catalogdata-product2gs.xml"
STRUCTURE_FEATURES_FILEPATH = TEMP_DATA_FOLDER + "\\catalogdata-structurefeatures.xml"
STRUCTURE_GROUPS_FILEPATH = TEMP_DATA_FOLDER + "\\catalogdata-structuregroups.xml"
UNITS_FILEPATH = TEMP_DATA_FOLDER + "\\catalogdata-units.xml"
TEMP_CSV_FILEPATH = TEMP_DATA_FOLDER + "\\temp.csv"

FILES_IN_ZIP = ['Articles', 'Units', 'StructureGroups', 'StructureFeatures', 'Products']
LIST_NAMES_IN_CODE = ['Article', 'Unit', 'StructureGroup', 'StructureFeature', 'Product2G']
BRANDS_WITH_FILES = ['caddy', 'erico', 'eriflex']

PRIMARY_KEYS = {
    "Articles": "Identifier",
    "Units": "Code",
    "StructureGroups": "Identifier",
    "StructureFeatures": "Identifier",
    "Products": "Identifier",
}

# ANSI escape codes
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


'''
field names for each table are listed below
these are almost the same as the table columns, except these match what comes from the xml
which does not follow any standard naming convention (some are capitalized others are not)
these are used by the csv dictwriter to write tables to a csv file for bulk insertion
'''
# Units columns
UNITS_COLUMNS = ["Code", "BaseUnitFactor", "MeasurementSystem", "BaseUnit", "Modified"]
UNIT_LANGS_COLUMNS = ["UnitCode", "Language", "Symbol", "Name"]

# Structure group columns
STRUCTURE_GROUPS_COLUMNS = ["Identifier","StructureReference","Modified","DisplayOrder","NodeType","Level","MasterStatus","ShowProducts","ParentIdentifier","Brand","ChartSort", "ChartPackingQuantity","ChartStyle","RestrictUnits"]
STRUCTURE_GROUP_ATTRIBUTES_COLUMNS = ["StructureGroupIdentifier","NameInKeyLanguage","DisplayOrder","Unit","FacetType", "ShowFractions", "ChartDisplay", "ShowDecimals"]
STRUCTURE_GROUP_ATTRIBUTE_PRESET_VALUES_COLUMNS = ["Identifier","StructureGroupIdentifier","AttributeNameInKeyLanguage","StructureValueProxy","DisplayOrder"]
STRUCTURE_GROUP_ATTRIBUTE_VALUES_COLUMNS = ["Identifier","StructureGroupIdentifier","AttributeNameInKeyLanguage","Value","Language"]
STRUCTURE_GROUP_LANGS_COLUMNS = ["StructureGroupIdentifier", "Language","LanguageStatus", "Name", "Abstract", "Content"]
STRUCTURE_GROUP_NARRATIVES_COLUMNS = ["StructureGroupIdentifier", "Language", "Narrative", "Sequence"]
STRUCTURE_GROUP_BULLETS_COLUMNS = ["StructureGroupIdentifier", "Language", "Bullet", "Sequence"]
STRUCTURE_GROUP_ASSETS_COLUMNS = ["StructureGroupIdentifier", "AssetId", "Sequence", "AssetType"]
STRUCTURE_GROUP_FACETS_COLUMNS = ["StructureGroupIdentifier", "Facet", "Sequence"]

# Articles columns
ARTICLES_COLUMNS = ['Identifier', 'Modified', 'SupplierAltAID', 'ProductAssignment', 'Gtin', 'MarketToPublic', 'OrderUnit', 'ContentUnit', 'NoCUperOU', 'QuantityInterval', 'PrimaryStructureGroupMasterStatus', 'RealEAN', 'Step']
ARTICLE_STRUCTURE_GROUPS_COLUMNS = ['ArticleIdentifier', 'StructureGroup', 'Structure']
ARTICLE_REGIONS_COLUMNS = ['ArticleIdentifier', 'Region', 'MarketToPublic', 'ReferenceCode', 'StockCode']
ARTICLE_REGION_LIMIT_MARKETS_COLUMNS = ['ArticleIdentifier', 'Region', 'Market']
ARTICLE_PRODUCT_LINES_COLUMNS = ['ArticleIdentifier', 'ProductLine', 'ProductLineTag', 'LabelEnglish']
ARTICLE_APPLICATIONS_COLUMNS = ['ArticleIdentifier', 'Application', 'ApplicationTag', 'LabelEnglish']
ARTICLE_ASSETS_COLUMNS = ['ArticleIdentifier', 'AssetId', 'AssetType', 'Sequence']
ARTICLE_LANGS_COLUMNS = ['ArticleIdentifier', 'DescriptionSystem', 'DescriptionShort', 'Language']
ARTICLE_ATTRIBUTES_COLUMNS = ['ArticleIdentifier', 'NameInKeyLanguage', 'CombinedValue', 'CombinedValueWithUnit', 'SortValue']
ARTICLE_ATTRIBUTE_VALUES_COLUMNS = ['ArticleIdentifier', 'AttributeNameInKeyLanguage', 'Identifier', 'Language', 'Value']
ARTICLE_SALES_COLUMNS = ['ArticleIdentifier', 'Customer']
ARTICLE_SALE_PRICE_GROUP_IDS_COLUMNS = ['ArticleIdentifier', 'SalesCustomer', 'Identifier', 'Code']
ARTICLE_REFERENCES_COLUMNS = ['ArticleIdentifier', 'Object', 'ObjectType', 'Type', 'DisplayOrder']

# Structure Features
STRUCTURE_FEATURES_COLUMNS = ['Identifier', 'StructureReference', 'Modified', 'NameInKeyLanguage', 'Datatype', 'Purpose', 'Unit', 'Annotation']
STRUCTURE_FEATURE_LANGS_COLUMNS = ['StructureFeatureIdentifier', 'Language', 'Description']
STRUCTURE_FEATURE_PRESET_VALUES_COLUMNS = ['StructureFeatureIdentifier', 'StructureValueProxy', 'Identifier', 'DisplayOrder', 'AssetId', 'Description']

# Products
PRODUCT2GS_COLUMNS = ['Identifier', 'Modified', 'MarketToPublic', 'PrimaryStructureGroupMasterStatus', 'DisplayOrder']
PRODUCT2G_STRUCTURE_GROUPS_COLUMNS = ['ProductIdentifier', 'Structure', 'StructureGroup']
PRODUCT2G_REGIONS_COLUMNS = ['ProductIdentifier', 'Region', 'MarketToPublic']
PRODUCT2G_PRODUCT_LINES_COLUMNS = ['ProductIdentifier', 'ProductLine', 'ProductLineTag', 'LabelEnglish']
PRODUCT2G_APPLICATIONS_COLUMNS = ['ProductIdentifier', 'Application', 'ApplicationTag', 'LabelEnglish']
PRODUCT2G_ASSETS_COLUMNS = ['ProductIdentifier', 'AssetType', 'Sequence', 'AssetId']
PRODUCT2G_LANGS_COLUMNS = ['ProductIdentifier', 'Language', 'DescriptionShort', 'Abstract', 'Keyword']
PRODUCT2G_NARRATIVES_COLUMNS = ['ProductIdentifier', 'Language', 'Sequence', 'Narrative']
PRODUCT2G_BULLETS_COLUMNS = ['ProductIdentifier', 'Language', 'Sequence', 'Bullet']
PRODUCT2G_FOOTNOTES_COLUMNS = ['ProductIdentifier', 'Language', 'Sequence', 'Footnote']
PRODUCT2G_REFERENCES_COLUMNS = ['ProductIdentifier', 'Object', 'ObjectType', 'Type', 'DisplayOrder']
PRODUCT2G_REGION_LIMIT_MARKETS_COLUMNS = ['ProductIdentifier', 'Region', 'Market']

'''
Mappings for each table
Maps the actual table name from the sql database to the columns and the name that is generated by parse_xml
This is nice because you can iterate over writing to csv and inserting into the database with just one loop
'''

TABLE_MAPS = {
    # Units
    "Units": {
        "columns": UNITS_COLUMNS,
        "tableNameInCode": "Unit>fields",
        "primaryKey": "Code",
    },
    "Unit_Langs": {
        "columns": UNIT_LANGS_COLUMNS,
        "tableNameInCode": "Unit>Langs>Lang>fields"
    },

    # Structure Groups
    "Structure_Groups": {
        "columns": STRUCTURE_GROUPS_COLUMNS,
        "tableNameInCode": "StructureGroup>fields"
    },
    "Structure_Group_Attributes": {
        "columns": STRUCTURE_GROUP_ATTRIBUTES_COLUMNS,
        "tableNameInCode": "StructureGroup>Attributes>Attribute>fields"
    },
    "Structure_Group_Attribute_Preset_Values": {
        "columns": STRUCTURE_GROUP_ATTRIBUTE_PRESET_VALUES_COLUMNS,
        "tableNameInCode": "StructureGroup>Attributes>Attribute>PresetValues>PresetValue>fields"
    },
    "Structure_Group_Attribute_Values": {
        "columns": STRUCTURE_GROUP_ATTRIBUTE_VALUES_COLUMNS,
        "tableNameInCode": "StructureGroup>Attributes>Attribute>Values>Value>fields"
    },
    "Structure_Group_Langs": {
        "columns": STRUCTURE_GROUP_LANGS_COLUMNS,
        "tableNameInCode": "StructureGroup>Langs>Lang>fields"
    },
    "Structure_Group_Narratives": {
        "columns": STRUCTURE_GROUP_NARRATIVES_COLUMNS,
        "tableNameInCode": "StructureGroup>Narratives>Narrative>fields"
    },
    "Structure_Group_Bullets": {
        "columns": STRUCTURE_GROUP_BULLETS_COLUMNS,
        "tableNameInCode": "StructureGroup>Bullets>Bullet>fields"
    },
    "Structure_Group_Assets": {
        "columns": STRUCTURE_GROUP_ASSETS_COLUMNS,
        "tableNameInCode": "StructureGroup>Assets>Asset>fields"
    },
    "Structure_Group_Facets": {
        "columns": STRUCTURE_GROUP_FACETS_COLUMNS,
        "tableNameInCode": "StructureGroup>Facets>Facet>fields"
    },

    # Articles
    "Articles": {
        "columns": ARTICLES_COLUMNS,
        "tableNameInCode": "Article>fields"
    },
    "Article_Structure_Groups": {
        "columns": ARTICLE_STRUCTURE_GROUPS_COLUMNS,
        "tableNameInCode": "Article>StructureGroup>fields"
    },
    "Article_Regions": {
        "columns": ARTICLE_REGIONS_COLUMNS,
        "tableNameInCode": "Article>Regions>Region>fields"
    },
    "Article_Product_Lines": {
        "columns": ARTICLE_PRODUCT_LINES_COLUMNS,
        "tableNameInCode": "Article>ProductLines>ProductLine>fields"
    },
    "Article_Applications": {
        "columns": ARTICLE_APPLICATIONS_COLUMNS,
        "tableNameInCode": "Article>Applications>Application>fields"
    },
    "Article_Assets": {
        "columns": ARTICLE_ASSETS_COLUMNS,
        "tableNameInCode": "Article>Assets>Asset>fields"
    },
    "Article_Langs": {
        "columns": ARTICLE_LANGS_COLUMNS,
        "tableNameInCode": "Article>Langs>Lang>fields"
    },
    "Article_Attributes": {
        "columns": ARTICLE_ATTRIBUTES_COLUMNS,
        "tableNameInCode": "Article>Attributes>Attribute>fields"
    },
    "Article_Attribute_Values": {
        "columns": ARTICLE_ATTRIBUTE_VALUES_COLUMNS,
        "tableNameInCode": "Article>Attributes>Attribute>Values>Value>fields"
    },
    "Article_Sales": {
        "columns": ARTICLE_SALES_COLUMNS,
        "tableNameInCode": "Article>Sales>Sales>fields"
    },
    "Article_Sale_Price_Group_Ids": {
        "columns": ARTICLE_SALE_PRICE_GROUP_IDS_COLUMNS,
        "tableNameInCode": "Article>Sales>Sales>PriceGroupId>fields"
    },
    "Article_References": {
        "columns": ARTICLE_REFERENCES_COLUMNS,
        "tableNameInCode": "Article>References>Reference>fields"
    },
    "Article_Region_Limit_Markets": {
        "columns": ARTICLE_REGION_LIMIT_MARKETS_COLUMNS,
        "tableNameInCode": "Article>Regions>Region>LimitMarket>Market>fields"
    },

    #Structure Features
    "Structure_Features": {
        "columns": STRUCTURE_FEATURES_COLUMNS,
        "tableNameInCode": "StructureFeature>fields"
    },
    "Structure_Feature_Langs": {
        "columns": STRUCTURE_FEATURE_LANGS_COLUMNS,
        "tableNameInCode": "StructureFeature>Langs>Lang>fields"
    },
    "Structure_Feature_Preset_Values": {
        "columns": STRUCTURE_FEATURE_PRESET_VALUES_COLUMNS,
        "tableNameInCode": "StructureFeature>PresetValues>PresetValue>fields"
    },

    #Products
    "Product2Gs" : {
        "columns": PRODUCT2GS_COLUMNS,
        "tableNameInCode": "Product2G>fields"
    },
    "Product2G_Structure_Groups" : {
        "columns": PRODUCT2G_STRUCTURE_GROUPS_COLUMNS,
        "tableNameInCode": "Product2G>StructureGroup>fields"
    },
    "Product2G_Regions" : {
        "columns": PRODUCT2G_REGIONS_COLUMNS,
        "tableNameInCode": "Product2G>Regions>Region>fields"
    },
    "Product2G_Product_Lines" : {
        "columns": PRODUCT2G_PRODUCT_LINES_COLUMNS,
        "tableNameInCode": "Product2G>ProductLines>ProductLine>fields"
    },
    "Product2G_Applications" : {
        "columns": PRODUCT2G_APPLICATIONS_COLUMNS,
        "tableNameInCode": "Product2G>Applications>Application>fields"
    },
    "Product2G_Assets" : {
        "columns": PRODUCT2G_ASSETS_COLUMNS,
        "tableNameInCode": "Product2G>Assets>Asset>fields"
    },
    "Product2G_Langs" : {
        "columns": PRODUCT2G_LANGS_COLUMNS,
        "tableNameInCode": "Product2G>Langs>Lang>fields"
    },
    "Product2G_Narratives" : {
        "columns": PRODUCT2G_NARRATIVES_COLUMNS,
        "tableNameInCode": "Product2G>Narratives>Narrative>fields"
    },
    "Product2G_Bullets" : {
        "columns": PRODUCT2G_BULLETS_COLUMNS,
        "tableNameInCode": "Product2G>Bullets>Bullet>fields"
    },
    "Product2G_Footnotes" : {
        "columns": PRODUCT2G_FOOTNOTES_COLUMNS,
        "tableNameInCode": "Product2G>Footnotes>Footnote>fields"
    },
    "Product2G_References" : {
        "columns": PRODUCT2G_REFERENCES_COLUMNS,
        "tableNameInCode": "Product2G>References>Reference>fields"
    },
    "Product2G_Region_Limit_Markets" : {
        "columns": PRODUCT2G_REGION_LIMIT_MARKETS_COLUMNS,
        "tableNameInCode": "Product2G>Regions>Region>LimitMarket>fields"
    },

    # StructureFeatures

}