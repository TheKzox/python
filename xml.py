import json
import xml.etree.cElementTree as Et

date = []

print("inter your id")

while True:
    edame = str(input())
    if edame == 'q':
        break

    edame = edame.split(',')
    info = {
        'name': edame[0],
        'family': edame[1],
        'phone_number': edame[2],
        'favorite_lang': edame[3]
    }
    date.append(info)

with open('data.json', 'w') as json_file:
    json.dump(date, json_file, indent=4)

root = Et.Element("people")

for person in date:
    person_element = Et.SubElement(root, "person")
    for key, value in person.items():
        child = Et.SubElement(person_element, key)
        child.text = value


tree = Et.ElementTree(root)
tree.write("date.xml", encoding='unicode', xml_declaration=True)


