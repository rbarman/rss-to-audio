import feedparser as fp
from gtts import gTTS as gT
import argparse

def get_summaries(feed_url):
	'''parse rss feed to get article summaries'''
	parsed = fp.parse(feed_url)
	return [news.summary for news in parsed['entries']]

def create_audio(feed_urls,filename):
	'''create audio file of news summaries from all feeds'''

	news_summaries = []
	# get news summaries from each rss feed
	for url in feed_urls:
		news_summaries = news_summaries + get_summaries(url)
 	
	news_string = ' NEXT STORY. '.join(news_summaries)
	tts = gT(news_string).save(filename)

if __name__ == "__main__":

	# get command line arguments
	parser = argparse.ArgumentParser(description='Create audio of your rss feeds')
	parser.add_argument('--feeds',help="text file with list of feeds",required=True)
	parser.add_argument('--filename',help="name of audio file to create",required=True)
	args = parser.parse_args()

	# create audio
	with open(args.feeds) as f:
		feed_urls = f.read().splitlines()
	filename = args.filename
	create_audio(feed_urls,filename)
