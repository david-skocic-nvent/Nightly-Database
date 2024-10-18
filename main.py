'''
Controller for the whole program
'''
from unzip_and_move import archive_and_clear_temp, unzip_to_temp
from parse_xml import *
from constants import FILES_IN_ZIP, BRANDS_WITH_FILES, TABLE_MAPS
from insert_data import bulk_insert

def find_table_name_in_maps(table_name_from_code):
    for table_map in TABLE_MAPS:
        if TABLE_MAPS[table_map]['tableNameInCode'] == table_name_from_code:
            return table_map

tables = {}

# Loop through every brand and add all data to tables here
for brand in BRANDS_WITH_FILES:

    # unzip the files for a brand to the temporary directory
    unzip_to_temp(brand)

    # pull the xml files into tables (dictionaries) in code and save them to tables
    for file_data_group in FILES_IN_ZIP:
        new_tables = get_xml_tables(file_data_group)
        for table in new_tables:
            if table in tables:
                tables[table].update(new_tables[table])
            else:
                tables[table] = new_tables[table]
            

    archive_and_clear_temp(brand)


'''
Loop through all the tables and bulk insert them. Loop through TABLE_MAPS 
instead of tables because it follows an order for primary keys and such
that is allowed
'''
for table_name_in_sql in TABLE_MAPS:
    table_name_in_code = TABLE_MAPS[table_name_in_sql]["tableNameInCode"]
    if table_name_in_code in tables:
        bulk_insert(tables[table_name_in_code], table_name_in_sql)

'''
NEW IDEA
instead of doing the bulk insert for an individual brand table, we do each brand table then pull the common ones to one single table (dict)
'''

