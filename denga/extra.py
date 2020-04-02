def nlp(filePath):
	df = pd.read_csv(filePath, sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	# df = pd.DataFrame(data, columns=['Sentences'])
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