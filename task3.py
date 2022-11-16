import json
import sys

def Value_change(item, values):
	for value in values["values"]:
		if (item["id"] == value["id"]):
			item["value"] = value["value"]
	return item

def Values(item):
	if "values" in item:
		for i in item["values"]:
			i = Values(i)
			Value_change(i, values)
	return item
with open(sys.argv[1], 'r') as d:
	data = json.loads(d.read())
with open(sys.argv[2], 'r') as v:
	values = json.loads(v.read())

for item in data["tests"]:
	item = Value_change(item, values)
	item = Values(item)
new_json = json.dumps(data, indent=2)
with open("report.json", 'w') as f:
	f.write(new_json)