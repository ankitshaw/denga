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
		if tag.startswith("J") or tag.startswith("R") or tag.startswith("V") or tag.startswith("N"):
			woi.append(word)
	return woi



def nlp_test():
	# df = pd.read_csv(filePath,sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	data = ["i want to swim"] # 'I will work from home today'
	df= pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist() #first column of data frame i.e. all sentences

	# get list of synonyms for each word in filtered sentence
	for sentence in datasetList:
		sentenceFiltered = removeStopWords(sentence)
		print("filtered sentence: ", sentenceFiltered)
		tag = getPosTag(sentenceFiltered)
		print("tag: ", tag)
		woi = getWordsOfInterest(tag)
		print("woi: ", woi)
		synonym_dict = {}
		for word in woi:
			synonyms = getSynonyms(word)
			synonym_dict[word] = synonyms
		print(synonym_dict)

		print("no of woi: ", len(woi))
		no_of_words_to_be_replaced = 2 #flag to set how many words need to be replaced
		generated_sentences=[]
		if no_of_words_to_be_replaced <=len(woi):
			for i in range(0,no_of_words_to_be_replaced):
				# print(list(synonym_dict.values())[i]) #some check needs to be there to map lemma with actual word in sentence: Lets --> Let
				for syn in list(synonym_dict.values())[i]:
					generated_sentence = sentence.replace(list(synonym_dict.keys())[i], syn)
					# here keep a check based on similarity threshold, only if it passes: append to final list
					generated_sentences.append(generated_sentence)
		generated_sentences=set(generated_sentences)
		print(generated_sentences)

nlp_test()

# https://nlpforhackers.io/wordnet-sentence-similarity/