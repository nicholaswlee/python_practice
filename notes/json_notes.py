### JSON JavaScript Object Notation
### Format is like JavaScript in a way

import json

### JSON has "objects", which python will turn into
### dictionaries
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"   
    }'''
### loads essentially just returns a dictionary
### JSON is a lot more simple compared to XML
### so it is easier to use, but not as rich.
info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Nicholas"
    },
    {   "id" : "002",
        "x" : "7",
        "name" : "Nathan"
    }
]'''
info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])