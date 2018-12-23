import requests
from alternate_advanced_caching import Cache
from Scrap import *
import emoji
import base64
import os
from Twitter_official import *







Cache_name_twitter = "Twitter_cache.json"
Twitter_cache = Cache(Cache_name_twitter)
lst_twitter_url = []



def init_twitter(client_key, client_secret):


    client_key = client_key
    client_secret = client_secret

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')

    return key_secret


key_secret = init_twitter(client_key, client_secret)

b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')
base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']


class Media:
    def __init__(self,search_term):

        self.type = search_term
        self.rank = {}
        self.name = get_top_billboard(2018, self.type)[:30]

    def get_top_10(self):
        for i in rang(10):
            return self.name[i]

    def save_rank(self):
        for i in self.name:
            index = self.name.index(i) - 1
            self.rank[index] = i
        return self.rank



class Emoji:
    def __init__(self):
        self.emoji_all_lst = list(emoji.EMOJI_UNICODE.values())
        self.emoji_all_str = ""
        for i in self.emoji_all_lst:

            self.emoji_all_str = self.emoji_all_str+i




def search_twitter(name):

    search_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    pd = {}
    pd["query"] = name

    search_url = 'https://api.twitter.com/1.1/tweets/search/30day/dev1.json'
    unique_url = search_url+ name
    lst_twitter_url.append(unique_url)
    for url in lst_twitter_url:
        if Twitter_cache.get(unique_url) is None:
            twitter_data = requests.get(search_url, headers=search_headers, params=pd).json()
            html_text = twitter_data
            Twitter_cache.set(unique_url, html_text, 30)

    return Twitter_cache.get(url)


def get_emoji(twitter_data):
    emoji_dict = {}
    emoji_lst = []
    for result in twitter_data["results"]:
        text = result["text"]
        for word in text:
            if word in emoji.UNICODE_EMOJI:

                if word not in emoji_dict.keys():
                    emoji_dict[word] = 1
                    emoji_lst.append(word)
                    # print(emoji_lst)
                else:
                    emoji_dict[word]+= 1

    return emoji_dict,emoji_lst



def whole_emoji_dict(artists_lst,tp):
    tp = tp
    whole_dict = {}
    whole_dict_sorted = {}
    emoji_lst = []
    temp= {}
    for each in artists_lst:
        try:
            twitter_data = search_twitter(each)
            emoji_dict = get_emoji(twitter_data)[0]
            whole_dict[each] = emoji_dict
            for i in get_emoji(twitter_data)[1]:
                if i not in emoji_lst:
                    emoji_lst.append(i)
                else:
                    continue
            whole_dict_sorted[each] = sorted(emoji_dict, key = lambda x: emoji_dict[x],reverse = True)[0]
        except :
            continue
    with open("whole_dict_{}.json".format(tp),"w") as f:
        f.write(json.dumps(whole_dict,indent = 4))
    with open("whole_emoji_{}.json".format(tp),"w") as f2:
        temp["1"] = emoji_lst
        f2.write(json.dumps(temp, indent = 4))
    return [whole_dict, whole_dict_sorted,emoji_lst]



def main():

    init_twitter(client_key,client_secret)

    print("Which type of media do you want to search? ")
    print("1. top artists")
    print("2. hot 100 songs")
    print("type 'exit' to exit")


    search_term = input("Please chose the index")
    try:
        if search_term =="1":
            artists_lst = Media("top artists").name
            whole_dict = whole_emoji_dict(artists_lst,"artists")[0]
            whole_dict_sorted = whole_emoji_dict(artists_lst, "artists")[1]
            emoji_lst = whole_emoji_dict(artists_lst,"artists")[2]
            print("the name and most frequent emoji are:")
            for i in artists_lst:
                try:
                    print("{}.".format(artists_lst.index(i)+1) + "{}".format(i) + " {}".format(whole_dict_sorted[i]))
                except:
                    continue
        elif search_term == "2":
            artists_lst = Media("hot 100 songs").name
            whole_dict = whole_emoji_dict(artists_lst,"songs")[0]
            whole_dict_sorted = whole_emoji_dict(artists_lst, "songs")[1]
            emoji_lst = whole_emoji_dict(artists_lst,"songs")[2]
            print("the name and most frequent emoji are:")
            for i in artists_lst:
                try:
                    print("{}.".format(artists_lst.index(i)+1) + "{}".format(i) + " {}".format(whole_dict_sorted[i]))
                except:
                    continue

        else:
            print("please input a right commend!")
    except:
        print("please input a right commend!")

main()















    
        



        









