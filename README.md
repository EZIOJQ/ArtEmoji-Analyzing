# Jieqing Chen

## Please install the following libraries:
* bs4
* requests
* datetime
* json
* emoji
* os
* base64

### Reminder:
* For the emoji library, you can check this link to install: https://pypi.org/project/emoji
* For the visual part, you need to run extra files, and start your local sever via using '$ python3 -m http.sever' in terminal.

## Project Overview
This project contains two different functions but both are based on twitter api:
* Search the last 30 day twitter data to figure out which emoji people used most to describe an artist and a song.
* The network graph will give you the network between all the emojis people are using to describe an artist or a song.
* Three data sources used: Billboard, Twitter, d3.js
* Caching for twitter data is in 'twitter_cache.json'. Scrapping caching file is 'Artists_cache.json', using codes from `alternative_advanced_caching.py`

## Sample Output
* Sample output for d3 network graph of different emojis and artists.
![](https://github.com/EZIOJQ/ArtEmoji-Analyzing/blob/master/Sample_network_graph.png)
* Image 'Sample_most_emoji' is the sample output of the command '1'
![](https://github.com/EZIOJQ/ArtEmoji-Analyzing/blob/master/Sample_most_emoji.png)

## Run Process

### PartI:
* Make sure you have installed all the libraries listed above. You need to get twitter api and secret key which I provide my key in the 'twitter_offical.py". To get the key, you can visit https://developer.twitter.com/en/docs/basics/getting-started
* Run file 'twitter.py'
* Try command '1' to see the most emoji people used to describe each artists in top30 of billboard.
* Try command '2' to see the most emoji people used to describe each songs in top30 of billboard.
* Quit input by `exit`

### PartII:
* Run Generatenood.py AFTER you have run the main file('Twitter.py') and make sure there are two files in the directory: 'whole_dict_artists.json' and 'whole_emoji_artists.json'
* When 'network.json' has shown up, you need to start sever in this directory.
* In your browser, go to 'http://0.0.0.0:8000/' to see the graph.

#### Overview


## Main file overview:
* Twitter.py: program the interactive command lines and generate necessary files for visualization.
* Generatenood.py: define Foundation class and Color class, include codes that scrapes the color hex codes, and API to change them to hsl color mode
* Twitter_test.py: test file
* index.html: Use D3.js and json file generated before to make visualization.
* advanced_expiry_caching.py: copy from code provided on the class. Define a chache class to store the respond to a cache file.
* README.md






