
import denga.augment as au
import pandas as pd

class Genda():

	def __init__(self,filepath):  
		self.filepath = filepath
		self.dataset = None
		try:
			self.dataset = pd.read_csv(self.filepath, header= None, error_bad_lines=False)
		except:
			raise Exception("ERROR: File Missing") 
		self.data = None

	def generate(self):
		self.data = au.nlp(self.dataset)

	def save(self,filename="genda.txt"):
		if(self.data is None):
			raise Exception("ERROR: New Dataset not yet generated.")

		if not "." in filename:
			raise Exception("ERROR: extension missing from file name.")
		elif filename.endswith(".csv"):
			df = pd.DataFrame(self.data, columns=["New Sentences"])
			df.to_csv(filename, index=False)
		elif filename.endswith(".txt"):
			with open(filename, "w") as output:
				for line in self.data:
					output.write(str(line)+"\n")
		else:
			raise Exception("ERROR: file type not supported use .txt or .csv file name.") 	