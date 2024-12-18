'''
Controller for the whole program
'''
from unzip_and_move import archive_and_clear_temp, unzip_to_temp
from parse_xml import *
from constants import FILES_IN_ZIP, BRANDS_WITH_FILES, TABLE_MAPS
from queries import *
from Tee import Tee
import sys
import time

def find_table_name_in_maps(table_name_from_code):
    for table_map in TABLE_MAPS:
        if TABLE_MAPS[table_map]['tableNameInCode'] == table_name_from_code:
            return table_map
        
'''
Pass in two lists where each item in a list is a row in a table (a dict)
Puts all items from list2 into list1 that arent already there.
'''
def combine_lists(L1:list, L2:list, content_type):
    # for each dict in the second list
    for d in L2:
        if d[PRIMARY_KEYS[content_type]] not in primary_keys_in_bulk_insert_data[content_type]:
            L1.append(d)
            primary_keys_in_bulk_insert_data[content_type].add(d[PRIMARY_KEYS[content_type]])


print("Running.....")

# redirect print statements to a log file to debug later
#TODO rewrite so prints go to stdout and log file
logfile = open(LOG_FILEPATH,"w")

stdout = sys.stdout
sys.stdout = Tee(stdout, logfile)

primary_keys_in_bulk_insert_data = {}

bulk_insert_data = {}
for content_type, list_name in zip(FILES_IN_ZIP, LIST_NAMES_IN_CODE):
    bulk_insert_data[content_type] = {
        list_name:[]
    }
    primary_keys_in_bulk_insert_data[content_type] = set()



# Loop through every brand and add all data to tables here
for brand in BRANDS_WITH_FILES:

    # unzip the files for a brand to the temporary directory
    unzip_to_temp(brand)

    for content_type, list_name in zip(FILES_IN_ZIP, LIST_NAMES_IN_CODE):
        data_to_add = get_table_dicts(content_type)
        print(f"Adding {brand} data to {content_type} list")
        rows_before_addition = len(bulk_insert_data[content_type][list_name])
        combine_lists(bulk_insert_data[content_type][list_name], data_to_add[list_name], content_type)
        rows_after_addition = len(bulk_insert_data[content_type][list_name])
        print(f"{rows_after_addition - rows_before_addition} rows added to {content_type} data")

    print("Clearing tempfile and archiving zip files...")
    archive_and_clear_temp(brand)

'''
clear all data from database by executing this script
TODO: write a script to drop all data without removing the tables themselves
'''
clear_database()


bulk_insert_tables = {}
for content_type in bulk_insert_data:
    bulk_insert_tables.update(collapse_hierarchy(bulk_insert_data[content_type]))

'''
Loop through all the tables and bulk insert them. Loop through TABLE_MAPS 
instead of tables because it follows an order for primary keys and such
that is allowed
'''
for table_name_in_sql in TABLE_MAPS:
    table_name_in_code = TABLE_MAPS[table_name_in_sql]["tableNameInCode"]
    if table_name_in_code in bulk_insert_tables:
        bulk_insert(bulk_insert_tables[table_name_in_code], table_name_in_sql)


sys.stdout = stdout
print("Complete")
time.sleep(3)