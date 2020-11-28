from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib():
	@staticmethod
	def histogram(data: pd.DataFrame, features):
		data.hist(column=features, grid=False)
		plt.show()

	@staticmethod
	def density(data: pd.DataFrame, features: list):
		for feat in features:
			sns.distplot(data[feat], hist=False, kde=True,
						label=feat)
		plt.legend()
		plt.xlabel('')
		plt.show()
	
	@staticmethod
	def pair_plot(data: pd.DataFrame, features: list):
		pd.plotting.scatter_matrix(frame=data[features], grid=True, diagonal='hist')
		plt.show()

	@staticmethod
	def box_plot(data: pd.DataFrame, features: list):
		data.boxplot(column=features)
		plt.show()
	
if __name__ == "__main__":
	loader = FileLoader()
	mpl = MyPlotLib()
	df = loader.load("../resources/athlete_events.csv")
	mpl.histogram(df, ['Height', 'Weight'])
	mpl.density(df, ['Weight', 'Height'])
	mpl.pair_plot(df, ['Weight', 'Height'])
	mpl.box_plot(df, ['Weight', 'Height'])