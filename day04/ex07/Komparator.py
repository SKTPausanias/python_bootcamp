from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator():
	def __init__(self, df: pd.DataFrame):
		self.df = df

	def compare_box_plots(self, categorical_var, numerical_var):
		'''
		Displays a series of box plots to compare how the distribution of the
		numerical variable changes if we only consider the subpopulation which
		belongs to each category. There should be as many box plots as categories.
		For example, with Sex and Height, we would compare the height distributions
		of men vs. women with two box plots.
		'''
		df = self.df[[categorical_var, numerical_var]].dropna()
		sns.boxplot(y=categorical_var, x=numerical_var, data=df, orient='h')
		plt.show()
	
	def density(self, categorical_var, numerical_var):
		'''
		Displays the density of the numerical variable. Each subpopulation should
		be represented by a separate curve on the graph.
		'''
		df = self.df[[categorical_var, numerical_var]].dropna()
		gb = df[categorical_var].drop_duplicates().to_list()
		df = df.groupby(categorical_var)
		for i, _ in enumerate(df):
			ax = df.get_group(gb[i])
			sns.distplot(ax[numerical_var], hist=False, kde=True, label=gb[i])
		plt.legend()
		plt.show()

	def compare_histograms(self, categorical_var, numerical_var):
		'''
		plots the numerical variable in a separate histogram for each category.
		As a bonus, you can use overlapping histograms with a color code
		'''
		df = self.df[[categorical_var, numerical_var]].dropna()
		gb = df[categorical_var].drop_duplicates().to_list()
		df = df.groupby(categorical_var)
		for i, _ in enumerate(df):
			ax = df.get_group(gb[i])
			plt.hist(ax[numerical_var], label=gb[i])
			#MyPlotLib.histogram(ax[numerical_var], numerical_var)
		plt.legend()
		plt.show()

if __name__ == "__main__":
	loader = FileLoader()
	df = loader.load("../resources/athlete_events.csv")
	kmp = Komparator(df)
	#kmp.compare_box_plots('City', 'Height')
	#kmp.density('Sex', 'Age')
	kmp.compare_histograms('Sport', 'Weight')
