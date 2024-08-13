import pyodbc
from parse_xml import get_xml_dict 
from general_queries import *
from unit_queries import *


server = 'localhost'
database = 'DW_P360'

# Create a connection string
connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

# Connect to the SQL Server
try:
    connection = pyodbc.connect(connection_string)
    print("Connected to SQL Server")
    #units_meta_dict = get_xml_dict("units")["Meta"]
    #add_metadata_row("Unit_Metadata", units_meta_dict)

    for unit_dict in get_xml_dict("units")["Units"]["Unit"]:
        add_unit_row(unit_dict)

except pyodbc.Error as e:
    print("Error occurred:", e)

finally:
    if connection:
        connection.close()