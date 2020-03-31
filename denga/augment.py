import nltk
import pandas as pd
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))
def removeStopWords(sentence):
		filtered_sentence = " ".join(filter(lambda word: word not in stop_words, sentence.split()))
		return filtered_sentence

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

#def nlp(filePath):
def nlp():
	# df = pd.read_csv(filePath,sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	data = ['I will be logging in from home today', 'working from home today']
	df=pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist() #first column of data frame i.e. all sentences

	#remove stop words
	sentenceMap = {} #mapping original sentence to filtered sentence
	for sentence in datasetList:
		sentenceMap[sentence] = removeStopWords(sentence)
	print("Sentence Map: ",sentenceMap)

	# pos tagging to know which words can be replaced with their synonyms/hypernym/hyponym (maybe not required???)

	# get list of synonyms for each word in filtered sentence
	for filteredSentence in sentenceMap.values():
		for word in filteredSentence.split():
			synonyms = getSynonyms(word)
			print(synonyms)

	# generate all combinations of new sentences

	# check grammatical validity of sentences

	# generatedDataset = [getSynonym(x) for x in datasetList]

	# return generatedDataset

nlp()

