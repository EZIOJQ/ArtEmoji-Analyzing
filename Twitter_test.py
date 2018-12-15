import unittest
from Twitter import *

class setup:

	def __init__(self):
		self.search_lst = get_top_billboard(2018, "top artists")[:3]
		self.twitter_data = search_twitter("Ed Shareen")
		self.emoji = get_emoji(self.twitter_data)

class Testinit_scrap(unittest.TestCase):
	def test_checkscarp(self):
		artist_data = get_top_billboard(2018, "top artists")
		try:
			for i in artist_data:
				isinstance(i, str)
		except:
			self.fail()

	def setUp(self):
		self.search_lst = get_top_billboard(2018, "top artists")[:30]
		self.twitter_data = search_twitter("Ed Shareen")
		self.emoji = get_emoji(self.twitter_data)

	def test_check_emoji(self):
		self.assertEqual(type(self.emoji), type((1,2)))
			


class TestCheck_cache(unittest.TestCase):
	def test_generate_cache(self):
		try:
			with open("Artists_cache.json") as f:
				text = json.loads(f.read())
				i = list(text.keys())[0]
		except:
			self.fail()

	def test_check_twitter_cache(self):
		try:
			with open("Twitter_cache.json") as f:
				text = json.loads(f.read())
				i = list(text.keys())[0]
		except:
			self.fail()

	def test_emoji_dict(self):
		try:
			with open("whole_emoji_artists.json") as f:
				text = json.loads(f.read())
				i = text["1"][0]
		except:
			self.fail()

class TesttwitterMain(unittest.TestCase):
	def test_emoji(self):
		self.assertEqual(type(Emoji().emoji_all_lst), type([]))
		self.assertEqual(len(Emoji().emoji_all_lst), 2623)

	def test_emoji_str(self):
		try:
			self.assertEqual(get_emoji(setup().twitter_data), setup().emoji)
		except:
			self.fail()

	def test_check_emoji_in(self):
		try:
			self.assertEqual(setup().search_lst, ["Drake", "Post Malone", "Ed Sheeran"])
		except:
			self.fail()

	def test_network(self):
		try:
			with open("network.json") as f:
				text=  json.loads(f.read())
				self.assertTrue(len(text["nodes"]) > 30)
		except:
			self.fail()




if __name__ == '__main__':
    unittest.main()

