import pyodbc
from general_queries import *

def add_structure_group_metadata_row(connection, metadatadict):
    add_metadata_row(connection=connection, tablename="Structure_Group_Metadata", metadatadict=metadatadict)

def add_structure_group(connection, sg):
    try:
        # Create a cursor from the connection
        cursor = connection.cursor()

        sql = f'''
        INSERT INTO Structure_Groups (Identifier, Facet, NodeType, ShowProducts, FacetSequence, Brand, DisplayOrder, Level, ChartSort, 
        ChartStyle, ChartPackingQuantity, StructureReference, Modified, MasterStatus, ParentIdentifier, RestrictUnits)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''

        identifier = get_or_null(sg, ["identifier"])
        facet = get_or_null(sg, ["facet"])
        node_type = get_or_null(sg, ["NodeType"])
        show_products = get_or_null(sg, ["ShowProducts"])
        facet_sequence = get_or_null(sg, ["FacetSequence"])
        brand = get_or_null(sg, ["Brand"])
        display_order = get_or_null(sg, ["identifier"])
        level = get_or_null(sg, ["identifier"])
        chart_sort = get_or_null(sg, ["identifier"])
        chart_style = get_or_null(sg, ["identifier"])
        chart_packing_quantity = get_or_null(sg, ["ChartPackingQuantity"])
        structure_reference = get_or_null(sg, ["structureReference"])
        modified = get_or_null(sg, ['Modified'])
        master_status = get_or_null(sg, ["MasterStatus"])
        parent_identifier = get_or_null(sg, ["ParentIdentifier"])
        restrict_units = get_or_null(sg, ["RestrictUnits"])

        
        if modified is not None:
            modified = modified.replace('T', ' ')
        data = (identifier, facet, node_type, show_products, facet_sequence, brand, display_order, level, chart_sort, chart_style,\
                chart_packing_quantity, structure_reference, modified, master_status, parent_identifier, restrict_units)
        print(data)

        cursor.execute(sql, data)
        cursor.commit()
    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()