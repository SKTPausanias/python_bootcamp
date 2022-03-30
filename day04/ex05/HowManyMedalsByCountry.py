from FileLoader import FileLoader

def howManyMedalsByCountry(df, country_name):
	country = df.loc[df['Team'] == country_name]
	ret = {}
	for _, row in country.iterrows():
		ret[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
	for _, row in country.iterrows():
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
	print(howManyMedalsByCountry(df, 'China'))