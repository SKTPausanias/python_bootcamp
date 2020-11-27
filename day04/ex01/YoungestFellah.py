from FileLoader import FileLoader
import pandas as pd

def youngestFellah(df, olimpicYear):
	fem = df['Age'].loc[df['Sex'] == 'F'].loc[df['Year'] == olimpicYear].min()
	mal = df['Age'].loc[df['Sex'] == 'M'].loc[df['Year'] == olimpicYear].min()
	return {'f': fem, 'm': mal}

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("../resources/athlete_events.csv")
	print(youngestFellah(data, 2004))
