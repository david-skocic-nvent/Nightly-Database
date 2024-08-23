import csv
import time
import pyodbc
from constants import *
from parse_xml import get_xml_tables



def bulk_insert(table_name):
    try:
        connection = pyodbc.connect(connection_string)
        print(f"Connected to Server to add to table {table_name}")
        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute(f"""
        BULK INSERT {table_name}
        FROM '{TEMP_CSV_FILEPATH}'
        WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\\n', FIRSTROW = 1, FORMAT = 'CSV')
        """)

        print(f"Bulk Insert successful. {table_name} has been filled with data\n")

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

# Function to not throw an error if you refence something that is not in a dictionaryu and instead just returns None
def get_or_null (dictionary, index_list):
    for index in index_list:
        if index not in dictionary:
            return None
        else:
            dictionary = dictionary[index]
    return dictionary

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
tables = get_xml_tables("structuregroups")
tables.update(get_xml_tables("articles"))
tables.update(get_xml_tables("products"))
tables.update(get_xml_tables("structurefeatures"))
tables.update(get_xml_tables("units"))

for i,table_name in enumerate(table_maps):
    print(f"dumping {table_name} data to temporary csv file for bulk insertion")
    with open(TEMP_CSV_FILEPATH, "w", newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=table_maps[table_name]["columns"])
        writer.writerows(tables[table_maps[table_name]["tableNameInCode"]])
    print("inserting data into database...")
    bulk_insert(table_name)
    #insert(table_name, tables[table_maps[table_name]["tableNameInCode"]])
    time.sleep(1)
    




#print("inserting data into database...")

#bulk_insert("Structure_Group_Assets", STRUCTURE_GROUP_ASSETS_COLUMNS, sg_asset_data_list)
#print("Operation Complete")
