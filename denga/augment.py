import nltk
import pandas as pd
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import DefaultTagger
import operator
import spacy


stop_words = set(stopwords.words('english')) #from nltk
lang_data = spacy.load('en_core_web_sm') #nlp english data model

def removeStopWords(sentence):
	filtered_sentence = " ".join(filter(lambda word: word not in stop_words, sentence.split()))
	return filtered_sentence

def getPosTag(sentence):
	text = word_tokenize(sentence)
	tags = nltk.pos_tag(text)
	return tags

def getWordsOfInterest(tags):
	woi = []
	for (word, tag) in tags:
		if tag.startswith("J") or tag.startswith("R") or tag.startswith("V") or tag.startswith("N"):
			woi.append(word)
	return woi

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

#lemmatisation starts here
def nltk_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

lemmatizer = WordNetLemmatizer()
def lemmatize(sentence):
    nltk_tagged = getPosTag(sentence)
    wordnet_tagged = map(lambda x: (x[0], nltk_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            lemmatized_sentence.append(word)
        else:
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

def calculateSimilarity(sentence1,sentence2):
	lemmatized_sentence2 = lemmatizer.lemmatize(sentence2) #pre-processing generated sentence
	sentence2_filtered = removeStopWords(lemmatized_sentence2)
	# similarity_score = lang_data(sentence1).similarity(lang_data(sentence2))
	similarity_score_f = lang_data(sentence1).similarity(lang_data(sentence2_filtered))
	return similarity_score_f #,similarity_score


def nlp(dataset):
	df = dataset   #need to handle different file formats.
	# df = pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist()
	newDatasetList = []
	no_of_generated_sentences=0
	total_score = 0
	all_sentence_score = {}
	for sentence in datasetList:
		sentenceFiltered = removeStopWords(sentence)
		tag = getPosTag(sentenceFiltered)
		woi = getWordsOfInterest(tag)
		synonym_dict = {}
		for word in woi:
			synonyms = getSynonyms(word)
			synonym_dict[word] = list(set(synonyms))

		no_of_words_to_be_replaced = len(woi) #flag to set how many words need to be replaced
		generated_sentences=[]
		
		if no_of_words_to_be_replaced <=len(woi):
			for i in range(0,no_of_words_to_be_replaced):
				for syn in list(synonym_dict.values())[i]:

					generated_sentence = sentence.replace(list(synonym_dict.keys())[i], syn)
					no_of_generated_sentences = no_of_generated_sentences + 1
					score = calculateSimilarity(sentenceFiltered,generated_sentence)
					all_sentence_score[generated_sentence]=score # dictionary to map sentence to score
					total_score = total_score + score

		try:
			average = total_score/no_of_generated_sentences
		except Exception as e:
			average = 0
		for sentence,score in all_sentence_score.items():
			if score >=average: #filtering out only sentences with score above average
				generated_sentences.append(sentence)
		all_sentence_score.clear() #flushing out dictionary after sentences generated for each sentence in dataframe
		
		newDatasetList.extend(generated_sentences)

	return newDatasetList		

		

def nlp_test():
	# df = pd.read_csv(filePath,sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	data = ["number","two"]
	df= pd.DataFrame(data, columns=['Sentences'])
	datasetList = df.iloc[:,0].values.tolist() #first column of data frame i.e. all sentences

	# get list of synonyms for each word in filtered sentence
	no_of_generated_sentences=0
	total_score = 0
	all_sentence_score = {}
	for sentence in datasetList:
		print("Original Sentence: ", sentence)
		sentenceFiltered = removeStopWords(sentence)
		print("filtered sentence: ", sentenceFiltered)
		tag = getPosTag(sentenceFiltered)
		print("tags: ", tag)
		woi = getWordsOfInterest(tag)
		print("woi: ", woi)
		synonym_dict = {}
		for word in woi:
			synonyms = getSynonyms(word)
			synonym_dict[word] = list(set(synonyms))
		print(synonym_dict)

		print("no of woi: ", len(woi))
		no_of_words_to_be_replaced = len(woi) #flag to set how many words need to be replaced
		generated_sentences=[]
		if no_of_words_to_be_replaced <=len(woi):
			for i in range(0,no_of_words_to_be_replaced):
				for syn in list(synonym_dict.values())[i]:
					generated_sentence = sentence.replace(list(synonym_dict.keys())[i], syn)
					no_of_generated_sentences = no_of_generated_sentences + 1
					score = calculateSimilarity(sentenceFiltered,generated_sentence)
					all_sentence_score[generated_sentence]=score # dictionary to map sentence to score
					total_score = total_score + score
		try:
			average = total_score/no_of_generated_sentences
		except Exception as e:
			average = 0
		for sentence,score in all_sentence_score.items():
			if score >=average: #filtering out only sentences with score above average
				generated_sentences.append(sentence)
		all_sentence_score.clear() #flushing out dictionary after sentences generated for each sentence in dataframe
		print(generated_sentences)
		# print(dict(sorted(all_sentence_score.items(), key=operator.itemgetter(1), reverse=True)[:5]))
		# return generated_sentences

#nlp_test()

# https://nlpforhackers.io/wordnet-sentence-similarity/