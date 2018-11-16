import json


filename = 'apps.json'

data = json.load(open(filename))
print(data.keys())
categories = data['categories']
apps = data['apps']
print(len(apps))

# print(categories)

table = []
for app, info in apps.items():
    cats = info['cats']
    for cat in cats:
        categories[str(cat)].setdefault('items', []).append(app)
    score = 0

    cats = [categories[str(i)]['name'] for i in cats]
    for cat in cats:
        row = [app, cat, score]
        table.append(row)


# print(table)
print(len(table))
from pprint import pprint; pprint(table)

tech = {'data': table}
with open('tech.json', 'w') as fh:
    json.dump(tech, fh)


for key, value in categories.items():
    # print(value['name'], len(value.get('items', [])))
    pass
