import pyodbc
from parse_xml import get_xml_dict 

server = 'localhost'
database = 'DW_P360'

def fill_metadata_table(whichtable, metadatadict):
    try:
        # Create a cursor from the connection
        cursor = connection.cursor()

        sql = f'''
        INSERT INTO {whichtable}_Metadata (Type, Version, Mode, StartTime, TimeCity, Environment)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        with metadatadict as m:
            startTime = m['StartTime']
            startTime = startTime.replace('T', ' ')
            data = (m['Type'],m['Version'], m['Mode'], startTime, m['TimeCity'], m['Environment'])
            print(data)

        #cursor.execute(sql, data)
        #cursor.commit()
    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()

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
    units_meta_dict = get_xml_dict("units")
    fill_metadata_table("Unit", units_meta_dict)

except pyodbc.Error as e:
    print("Error occurred:", e)

finally:
    if connection:
        connection.close()


