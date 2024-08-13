import pyodbc

server = 'localhost'
database = 'DW_P360'
username = 'A2023355'
password = 'Gymboy21859'

# Create a connection string
connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Connect to the SQL Server
try:
    connection = pyodbc.connect(connection_string)
    print("Connected to SQL Server")

    # Create a cursor from the connection
    '''cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM YourTableName")

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)'''

except pyodbc.Error as e:
    print("Error occurred:", e)

#finally:
    # Close the cursor and connection
'''    if cursor:
        cursor.close()
    if connection:
        connection.close()'''