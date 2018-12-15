import json
import os







def gernerate_artists_node_links(tp):
	tp = tp
	node_list = []
	link_list = []
	with open("whole_dict_artists.json".format(tp), "r") as f:
		artistDict = json.loads(f.read())
		for k, v in artistDict.items():
			newNode = {"id": k, "group": 0, "photo": "img/{}.jpg".format(str(k).replace(" ","-").lower())}
			# newNode = {"id": k, "group": 0}
			node_list.append(newNode)
			for emoji in v:
				link_list.append({"source": k, "target": emoji, "value": v[emoji]})
	with open("whole_emoji_artists.json".format(tp),"r") as f2:
		emojilst = json.loads(f2.read())["1"]
		for i in emojilst:
			newNode_emoji = {"id": i, "group":1}
			node_list.append(newNode_emoji)
	return (node_list, link_list)


# print(gernerate_artists_node_links())


def flat_node(tp):
	tp = tp
	node_lst = gernerate_artists_node_links(tp)[0]
	link_lst = gernerate_artists_node_links(tp)[1]
	jsonDict = {"nodes": node_lst, "links": link_lst}
	with open("network.json", "w") as f:
		f.write(json.dumps(jsonDict, indent=2))

flat_node(tp)


