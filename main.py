from unzip_and_move import archive_and_clear_temp, unzip_to_temp
from parse_xml import *

unzip_to_temp('erico')
tables = get_xml_tables('articles')
for table in tables:
    print(table)
    print("\t" + str(get_varchar_lengths(tables[table])))