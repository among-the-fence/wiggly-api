import json
with open('app/heroData.json') as file:
    herojson = json.load(file)
herodata = []
for i in herojson["heroes"]:
    herodata.append(i)