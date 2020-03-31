import nltk
import pandas as pd
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import DefaultTagger 

stop_words = set(stopwords.words('english'))
def removeStopWords(sentence):
		filtered_sentence = " ".join(filter(lambda word: word not in stop_words, sentence.split()))
		return filtered_sentence

def getPosTag(sentence):
	text = word_tokenize(sentence)
	tags = nltk.pos_tag(text)
	return tags

def getSynonyms(word):
	"""This function returns a list of synonyms for each word passed to it"""
	#implementation needed
	#use nltk wordnet
	synonyms = []
	for syn in wordnet.synsets(word):
		# print(syn.name(), " ", syn.definition(), " ", syn.examples())
		for l in syn.lemmas():
			synonyms.append(l.name())
	return synonyms

def getWordsOfInterest(tags):
	woi = []
	for (word, tag) in tags:
		if tag.startswith("J") or tag.startswith("R") or tag.startswith("V"):
			woi.append(word)
	return woi

def nlp(filePath):
	df = pd.read_csv(filePath, sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	df = pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist()

	for sentence in datasetList:
		sentenceFiltered = removeStopWords(sentence)
		tag = getPosTag(sentenceFiltered)
		woi = getWordsOfInterest(tag)
		synonym_dict = {}
		for word in woi:
			synonyms = getSynonyms(word)
			synonym_dict[word] = set(synonyms)
		print(synonym_dict)



def nlp_test():
	# df = pd.read_csv(filePath,sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	data = ['I will be logging in from home today', 'I will working from home today']
	df= pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist() #first column of data frame i.e. all sentences

	# pos tagging to know which words can be replaced with their synonyms/hypernym/hyponym (maybe not required???)

	# get list of synonyms for each word in filtered sentence
	for sentence in datasetList:
		sentenceFiltered = removeStopWords(sentence)
		tag = getPosTag(sentenceFiltered)
		woi = getWordsOfInterest(tag)
		synonym_dict = {}
		for word in woi:
			synonyms = getSynonyms(word)
			synonym_dict[word] = set(synonyms)
		print(synonym_dict)


	# generate all combinations of new sentences

	# check grammatical validity of sentences

	# generatedDataset = [getSynonym(x) for x in datasetList]

	# return generatedDataset

nlp_test()

