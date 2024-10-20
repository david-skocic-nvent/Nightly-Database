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
        
'''
Pass in two lists where each item in a list is a row in a table (a dict)
Puts all items from list2 into list1 that arent already there.
'''
def combine_lists(L1:list, L2:list):
    # for each dict in the second list
    for d in L2:
        if d not in L1:
            L1.append(d)



bulk_insert_data = {}
for content_type in FILES_IN_ZIP:
    bulk_insert_data[content_type] = {}

# Loop through every brand and add all data to tables here
for brand in BRANDS_WITH_FILES:

    # unzip the files for a brand to the temporary directory
    unzip_to_temp(brand)

    for content_type in FILES_IN_ZIP:
        data_to_add = get_table_dicts(content_type)
        combine_lists(bulk_insert_data[content_type[:-1]], data_to_add[content_type[:-1]])
        for k in bulk_insert_data:
            print(len(bulk_insert_data[k]))
    archive_and_clear_temp(brand)


'''
Loop through all the tables and bulk insert them. Loop through TABLE_MAPS 
instead of tables because it follows an order for primary keys and such
that is allowed
'''
for table_name_in_sql in TABLE_MAPS:
    table_name_in_code = TABLE_MAPS[table_name_in_sql]["tableNameInCode"]
    if table_name_in_code in bulk_insert_data:
        bulk_insert(bulk_insert_data[table_name_in_code], table_name_in_sql)

'''
NEW IDEA
instead of doing the bulk insert for an individual brand table, we do each brand table then pull the common ones to one single table (dict)
'''

