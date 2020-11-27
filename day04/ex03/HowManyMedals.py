from FileLoader import FileLoader
import pandas as pd

def howManyMedals(df, name):
	medals = df.loc[df.Name == name, ['Year', 'Medal']]
	ret = {}
	for _, row in medals.iterrows():
		ret[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
	for _, row in medals.iterrows():
		if row['Medal'] == 'Gold':
			ret[row['Year']]['G'] += 1
		elif row['Medal'] == 'Silver':
			ret[row['Year']]['S'] += 1
		elif row['Medal'] == 'Bronze':
			ret[row['Year']]['B'] += 1
	return ret

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("../resources/athlete_events.csv")
	print(howManyMedals(df, 'Kjetil Andr Aamodt'))