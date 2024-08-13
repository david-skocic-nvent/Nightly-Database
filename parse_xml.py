import xml.etree.ElementTree as et
from constants import *

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

def recursiveFill2 (parent, parent_dict):
    if len(parent.attrib) > 0:
        parent_dict["attribs"] = parent.attrib
    if len(parent) > 0:
        parent_dict["children"] = {}
        for element in parent:
            tgstr = tagstring(element.tag)
            if tgstr in parent_dict["children"]:
                if isinstance(parent_dict["children"][tgstr], dict):
                    tempdict = parent_dict["children"][tgstr]
                    parent_dict["children"][tgstr] = []
                    parent_dict["children"][tgstr].append(tempdict)
                parent_dict["children"][tgstr].append({})
                recursiveFill(element, parent_dict["children"][tgstr][-1])
            else:
                parent_dict["children"][tgstr] = {}
                recursiveFill(element, parent_dict["children"][tgstr])

    if parent.text is not None and not parent.text.isspace():
        parent_dict["text"] = parent.text

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

def get_xml_dict(whichFile):
    rootdict = {}
    match whichFile.lower():
        case 'units':
            tree = et.parse(UNITS_FILEPATH)
            root = tree.getroot()
    
    recursiveFill(root, rootdict)
    return rootdict

if __name__ == '__main__':
    rootdict = {}

    recursiveFill(structure_group_root, rootdict)
    for k in rootdict:
        print(k)

    print(rootdict["StructureGroups"]["StructureGroup"][0])