from unzip_and_move import archive_and_clear_temp, unzip_to_temp
from parse_xml import *

different_files = ['articles', 'units', 'structuregroups', 'structurefeatures', 'products']
brands = ['caddy', 'erico']
for b in brands:
    unzip_to_temp(b)
    for f in different_files:
        tables = get_xml_tables(f)
        for table in tables:
            print(table)
            print("\t" + str(get_varchar_lengths(tables[table])))
