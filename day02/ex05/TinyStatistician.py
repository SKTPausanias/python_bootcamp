import numpy as np

class TinyStatistician():
	def mean(self, x):
		if len(x) < 1:
			return None
		return (float(sum(x)) / len(x))
	
	def median(self, x):
		if len(x) < 1:
			return None
		n = len(x)
		x.sort()
		if n % 2 == 0:
			median1 = x[ n // 2]
			median2 = x[( n// 2) - 1]
			median = (median1 + median2) / 2.0
		else:
			median = float(x[n // 2])
		return median
	
	def quartiles(self, x, percentile):
		if len(x) < 1:
			return None
		x.sort()
		if percentile == 25:
			if len(x) % 2 == 0:
				return self.median(x[:(len(x)//2) - 1])
			else:
				return self.median(x[:(len(x)//2) + 1])
		elif percentile == 75:
			if len(x) % 2 == 0:
				return (self.median(x[len(x)//2:]))
			else:	
				return (self.median(x[len(x)//2:]))

	


if __name__ == "__main__":
	ts = TinyStatistician()
	arr = [1, 1, 8, 12, 13, 13, 14, 16, 19, 22, 27, 28, 31]
	#print(ts.median(arr))
	print(ts.quartiles(arr, 25))
	print(ts.quartiles(arr, 75))
	print()
	print(np.percentile(arr, 25))
	print(np.percentile(arr, 75))
