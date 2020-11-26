import pandas as pd

class FileLoader():
	def load(self, path):
		df = pd.read_csv(path)
		print(print("Loading dataset of dimensions " + "{} x {}".format(df.shape[0], df.shape[1])))
	
	#def display(self, df, n):
