from unzip_and_move import archive_and_clear_temp, unzip_to_temp
from parse_xml import *

different_files = ['articles', 'units', 'structuregroups', 'structurefeatures', 'products']
brands = ['caddy', 'erico']
tables_list = []
for b in brands:
    unzip_to_temp(b)
    for f in different_files:
        tables_list.append(get_xml_tables(f))

keysets:list[set] = []
for tables in tables_list:
    keysets.append(set(tables.keys()))

print("\n\ndifference::")
print(keysets[0].difference(keysets[1]))
print(keysets[1].difference(keysets[0]))
'''
for caddy_tables, erico_tables in zip(*tables_list):
    for table in caddy_tables:
        if table not in erico_tables:
            print("MISSING A TABLE-------------\n\n")
        else:
            varchar_len_caddy = get_varchar_lengths(caddy_tables[table])
            varchar_len_erico = get_varchar_lengths(erico_tables[table])
            for table_len in varchar_len_caddy:
                if table_len not in varchar_len_erico:
                    print(f"MISSING COLUMN {table_len} IN TABLE")
                else:
                    
                print("\t" + str(get_varchar_lengths(tables[table])))
'''