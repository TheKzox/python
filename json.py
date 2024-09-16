import json
import xml.etree.ElementTree as ET

data = []
print('Enter information as [name / last name / phone number / favourite programming language] | press Q or q to Quit')

while True:
    line = input()
    if line == '0':
        break

    line = line.split(",")
    info = {
        'name': line[0],
        'last_name': line[1],
        'phone_number': line[2],
        'fav_lang': line[3]
    }

    data.append(info)


# JSON
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


# XML
root = ET.Element("people")

for person in data:
    person_element = ET.SubElement(root, "person")
    for key, value in person.items():
        child = ET.SubElement(person_element, key)
        child.text = value

tree = ET.ElementTree(root)
tree.write("data.xml")