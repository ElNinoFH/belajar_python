import json

with open("data_json.json","r", encoding="utf-8") as file:
    python_dict = json.load(file)

x = python_dict[0]
# print(python_dict)
print(x['maps']['googleMaps'])
print(x['population'])