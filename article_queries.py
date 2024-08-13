import pyodbc
from general_queries import *

def add_article_metadata_row(connection, metadatadict):
    add_metadata_row(connection=connection, tablename="Article_Metadata", metadatadict=metadatadict)

def add_article(connection, article_dict):
    try:
        # Create a cursor from the connection
        cursor = connection.cursor()

        sql = f'''
        INSERT INTO Units (Code, BaseUnitFactor, MeasurementSystem, BaseUnit, Modified, Name, Language, Symbol)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        modified = get_or_null(unit_dict, ['Modified'])
        if modified is not None:
            modified = modified.replace('T', ' ')
        data = (get_or_null(unit_dict, ['code']), get_or_null(unit_dict,['BaseUnitFactor']), get_or_null(unit_dict,['MeasurementSystem']), get_or_null(unit_dict, ['BaseUnit']), modified,\
                get_or_null(unit_dict,['Langs','Lang','Name']), get_or_null(unit_dict, ['Langs','Lang','Language']), get_or_null(unit_dict, ['Langs','Lang','Symbol']))
        print(data)

        cursor.execute(sql, data)
        cursor.commit()
    except pyodbc.Error as e:
        print("Error occurred:", e)
    finally:
        if cursor:
            cursor.close()