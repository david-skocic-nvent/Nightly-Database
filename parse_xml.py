import xml.etree.ElementTree as et
from constants import *



def tagstring(uglytag):
    return uglytag[uglytag.index('}') + 1:]

def recursiveFill (parent, parent_dict):
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
                recursiveFill(element, parent_dict[tgstr][-1])
            else:
                parent_dict[tgstr] = {}
                recursiveFill(element, parent_dict[tgstr])

    if parent.text is not None and not parent.text.isspace():
        parent_dict["text"] = parent.text

def recursiveFill_Always_List (parent, parent_dict):
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
            recursiveFill_Always_List(element, parent_dict[tgstr][-1])

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

def tablify (rootdict):
    ret_dict = {}
    for field in rootdict:
        if isinstance(rootdict[field],list):
            field_list = []
            for el in rootdict[field]:
                field_list.append(tablify(el))
            ret_dict[field] = field_list
        else:
            if "fields" not in ret_dict:
                ret_dict["fields"] = {}
            ret_dict["fields"][field] = rootdict[field]
    return ret_dict

                
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


def get_xml_dict(whichFile):
    rootdict = {}
    match whichFile.lower():
        case 'units':
            tree = et.parse(UNITS_FILEPATH)
            root = tree.getroot()
        case 'structuregroups':
            tree = et.parse(STRUCTURE_GROUPS_FILEPATH)
            root = tree.getroot()
    
    recursiveFill(root, rootdict)
    return rootdict

if __name__ == '__main__':

    sgroot = et.parse("C:\\Users\\E2023355\\OneDrive - nVent Management Company\\Documents\\VSCode\\Projects\\Nightly Database\\Sample Data\\catalogdata-structuregroups.xml").getroot()
    rootdict = {}

    #recursiveFill(sgroot, rootdict)
    recursiveFill_Always_List(sgroot, rootdict)
    collapsed = collapse_hierarchy(rootdict["StructureGroups"][0])
    
    for table in collapsed:
        fields = set()
        print(table)
        for row in collapsed[table]:
            fields = fields | row.keys()
        print(fields)
    #recursivePrint(collapsed)

    #for i in range(10):
        #recursivePrint(rootdict["StructureGroups"][0]["StructureGroup"][i])
    exit()
    fields = set()
    psfields = set()
    for structureGroup in rootdict["StructureGroups"]["StructureGroup"]:
        if "Attributes" in structureGroup:
            if len(structureGroup["Attributes"]) != 0:
                if isinstance(structureGroup["Attributes"]["Attribute"], list):
                    for attribute in structureGroup["Attributes"]["Attribute"]:
                        for field in attribute:
                            fields.add(field)
                            if "Values" in attribute:
                                if isinstance(attribute["Values"]["Value"], list):
                                    for preset_value in attribute["Values"]["Value"]:
                                        for f in preset_value:
                                            psfields.add(f)
                else:
                    for field in structureGroup["Attributes"]["Attribute"]:
                        fields.add(field)
    print(fields)
    print(psfields)
else:
    structure_group_tree = et.parse(STRUCTURE_GROUPS_FILEPATH)
    structure_group_root = structure_group_tree.getroot()

    units_tree = et.parse(UNITS_FILEPATH)
    units_root = units_tree.getroot()

    articles_tree = et.parse(ARTICLES_FILEPATH)
    articles_root = articles_tree.getroot()

    product2gs_tree = et.parse(PRODUCT2GS_FILEPATH)
    product2gs_root = product2gs_tree.getroot()

    structure_features_tree = et.parse(STRUCTURE_FEATURES_FILEPATH)
    structure_features_root = structure_features_tree.getroot()