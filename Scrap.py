from bs4 import BeautifulSoup as bs
from alternate_advanced_caching import Cache
from datetime import datetime
import json
import requests




lst_url = []


Cache_name = "Artists_cache.json"
artists_cache = Cache(Cache_name)

def check_cache(lst_url):

    for url in lst_url:
        if artists_cache.get(url) is None:
            data = requests.get(url)
            html_text = data.text
            artists_cache.set(url, html_text, 30)


def get_top_billboard(year,search_term):
	year = int(year)
	search_term = search_term.replace(" ","-")
	primary_url = str("https://www.billboard.com/charts/year-end/{}/{}".format(year,search_term))
	lst_url.append(primary_url)
	check_cache(lst_url)
	soup = bs(artists_cache.get(primary_url), features = "html.parser")
	name = [i.get_text().replace("\n","") for i in soup.find_all(class_= "ye-chart-item__title")]
	# print(artists_name)
	return name

# print(get_top_billboard(2018, "top artists"))






















