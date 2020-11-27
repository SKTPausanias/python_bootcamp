import pandas as pd

class FileLoader():
	def load(self, path):
		df = pd.read_csv(path)
		print("Loading dataset of dimensions " + "{} x {}".format(df.shape[0], df.shape[1]))
		return df
	
	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		elif n < 0:
			print(df.tail(-n))



def main():
	loader = FileLoader()
	data = loader.load("../resources/athlete_events.csv")
	loader.display(data, 12)
	loader.display(data, -5)

if __name__ == "__main__":
    main()