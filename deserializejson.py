import json

json_string = """
    {
        "firstname":"Fanny",
        "lastname":"Lorenz",
        "city":"Shigatse",
        "country":"Senegal",
        "countryCode":"No",
        "email": "Fanny.Lorenz@gmail.com"
    }
"""

python_dict = json.loads(json_string)

print(type(python_dict))
print(python_dict['firstname'])
print(python_dict['lastname'])