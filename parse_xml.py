import xml.etree.ElementTree as et
from constants import *



def tagstring(uglytag):
    return uglytag[uglytag.index('}') + 1:]

def recursive_fill_visual (parent, parent_dict):
    if len(parent.attrib) > 0:
        for attrib in parent.attrib:
            parent_dict[attrib] = parent.attrib[attrib]
    if len(parent) > 0:
        for element in parent:
            tgstr = tagstring(element.tag)
            if element.text is not None and not element.text.isspace():
                parent_dict[tgstr] = element.text
                continue
            if tgstr in parent_dict:
                if isinstance(parent_dict[tgstr], dict):
                    tempdict = parent_dict[tgstr]
                    parent_dict[tgstr] = []
                    parent_dict[tgstr].append(tempdict)
                parent_dict[tgstr].append({})
                recursive_fill_visual(element, parent_dict[tgstr][-1])
            else:
                parent_dict[tgstr] = {}
                recursive_fill_visual(element, parent_dict[tgstr])

    if parent.text is not None and not parent.text.isspace():
        parent_dict["text"] = parent.text

def recursive_fill_lists (parent, parent_dict):
    if len(parent.attrib) > 0:
        for attrib in parent.attrib:
            parent_dict[attrib] = parent.attrib[attrib]
    if len(parent) > 0:
        for element in parent:
            tgstr = tagstring(element.tag)
            if element.text is not None and not element.text.isspace():
                parent_dict[tgstr] = element.text
                continue
            elif tgstr not in parent_dict:
                parent_dict[tgstr] = []
            parent_dict[tgstr].append({})
            recursive_fill_lists(element, parent_dict[tgstr][-1])

def recursivePrint(print_dict, tabcount=0):
    for item in print_dict:
        if isinstance(print_dict[item], dict):
            for _ in range(tabcount):
                print('  ', end='')
            print(f"{item}:")
            recursivePrint(print_dict[item], tabcount + 1)
        elif isinstance(print_dict[item], list):
            for i, el in enumerate(print_dict[item]):
                for _ in range(tabcount):
                    print('  ', end='')
                print(f"{item}[{i}]:")
                recursivePrint(el, tabcount + 1)
        else:
            for _ in range(tabcount):
                print('  ', end='')
            print(f"{item}: {print_dict[item]}")

def createSchema(root):
    mycolumns = {}
    mycolumns["safe"] = set()
    mycolumns["variable"] = {}
    for child in root:
        if isinstance(root[child], list):
            if child not in mycolumns["variable"]:
                mycolumns["variable"][child] = {}
            for childdict in root[child]:
                tempdict = createSchema(childdict)
                if "variable" not in mycolumns["variable"][child]:
                    mycolumns["variable"][child]["variable"] = {}
                for key in tempdict["variable"]:
                    mycolumns["variable"][child]["variable"][key] = tempdict["variable"][key]
            for childdict in root[child]:
                tempdict = createSchema(childdict)
                if "safe" not in mycolumns["variable"][child]:
                    mycolumns["variable"][child]["safe"] = set()
                for key in tempdict["safe"]:
                    try:
                        if key[0:key.index(">")] not in mycolumns["variable"][child]["variable"]:
                            mycolumns["variable"][child]["safe"].add(key)
                    except ValueError:
                        if key not in mycolumns["variable"][child]["variable"]:
                            mycolumns["variable"][child]["safe"].add(key)

    for child in root:
        if child not in mycolumns["variable"]:
            if isinstance(root[child], dict):
                tempdict = createSchema(root[child])
                for key in tempdict["safe"]:
                    mycolumns["safe"].add(child+">"+key)
                for key in tempdict["variable"]:
                    mycolumns["variable"][child] = tempdict["variable"][key]
            else:
                mycolumns["safe"].add(child)
                #print(createSchema(childdict))
    return mycolumns
                
'''
Function to Create a dictionary where the keys are tables in the sql database and the values are the contents of the table.
The value is a list of dictionaries, each dictionary is a single row and has column names as keys and column values as vales 
'''
def collapse_hierarchy(rootdict):
    ret_dict = {}
    for field in rootdict:
        if isinstance(rootdict[field], list):
            for child in rootdict[field]:
                tempdict = collapse_hierarchy(child)
                for child_field in tempdict:
                    key = field + ">" + child_field
                    if key not in ret_dict:
                        ret_dict[key] = []
                    if isinstance(tempdict[child_field], list):
                        ret_dict[key] += tempdict[child_field]
                    else:
                        ret_dict[key].append(tempdict[child_field])
        else:
            if "fields" not in ret_dict:
                ret_dict["fields"] = {}
            ret_dict["fields"][field] = rootdict[field]
    return ret_dict

def write_create_table(tablename, fields):
    retstr = ""
    retstr += "CREATE TABLE " + tablename + " (\n"
    for field in fields:
        if fields[field] > 0:
            retstr += f"\t[{field}] VARCHAR({fields[field]}),\n"
        else:
            retstr += f"\t[{field}] ,\n"
    retstr += ");"
    return retstr

'''
Function that returns all the contents of a table based on the xml file that is passed in. This is used by the controller to get data
'''
def get_xml_tables(whichFile):
    rootdict = {}
    match whichFile.lower():
        case 'units':
            print("parsing units xml...")
            tree = et.parse(UNITS_FILEPATH)
            root = tree.getroot()
            recursive_fill_lists(root["Units"][0], rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["Units"][0])
            
        case 'structuregroups':
            print("parsing structure groups xml...")
            tree = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-structuregroups.xml")#STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
            recursive_fill_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["StructureGroups"][0])
    
    return collapsed

if __name__ == '__main__':

    sgroot = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-structuregroups.xml").getroot()
    rootdict = {}

    #recursiveFill(sgroot, rootdict)
    recursive_fill_lists(sgroot, rootdict)
    collapsed = collapse_hierarchy(rootdict["StructureGroups"][0])
    
    queries = []

    for table in collapsed:
        fields = {}
        print(table)
        for row in collapsed[table]:
            for key in row:
                if key not in fields:
                    fields[key] = 0
                try:
                    row[key] = int(row[key])
                except:
                    pass
                    
                    if fields[key] == 0:
                        if row[key].lower() == "true":
                            row[key] = True
                        elif row[key].lower() == "false":
                            row[key] = False
                
                if isinstance(row[key], str):
                    fields[key] = max(fields[key],len(row[key]))
                elif isinstance(row[key], int):
                    pass

        #print(fields)
        queries.append(write_create_table(table,fields))
    for query in queries:
        print(query)
    #recursivePrint(collapsed)

    #for i in range(10):
        #recursivePrint(rootdict["StructureGroups"][0]["StructureGroup"][i])
    

else:
    pass
    '''structure_group_tree = et.parse(STRUCTURE_GROUPS_FILEPATH)
    structure_group_root = structure_group_tree.getroot()

    units_tree = et.parse(UNITS_FILEPATH)
    units_root = units_tree.getroot()

    articles_tree = et.parse(ARTICLES_FILEPATH)
    articles_root = articles_tree.getroot()

    product2gs_tree = et.parse(PRODUCT2GS_FILEPATH)
    product2gs_root = product2gs_tree.getroot()

    structure_features_tree = et.parse(STRUCTURE_FEATURES_FILEPATH)
    structure_features_root = structure_features_tree.getroot()'''