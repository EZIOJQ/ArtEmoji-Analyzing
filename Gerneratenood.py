import json
import os


def gernerate_artists_node_links():
	node_list = []
	link_list = []
	with open("whole_dict.json", "r") as f:
		artistDict = json.loads(f.read())
		for k, v in artistDict.items():
			newNode = {"id": k, "group": 0}
			node_list.append(newNode)
			for emoji in v:
				link_list.append({"source": k, "target": emoji, "value": v[emoji]})
	return (node_list, link_list)


# print(gernerate_artists_node_links())


def flat_node():
	node_lst = gernerate_artists_node_links()[0]
	link_lst = gernerate_artists_node_links()[1]
	jsonDict = {"nodes": node_lst, "links": link_lst}
	with open("network.json", "w") as f:
		f.write(json.dumps(jsonDict, indent=2))

flat_node()
