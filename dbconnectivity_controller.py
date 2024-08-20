import csv
import time
import pyodbc
from constants import *
from parse_xml import get_xml_tables
from general_queries import *
from unit_queries import *
from structure_group_queries import *


def bulk_insert(table_name):
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connected to Server to add to table {table_name}")
        connection.autocommit = True

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

def insert(table_name, data):
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connected to Server to add to table {table_name}")
        connection.autocommit = True

        cursor = connection.cursor()
        
        for i,row in enumerate(data):
            query = f"INSERT INTO {table_name}("
            column_vals = []
            for col in row:
                query += capitalize(col) + ','
                column_vals.append(row[col])
            query = query[:-1] + f") VALUES({'?,'*(len(column_vals)-1) + '?'})"
            cursor.execute(query, column_vals)
            if i % 1000 == 0:
                print(i)
                
    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def capitalize(s):
    return s[0].upper() + s[1:]

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
for map in table_maps:
    with open("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\temp.csv", "w", newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=table_maps[map]["columns"])
        writer.writerows(structure_group_tables[table_maps[map]["tableNameInCode"]])
    time.sleep(2)




#print("inserting data into database...")
#bulk_insert("Structure_Groups", STRUCTURE_GROUPS_COLUMNS, sg_data_list)
#bulk_insert("Structure_Group_Assets", STRUCTURE_GROUP_ASSETS_COLUMNS, sg_asset_data_list)
#print("Operation Complete")