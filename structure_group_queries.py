import pyodbc
from general_queries import *

def add_structure_group_metadata_row(connection, metadatadict):
    add_metadata_row(connection=connection, tablename="Structure_Group_Metadata", metadatadict=metadatadict)

def add_structure_group(sg):
    try:

        # Get all the columns for the structuregroups table
        identifier = get_or_null(sg, ["identifier"])
        facet = get_or_null(sg, ["Facets", "Facet", "facet"])
        node_type = get_or_null(sg, ["NodeType"])
        show_products = get_or_null(sg, ["ShowProducts"])
        facet_sequence = get_or_null(sg, ["Facets", "Facet", "Sequence"])
        brand = get_or_null(sg, ["Brand"])
        display_order = get_or_null(sg, ["DisplayOrder"])
        level = get_or_null(sg, ["Level"])
        chart_sort = get_or_null(sg, ["ChartSort"])
        chart_style = get_or_null(sg, ["ChartStyle"])
        chart_packing_quantity = get_or_null(sg, ["ChartPackingQuantity"])
        structure_reference = get_or_null(sg, ["structureReference"])
        modified = get_or_null(sg, ['Modified'])
        if modified is not None:
            modified = modified.replace('T', ' ')
        master_status = get_or_null(sg, ["MasterStatus"])
        parent_identifier = get_or_null(sg, ["ParentIdentifier"])
        restrict_units = get_or_null(sg, ["RestrictUnits"])
        # put data into a tuple to return
        data = (identifier, facet, node_type, show_products, facet_sequence, brand, display_order, level, chart_sort, chart_style,\
        chart_packing_quantity, structure_reference, modified, master_status, parent_identifier, restrict_units)

        # get all the columns for assets for this structure group
        asset_data = []
        if "Assets" in sg:
            if isinstance(sg["Assets"]["Asset"], list):
                for asset in sg["Assets"]["Asset"]:
                    asset_id = get_or_null(asset, ["AssetId"])
                    asset_sequence = get_or_null(asset, ["sequence"])
                    asset_type = get_or_null(asset, ["assetType"])
                    asset_data.append((identifier, asset_id, asset_sequence, asset_type))
            else:
                asset = sg["Assets"]["Asset"]
                asset_id = get_or_null(asset, ["AssetId"])
                asset_sequence = get_or_null(asset, ["sequence"])
                asset_type = get_or_null(asset, ["assetType"])
                asset_data.append((identifier, asset_id, asset_sequence, asset_type))
        
        attributes_data = []
        if "Attributes" in sg:
            if isinstance(sg["Attributes"]["Attribute"], list):
                for attribute in sg["Attributes"]["Attribute"]:
                    display_order = get_or_null(attribute, ["DisplayOrder"])
                    name_in_key_language = get_or_null(attribute, ["nameInKeyLanguage"])
                    unit = get_or_null(attribute, ["Unit"])
                    facet_type = get_or_null(attribute, ["FacetType"])
                    chart_display = get_or_null(attribute, ["ChartDisplay"])
                    show_decimals = get_or_null(attribute, ["ShowDecimals"])
                    show_fractions = get_or_null(attribute, ["ShowFractions"])
                    if "PresetValues" in attribute:
                        

                     
        #print(data)

        #cursor.execute(sql, data)
        #cursor.commit()
        return data, asset_data
    except pyodbc.Error as e:
        print("Error occurred:", e)