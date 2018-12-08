import json
import os

def generate_movie_nodes_and_links():
    node_list = []
    link_list = []  
    with open("movie_data.json", "r") as f:
        movieDict = json.loads(f.read())
        for k, v in movieDict.items():
            newNode = {"id": k, "group": 0}
            node_list.append(newNode)
            for ch in v["Characters"]:
                link_list.append({"source": k, "target": ch, "value": 0})
    return (node_list, link_list)

def generate_character_nodes_and_links():

    character_node_dict = {}
    link_list = []
    relative = 0
    for filename in os.listdir("character_data_files/"):
        if filename[-5:] == ".json":
            with open("character_data_files/"+filename, "r") as f:
                characterDict = json.loads(f.read())
                name = characterDict["codeName"]
                for ally in characterDict["allies"]:
                    link_list.append({"source": name, "target": ally, "value": 1})
                for enemy in characterDict["enemies"]:
                    link_list.append({"source": name, "target": enemy, "value": 2})
                squad = 0
                if "Avengers" in characterDict["groups"]:
                    squad = 1
                elif "Guardians of the Galaxy" in characterDict["groups"]:
                    squad = 2
                try:
                    character_node_dict[name].update({"squad": squad})
                except:
                    character_node_dict[name] = {"group": 1, "squad": squad}

                if characterDict["relatives"] and character_node_dict[name].get("relative") == None:

                    character_node_dict[name].update({"relative": relative})
                    for c in characterDict["relatives"]:
                        try:
                            character_node_dict[c].update({"relative": relative})
                        except:
                            character_node_dict[c] = {"group": 1, "relative": relative}
                    relative += 1
    return (character_node_dict, link_list)

def flat_node_to_JSON():

    movie_data = generate_movie_nodes_and_links()
    character_data = generate_character_nodes_and_links()
    movie_node = movie_data[0]
    movie_link = movie_data[1]
    character_node = []
    character_link = character_data[1]
    for k, v in character_data[0].items():
        newDict = {"id": k}
        newDict.update(v)
        character_node.append(newDict)

    jsonDict = {"nodes": movie_node+character_node, "links": movie_link+character_link}
    with open("network.json", "w") as f:
        f.write(json.dumps(jsonDict, indent=2))

flat_node_to_JSON()
