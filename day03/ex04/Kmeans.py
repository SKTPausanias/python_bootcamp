from copy import deepcopy
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=4):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def euclidean_distance(self, a, b):
		return math.sqrt(sum(np.power(b - a, 2)))
	
	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
			None.
		Raises:
			This function should not raise any Exception.
		"""
		mean = np.mean(X, axis = 0)
		std = np.std(X, axis = 0)
		n = X.shape[0]
		c = X.shape[1]
		self.centroids = np.random.randn(self.ncentroid, c)*std + mean
		#plt.scatter(X[:,0], X[:,1], s=7)
		#plt.scatter(self.centroids[:,0], self.centroids[:,1], marker='*', c='g', s=150)
		#plt.show()
		#centers_old = np.zeros(self.centroids.shape) # to store old centers
		#centers_new = deepcopy(self.centroids)
		#error = np.linalg.norm(centers_new - centers_old)
		X.shape
		self.clusters = np.zeros(n)
		distances = np.zeros((n, self.ncentroid))
		for i in range(self.max_iter):
			for i in range(self.ncentroid):
				distances[:,i] = np.linalg.norm(X - self.centroids[i], axis=1)
			self.clusters = np.argmin(distances, axis = 1)
			#print(clusters)
			#centers_old = deepcopy(centers_new)
			for i in range(self.ncentroid):
				self.centroids[i] = np.mean(X[self.clusters == i], axis=0)
			#error = np.linalg.norm(centers_new - centers_old)
			#if error == 0:
			#	break
		self.table = np.zeros((X.shape[0], X.shape[1] + 1))
		self.table[:,:-1] = X
		self.table[:,3] = self.clusters
		#print(self.table)
		#plt.scatter(X[:,0], X[:,1], s=7)
		#plt.scatter(self.centroids[:,0], self.centroids[:,1], marker='*', c='g', s=150)
		#plt.show()
	
	def predict(self, X) -> np.ndarray:
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
			This function should not raise any Exception.
		"""
		#table = np.zeros((X.shape[0], X.shape[1] + 1))
		#table[:,:-1] = X
		#for i in range(X.shape[0]):
		#	min = 0
		#	for j in range(self.ncentroid):
		#		if ((np.linalg.norm(X[i] - self.centroids[j])) < (np.linalg.norm(X[i] - self.centroids[min]))):
		#			min = j
		#	table[i][3] = float(min)
		#print(table)
		y = [self.table[self.table[:,3]==k] for k in np.unique(self.table[:,3])]
		means = np.zeros((self.ncentroid, X.shape[1] + 1))
		i = 0
		for each in y:
			means[i] = each.mean(axis=0)
			i += 1
		means = means[means[:,0].argsort()]
		ret = np.chararray(shape=(X.shape[0], 1), itemsize=26)
		for i in range(X.shape[0]):
			if (self.table[i][3] == means[0][3]):
				ret[i] = "The flying cities of Venus"
			elif (self.table[i][3] == means[1][3]):
				ret[i] = "United Nations of Earth"
			elif (self.table[i][3] == means[2][3]):
				ret[i] = "Mars Republic"
			elif (self.table[i][3] == means[3][3]):
				ret[i] = "Asteroids Belt colonies"
		return ret

def main():
	f = open("../resources/solar_system_census.csv")
	k = KmeansClustering(max_iter=100)
	lines = f.readlines()
	data = []
	for i in range(len(lines)):
		data.append(lines[i].split(','))
	dataset = np.delete(np.array(data[1:], dtype='float'), 0, 1)
	dataset = dataset / np.linalg.norm(dataset, axis = 0)
	#print(dataset)
	#print(np.ndim(dataset))
	k.fit(dataset)
	#k.predict(dataset)
	print(k.predict(dataset))

	#colors = 10*["r", "g", "c", "b", "k"]
	#i = 0
	#for centroid in k.centroids:
	#	color = colors[i]
	#	plt.scatter(centroid[0], centroid[1], s = 130, color = color, marker = "x")
	#	i += 1
	#for i in range(k.table.shape[0]):
	#	color = colors[int(k.table[i][3])]
	#	plt.scatter(k.table[i][0], k.table[i][1], color = color,s = 30)
	#plt.show()
	colors = 10*["r", "g", "c", "b", "k"]
	fig=plt.figure()
	ax=Axes3D(fig)
	for i in range(k.table.shape[0]):
		color = colors[int(k.table[i][3])]
		ax.scatter(k.table[i][0],k.table[i][1],k.table[i][2], color = color)
	i = 0
	for centroid in k.centroids:
		color = colors[i]
		ax.scatter(centroid[0], centroid[1], centroid[2], s = 130 , color = color, marker = "x")
		i += 1
	plt.show()

if __name__ == "__main__":
    main()