import csv
import pyodbc
from constants import *
from parse_xml import get_xml_tables
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
structure_group_tables = get_xml_tables("structuregroups")
print("dumping data to temporary csv file for bulk insertion")
with open("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\temp.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=STRUCTURE_GROUPS_COLUMNS)
    writer.writerows(structure_group_tables["StructureGroup>fields"])

#print("inserting data into database...")
#bulk_insert("Structure_Groups", STRUCTURE_GROUPS_COLUMNS, sg_data_list)
#bulk_insert("Structure_Group_Assets", STRUCTURE_GROUP_ASSETS_COLUMNS, sg_asset_data_list)
#print("Operation Complete")