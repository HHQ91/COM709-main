import  json

with open("data.json") as file:
    data = json.load(file)
    university = data["university"]

    print(f"the name of the uni is : {university}")

    lectures = data["lectures"]

    for lecturer in lectures:
        name = lecturer['name']
        print(f'The name of the lecturer is {name}')

    