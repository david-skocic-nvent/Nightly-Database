import csv
import pyodbc
from constants import *
from parse_xml import get_xml_dict 
from general_queries import *
from unit_queries import *
from structure_group_queries import *


def bulk_insert(table_name, table_headers, data):
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connected to Server to add to table {table_name}")
        connection.autocommit = True

        with open(TEMP_CSV_FILEPATH, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(table_headers)
            writer.writerows(data)

        cursor = connection.cursor()

        cursor.execute(f"""
        BULK INSERT {table_name}
        FROM '{TEMP_CSV_FILEPATH}'
        WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\\n', FIRSTROW = 2)
        """)

    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    'SERVER=localhost;'
    'DATABASE=DW_P360;'
    'Trusted_Connection=yes;'
)

# Connect to the SQL Server

#units_meta_dict = get_xml_dict("units")["Meta"]
#add_metadata_row("Unit_Metadata", units_meta_dict)

#for unit_dict in get_xml_dict("units")["Units"]["Unit"]:
#    add_unit_row(unit_dict)
print("parsing structure groups xml")
structure_group_dict = get_xml_dict("structuregroups")
print("pulling structure group data into tables")
sg_data_list = []
sg_asset_data_list = []
for structure_group in structure_group_dict["StructureGroups"]["StructureGroup"]:
    sg_data, asset_data = add_structure_group(structure_group)
    sg_data_list.append(sg_data)
    sg_asset_data_list += asset_data

print("inserting data into database...")
#bulk_insert("Structure_Groups", STRUCTURE_GROUPS_COLUMNS, sg_data_list)
bulk_insert("Structure_Group_Assets", STRUCTURE_GROUP_ASSETS_COLUMNS, sg_asset_data_list)
print("Operation Complete")