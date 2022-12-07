import json

with open('tree.json', 'r') as r:
    data = json.load(r)

print(json.dumps(data, indent = 4, sort_keys=True))