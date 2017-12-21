import json
import shutil

def fixup (adict, v):

    new_name = '#' + str(v)
    for key in adict.keys():
        if key == "sku":
            adict[key] = str(v)
        if key == "name":
            adict[key] = new_name
        if key == "custom_url_key":
            adict[key] = 'www.' + new_name + ".com"
        elif type(adict[key]) is dict:
            fixup(adict[key], v)

with open('testproduct.json', 'r') as originalJson:
    json_data = json.load(originalJson)

for i in range(1, 100001):
    print("json file no: " + str(i))
    fixup(json_data, i)
    with open('jsons/testJson{}.json'.format(i), 'w') as file:
      json.dump(json_data, file)

shutil.make_archive('test', 'zip', 'jsons')
