import requests
from alternate_advanced_caching import Cache
from Scrap import *
import emoji
import base64
import requests




client_key = 'cRu8av1Z9ZThlZ1w89FCLe8MY'
client_secret = 'RGzsChyii5gh4fw3tZsXLFJcVkrSSesYmeLdvu4wRkcmbapbir'

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
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

Cache_name_twitter = "Twitter_cache.json"
Twitter_cache = Cache(Cache_name_twitter)
lst_twitter_url = []



def get_all_emoji():
    str_emoji = ""
    for i in list(emoji.EMOJI_UNICODE.values()):
        str_emoji = str_emoji+i
    return str_emoji

def search_twitter(name):
    search_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    pd = {}
    pd["query"] = "#" + name

    search_url = '{}1.1/tweets/search/30day/dev1.json'.format(base_url)
    unique_url = search_url+ name
    lst_twitter_url.append(unique_url)
    for url in lst_twitter_url:
        if Twitter_cache.get(unique_url) is None:
            twitter_data = requests.get(search_url, headers=search_headers, params=pd).json()
            html_text = twitter_data
            Twitter_cache.set(unique_url, html_text, 30)

    return Twitter_cache.get(url)


artists_lst = get_top_billboard(2018, "top artists")[:10]
# print(search_twitter("Ed sheeran"))

def get_emoji(twitter_data):
    emoji_dict = {}
    for result in twitter_data["results"]:
        text = result["text"]
        for word in text:
            if word in emoji.UNICODE_EMOJI:
                if word not in emoji_dict.keys():
                    emoji_dict[word] = 1
                else:
                    emoji_dict[word]+= 1

    return emoji_dict



def whole_emoji_dict(artists_lst):
    whole_dict = {}
    whole_dict_sorted = {}
    for each in artists_lst:
        try:
            twitter_data = search_twitter(each)
            emoji_dict = get_emoji(twitter_data)
            whole_dict[each] = emoji_dict
            whole_dict_sorted[each] = sorted(emoji_dict, key = lambda x: emoji_dict[x],reverse = True)[0]
        except :
            print("No emoji Found")
            continue
    return [whole_dict, whole_dict_sorted]

whole_dict = whole_emoji_dict(artists_lst)[0]
whole_dict_sorted = whole_emoji_dict(artists_lst)[1]
print(whole_dict_sorted)



    
        



        









