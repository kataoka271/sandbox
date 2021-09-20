import xml.etree.ElementTree as ET


tree = ET.parse(r"C:\Users\k_hir\Downloads\NewDatabase.xml")
root = tree.getroot()

print("List of customized sequences")
print("----------------------------")
for entry in root.findall(".//Group/Entry/AutoType/DefaultSequence/../.."):
    seq = entry.find("./AutoType/DefaultSequence")
    tit = entry.find("./String/Key[.='Title']/../Value")
    print("{}: {}".format(tit.text, seq.text))

print("")
print("List of window associations")
print("---------------------------")
for entry in root.findall(".//Group/Entry/AutoType/Association/Window/../../.."):
    win = entry.find("./AutoType/Association/Window")
    tit = entry.find("./String/Key[.='Title']/../Value")
    print("{}: {}".format(tit.text, win.text))

print("")
print("List of unknown fields")
print("----------------------")
knownFields = ["Notes", "Password", "Title", "URL", "UserName"]
d = {}
for entry in root.findall(".//Group/Entry"):
    title = None
    L = []
    for keyvalue in entry.findall("String"):
        key = keyvalue.find("Key")
        value = keyvalue.find("Value")
        if key.text == "Title":
            title = value.text
        if key.text not in knownFields:
            L.append((key.text, value.text))
    if title is None:
        raise ValueError("Entry has no title")
    if L:
        d[title] = L

for title, value in d.items():
    print("* {}".format(title))
    for k, v in value:
        print("  {}: {}".format(k, v))
