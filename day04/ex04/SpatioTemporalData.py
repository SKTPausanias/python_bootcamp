from FileLoader import FileLoader
import pandas as pd

class SpatioTemporalData(object):
	def __init__(self, df: pd.DataFrame):
		self.df = df

	def when(self, location):
		year = self.df.loc[self.df['City'] == location]['Year'].drop_duplicates()
		return year.to_list()

	def where(self, date):
		city = self.df.loc[self.df['Year'] == date]['City'].drop_duplicates()
		return city.to_list()

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("../resources/athlete_events.csv")
	std = SpatioTemporalData(df)
	print(std.where(1896))
	print(std.where(2016))
	print(std.when('Athina'))
	print(std.when('Paris'))