import json
data = {
    "employees": [
        {
            "firstName":"John",
            "lastName":"Doe"},
        {
            "firstName":"Anna",
            "lastName":"Smith"
        },
        {
            "firstName":"Peter",
            "lastName":"Jones"
        }
    ]
}

print(type(data))

with open("data_file.json", "w") as file:
    # json.dump(data, file)
    json.dump(data, file, indent=4)
json.dumps(data, indent=4)

print(json.dumps(data))