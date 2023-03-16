import json
test1 = {}
test2 = dict()
test1 = {"name": "Ярик","age":14}
print(test1["name"])
test1["password"]="bablkwas"
print(test1)
new_json = json.dumps(test1,indent = 4)
print(new_json)