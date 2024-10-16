import csv
import pyodbc
from constants import *

connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    'SERVER=localhost;'
    'DATABASE=DW_P360;'
    'Trusted_Connection=yes;'
)

'''
Function to bulk insert data from a table in dictionary form to a table in SQL Server
It does this by using a temporary file to output the dictionary as a CSV, then loading
the CSV into SQL Server.

This is more risky to use than regular insert statements, but much easier. If a small number
of lines in the CSV can't be inserted for some reason, it will stop the rest and lots of data
can be left missing.
'''
def bulk_insert(table, table_name):

    try:
        print(f"dumping {table_name} data to temporary csv file for bulk insertion")
        with open(TEMP_CSV_FILEPATH, "w", newline='',encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=TABLE_MAPS[table_name]["columns"])
            writer.writerows(table)
        print(f"{GREEN}Data successfully dumped{RESET}")
    except Exception as e:
        print(f"{RED}failed while dumping {table_name} to {TEMP_CSV_FILEPATH}{RESET}", e)
        print()
        return
    
    try:
        print(f"Trying to insert data from {TEMP_CSV_FILEPATH} to database")
        print("Connecting to Database...")

        connection = pyodbc.connect(connection_string)
        connection.autocommit = True
        cursor = connection.cursor()

        print(f"Executing a bulk insert into {table_name} from {TEMP_CSV_FILEPATH}...")

        cursor.execute(f"""
        BULK INSERT {table_name}
        FROM '{TEMP_CSV_FILEPATH}'
        WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\\n', FIRSTROW = 1, FORMAT = 'CSV')
        """)

        print(f"{GREEN}Bulk Insert successful{RESET}. {table_name} has been filled with data\n")

    except pyodbc.Error as e:
        print(f"{RED}Error occurred:{RESET}", e)
        print()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

'''
Function to insert a single line of data into table in SQL Server
This function worked at some point, but I haven't worked with it in 
a while so it probably needs some work to use it correctly again

In theory you could just insert the new data and update things that changed
instead of wiping the DB every time
'''
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
        print(f"{RED}Error occurred:{RESET}", e)
        print()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

'''
Capitalize the first letter of a string.
'''
def capitalize(s):
    return s[0].upper() + s[1:]