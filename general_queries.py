import pyodbc

def add_metadata_row(connection, tablename, metadatadict):
    try:
        # Create a cursor from the connection
        cursor = connection.cursor()

        sql = f'''
        INSERT INTO {tablename} (Type, Version, Mode, StartTime, TimeCity, Environment)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        startTime = metadatadict['StartTime']
        startTime = startTime.replace('T', ' ')
        data = (metadatadict['Type'],metadatadict['Version'], metadatadict['Mode'], startTime, metadatadict['TimeCity'], metadatadict['Environment'])
        print(data)

        cursor.execute(sql, data)
        cursor.commit()
    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()


# Function to not throw an error if you refence something that is not in a dictionaryu and instead just returns None
def get_or_null (dictionary, index_list):
    for index in index_list:
        if index not in dictionary:
            return None
        else:
            dictionary = dictionary[index]
    return dictionary