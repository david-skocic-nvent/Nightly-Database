import xml.etree.ElementTree as et
from constants import *

# these foreign keys are a little hard to understand:
# basically all these foreign keys are for a tables that reference some parent table, or data from inside of the
# xml element table that at references (like if a structuregroup has 4 regions, these regions are in a regions table that references structuregroups)
# These keys are not meant for something that just references some other table that is not a parent to it (if an element has a units field that references 
# the units table for example). The keys in this dictionary are at the level in the recursion that you can find this information. For example, when the key is
# StructureGroup>fields, you are within a structuregroup object so you have access to all its fields including its identifier, hence the xml_field_name in the associated dict.
# In this case, every nested table (one that references the structuregroup table as a child, like regions from the previous example) needs to know the identifier for 
# structuregroups, so within each child table it copies the value from xml_field_name to column_name in the child table and now the child can reference the parent.
foreign_keys = {
    "StructureGroup>fields": {"xml_field_name": "Identifier", "column_name": "StructureGroupIdentifier"},
    "Attribute>fields": {"xml_field_name": "NameInKeyLanguage", "column_name": "AttributeNameInKeyLanguage"},
    "Unit>fields": {"xml_field_name": "Code", "column_name": "UnitCode"},
    "Region>fields": {"xml_field_name": "Region", "column_name": "Region"},
    "Article>fields": {"xml_field_name": "Identifier", "column_name": "ArticleIdentifier"},
    "StructureFeature>fields": {"xml_field_name": "Identifier", "column_name": "StructureFeatureIdentifier"},
}

def capitalize(s):
    return s[0].upper() + s[1:]

def tagstring(uglytag):
    return capitalize(uglytag[uglytag.index('}') + 1:])

def recursive_fill_visual (parent, parent_dict):
    if len(parent.attrib) > 0:
        for attrib in parent.attrib:
            parent_dict[capitalize(attrib)] = parent.attrib[attrib]
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
    global count
    if len(parent.attrib) > 0:
        for attrib in parent.attrib:
            parent_dict[capitalize(attrib)] = parent.attrib[attrib]
    if parent.text is not None and not parent.text.isspace():
        parent_dict["txt"] = parent.text
    if len(parent) > 0:
        for element in parent:
            tgstr = tagstring(element.tag)
            if tgstr not in parent_dict:
                parent_dict[tgstr] = []
            parent_dict[tgstr].append({})
            recursive_fill_lists (element, parent_dict[tgstr][-1])

'''
Due to the way recursive fill lists works to capture all the data, it must make a list of dicts that hold the data for just the text of an xml element
We must take lists that are of length 1 and collapse them down so they are just a single field, and if there is more than 1, itll make a list of children
the following two functions work together, because for a given tag, if ANY of the lists are longer than 1 then they all shouldnt be collapsed
These comments probably dont make any sense but this seems to work.
'''
# I am nervous that this function specifically will mark a key as something that should not be collapsable in one spot,
# but if there is the same (name) key in a different level of the hierarchy that should be collapsed, it wont
def find_tags_to_collapse(rootdict, tags_to_collapse):
    for key in rootdict:
        if isinstance(rootdict[key], list):
            for child in rootdict[key]:
                if "txt" in child:
                    if key not in tags_to_collapse:
                        tags_to_collapse[key] = True
                    if len(rootdict[key]) > 1:
                        tags_to_collapse[key] = False
                else:
                    find_tags_to_collapse(child, tags_to_collapse)
def collapse_txts(rootdict, tags_to_collapse):
    for key in rootdict:
        if isinstance(rootdict[key], list):
            for child in rootdict[key]:
                if "txt" in child:
                    if tags_to_collapse[key]:
                        rootdict[key] = child["txt"]
                    else:
                        child[key] = child.pop("txt")
                else:
                    collapse_txts(child, tags_to_collapse)

def fill_and_clean_lists(root, rootdict):
    recursive_fill_lists(root, rootdict)
    tags_to_collapse = {}
    find_tags_to_collapse(rootdict, tags_to_collapse)
    collapse_txts(rootdict, tags_to_collapse)

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
    # loop through and fill out all the fields on this level
    for field in rootdict:
        if not isinstance(rootdict[field][0], dict):
            if "fields" not in ret_dict:
                ret_dict["fields"] = {}
            ret_dict["fields"][field] = rootdict[field]
    # now loop and fill out any children
    for field in rootdict:
        if isinstance(rootdict[field][0], dict):
            for child in rootdict[field]:
                tempdict = collapse_hierarchy(child)
                for child_field in tempdict:
                    key = field + ">" + child_field
                    # if this level of hierarchy has a foreign key, put the foreign key into each of the children so they can reference the parent structure
                    if key in foreign_keys:
                        for ch in tempdict:
                            key2 = field + ">" + ch
                            if key2 not in foreign_keys:
                                for ind in tempdict[ch]:
                                    ind[foreign_keys[key]["column_name"]] = tempdict["fields"][foreign_keys[key]["xml_field_name"]]
                    if key not in ret_dict:
                        ret_dict[key] = []
                    if isinstance(tempdict[child_field], list):
                        ret_dict[key] += tempdict[child_field]
                    else:
                        ret_dict[key].append(tempdict[child_field])
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
            fill_and_clean_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["Units"][0])
            
        case 'structuregroups':
            print("parsing structure groups xml...")
            tree = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-structuregroups.xml")#STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
            fill_and_clean_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["StructureGroups"][0])

        case "articles":
            print("parsing articles xml...")
            tree = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-articles.xml")#STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
            fill_and_clean_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["Articles"][0])
        
        case "products" | "product2gs":
            print("parsing products xml...")
            tree = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-product2gs.xml")#STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
            fill_and_clean_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["Product2Gs"][0])

        case "structurefeatures":
            print("parsing structure features xml...")
            tree = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-structurefeatures.xml")#STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
            fill_and_clean_lists(root, rootdict)
            print("putting xml data into tables...")
            collapsed = collapse_hierarchy(rootdict["StructureFeatures"][0])

    return collapsed

def get_varchar_lengths(table):
    fields = {}
    for row in table:
        for key in row:
            if key not in fields:
                fields[key] = 0
            try:
                row[key] = float(row[key])
            except:
                pass
            
            if isinstance(row[key], str):
                fields[key] = max(fields[key],len(row[key]))
    return fields

if __name__ == '__main__':

    collapsed = get_xml_tables("structureFeatures")

    for i, key in enumerate(collapsed):
        print(f"{i + 1}: {key}")
        print(write_create_table("a",get_varchar_lengths(collapsed[key])))
    #print(get_varchar_lengths(collapsed["Unit>Langs>Lang>fields"]))
    #print(collapsed["StructureGroup>Assets>Asset>fields"])#>Attribute>Values>Value>fields"])