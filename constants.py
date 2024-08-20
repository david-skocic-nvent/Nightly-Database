ARTICLES_FILEPATH = "F:\\P360Data\\Archive\\catalogdata-articles.xml"
PRODUCT2GS_FILEPATH = "F:\\P360Data\\Archive\\catalogdata-product2gs.xml"
STRUCTURE_FEATURES_FILEPATH = "F:\\P360Data\\Archive\\catalogdata-structurefeatures.xml"
STRUCTURE_GROUPS_FILEPATH = "F:\\P360Data\\Archive\\catalogdata-structuregroups.xml"
UNITS_FILEPATH = "F:\\P360Data\\Archive\\catalogdata-units.xml"
TEMP_CSV_FILEPATH = "F:\\P360Data\\Archive\\temp.csv"





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
ATRICLE_STRUCTURE_GROUPS_COLUMNS = ['ArticleIdentifier', 'StructureGroup', 'Structure']
ARTICLE_REGIONS_COLUMNS = ['ArticleIdentifier', 'Region', 'MarketToPublic', 'ReferenceCode', 'StockCode']
ARTICLE_REGION_LIMIT_MARKETS_COLUMNS = ['ArticleIdentifier', 'Region', 'Market']
ARTICLE_PRODUCT_LINES_COLUMNS = ['ArticleIdentifier', 'ProductLine', 'ProductLineTag', 'LabelEnglish']
ARTICLE_APPLICATIONS_COLUMNS = ['ArticleIdentifier', 'Application', 'ApplicationTag', 'LabelEnglish']
ARTICLE_ASSETS_COLUMNS = ['ArticleIdentifier', 'AssetId', 'AssetType', 'Sequence']
ARTICLE_LANGS_COLUMNS = ['ArticleIdentifier', 'DescriptionSystem', 'DescriptionShort', 'Language']
ARTICLE_ATTRIBUTES_COLUMNS = ['ArticleIdentifier', 'NameInKeyLanguage', 'CombinedValue', 'CombinedValueWithUnit', 'SortValue', 'Value']
ARTICLE_ATTRIBUTE_VALUES_COLUMNS = ['ArticleIdentifier', 'AttributeNameInKeyLanguage', 'Identifier', 'Language', 'Value']
ARTICLE_SALES_COLUMNS = ['ArticleIdentifier', 'Customer']
ATRICLE_SALE_PRICE_GROUP_IDS_COLUMNS = ['ArticleIdentifier', 'SalesCustomer', 'Identifier', 'Code']
ARTICLE_REFERENCES_COLUMNS = ['ArticleIdentifier', 'Object', 'ObjectType', 'Type', 'DisplayOrder']

# Structure Features
STRUCTURE_FEATURES_COLUMNS = ['Identifier', 'StructureReference', 'Modified', 'NameInKeyLanguage', 'DataType', 'Purpose', 'Unit', 'Annotation']
STRUCTURE_FEATURE_LANGS_COLUMNS = ['StructureFeatureIdentifier', 'Language', 'Description']
STRUCTURE_FEATURE_PRESET_VALUES_COLUMNS = ['StructureFeatureIdentifier', 'StructureValueProxy', 'Identifier', 'DisplayOrder', 'AssetId']

# Products


'''
Mappings for each table
Maps the actual table name from the sql database to the columns and the name that is generated by parse_xml
This is nice because you can iterate over writing to csv and inserting into the database with just one loop
'''

table_maps = {
    # Units
    "Units": {
        "columns": UNITS_COLUMNS,
        "tableNameInCode": "Unit>fields"
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

}