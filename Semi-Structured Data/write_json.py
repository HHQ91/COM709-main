import json

data = {

    "name" : "prins",
    "job" : "Lecturer"
}

with open("exported.json",'w') as file:
    json.dump(data, file, indent=4)