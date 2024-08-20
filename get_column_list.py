"""
This file is meant to be a simple script where you just input a sql file, it reads it, then spits out a list of column names
I have based this on the format I used in the constants.py file
"""

filename = "SQL Queries\\ArticlesTables.sql"

with open(filename, newline='') as f:
    in_create_table = False
    table_data = {}
    current_table_name = ''
    for line in f:
        print(line,end='')
        if "CREATE TABLE" in line.upper():
            in_create_table = True
            current_table_name = line.split()[2]
            if '(' in current_table_name:
                current_table_name = current_table_name[:-1]
            table_data[current_table_name] = []
        if ';' in line:
            in_create_table = False
        if in_create_table and "CREATE TABLE" not in line.upper():
            if not line.isspace():
                words = line.split()
                if '[' in words[0]:
                    table_data[current_table_name].append(words[0][1:-1])
    print()
    for table in table_data:
        print(f"{table.upper()}_COLUMNS = {table_data[table]}")