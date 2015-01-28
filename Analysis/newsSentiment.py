#@author: Uday Sharma
#@Description: Perfoming sentiment analysis on News stories

import json
import string 
import re
import urllib2



#Get the required data for sentiment analysis
# Need a better mechanism for importing the txt files, perhaps host them online and import from url, will decide.
try:
	newsfeed  = urllib2.urlopen('http://timesofindia.indiatimes.com/feeds/newsfeed/-2128936835.cms?feedtype=sjson')
	positiveWords = open('/Users/udaysharma/Documents/NewsCheck/data/positive-words.txt', 'r')
	negativeWords = open('/Users/udaysharma/Documents/NewsCheck/data/negative-words.txt', 'r')
	profaneWords = open('/Users/udaysharma/Documents/NewsCheck/data/profane-words.txt', 'r')
	
except: 
	print "No Data Found"
	exit()
 

posList = []
negList = []
profaneList = []


# This is a simple word cound method for getting the occurance of each word in the list, 
# it returns a dictionary of structure {('word1', count), ('word2', count)}
def getFrequency(wordList):
	word_frequency = {}
	for word in wordList:
		if word not in word_frequency:
			word_frequency[word] = 1
		else:
			word_frequency[word] +=1
	freq = word_frequency
	word_frequency = {}
	return freq



# This function will distribute words in the story text into three sets namely,
# positive, negative and profane
def distributeWords(storyWords):
	posWords = re.split(r'\n', positiveWords.read())
	negWords = re.split(r'\n', negativeWords.read())
	profWords = re.split(r'\r\n', profaneWords.read())
	
	for word in storyWords:
		if word in posWords:
			posList.append(word)
		elif word in negWords:
			negList.append(word)
		elif word in profWords:
			profaneList.append(word)
		else:
			continue

	negCount = getFrequency(negList)
	posCount =  getFrequency(posList)
	profConunt= getFrequency(profaneList)
	print profConunt
	
# This function is for analyzing each sentence in a story article and assign some sort of score 
# for classifying if it is good or bad.
def analyseSentances(storyText):
	sentences = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", storyText)
	for sent in sentences:
		wordList = sent.split()
		#printing for sake of showing the prgram output
		print sent
		# yet to write logic for classifying the sentance

		

		
# The code below needs to be grouped into a method, after all key methods are defined.

article= {}
count = 0
newsData = json.load(newsfeed)
newsArticles = newsData['NewsItem']

for news in newsArticles:
	article = news['Story']
	story = article.encode('utf8')
	storyText= story.lower()
	storyWords = storyText.split()
	analyseSentances(storyText)
	




	