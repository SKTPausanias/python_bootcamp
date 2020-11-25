from copy import deepcopy
import numpy as np
import math
import random
import matplotlib.pyplot as plt
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
		plt.scatter(X[:,0], X[:,1], s=7)
		plt.scatter(self.centroids[:,0], self.centroids[:,1], marker='*', c='g', s=150)
		plt.show()
		#centers_old = np.zeros(self.centroids.shape) # to store old centers
		#centers_new = deepcopy(self.centroids)
		#error = np.linalg.norm(centers_new - centers_old)
		X.shape
		clusters = np.zeros(n)
		distances = np.zeros((n, self.ncentroid))
		for i in range(self.max_iter):
			for i in range(self.ncentroid):
				distances[:,i] = np.linalg.norm(X - self.centroids[i], axis=1)
			clusters = np.argmin(distances, axis = 1)
			#centers_old = deepcopy(centers_new)
			for i in range(self.ncentroid):
				self.centroids[i] = np.mean(X[clusters == i], axis=0)
			#error = np.linalg.norm(centers_new - centers_old)
			#if error == 0:
			#	break
		plt.scatter(X[:,0], X[:,1], s=7)
		plt.scatter(self.centroids[:,0], self.centroids[:,1], marker='*', c='g', s=150)
		plt.show()
	
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
		#planets = ['The flying cities of Venus', 'United Nations of Earth', 'Mars Republic', 'Asteroids Belt colonies']
		res = list(X.shape[0], 1)
		print(res)
		distances = np.zeros(self.ncentroid)
		print(distances)
		for i in range(X.shape[0]):
			min = 0
			for j in range(self.ncentroid):
				if ((np.linalg.norm(X[i] - self.centroids[j])) < (np.linalg.norm(X[i] - self.centroids[min]))):
					min = j
			np.append(X[i], float(min))
			print(X[i])
			print(min)
			

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
	k.predict(dataset)
	#print(k.predict(dataset))

if __name__ == "__main__":
    main()