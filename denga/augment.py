import pandas as pd



def getSynonym():
	#implementation needed
	#use nltk wordnet

	return synonym

def nlp(filePath):
	df = pd.read_csv(filePath,sep='\t',header= None, error_bad_lines=False)  #need to handle different file formats.
	datasetList = df.iloc[:,0].values.tolist()

	generatedDataset = [getSynonym(x) for x in datasetList]

	return generatedDataset



