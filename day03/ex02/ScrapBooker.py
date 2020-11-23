from ImageProcessor import ImageProcessor
import numpy as np

class ScrapBooker():
	def crop(self, array, dimensions, position=(0,0)):
		if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
			print("Dimensions out of range")
			return array
		return np.array(array[position[0]:position[0] + dimensions[0], position[1]:position[1] +  dimensions[1]])
	
	def thin(self, array, n, axis):
		return np.delete(array, np.s_[::n], axis)
	
	def juxtapose(self, array, n, axis):
		tmp = array.copy()
		for _ in range(n):
			array = np.concatenate((array, tmp), axis)
		return array
	
	def mosaic(self, array, dimensions):
		tmp = array.copy()
		for _ in range(dimensions[0]):
			array = np.concatenate((array, tmp), 0)
		tmp = array.copy()
		for _ in range(dimensions[1]):
			array = np.concatenate((array, tmp), 1)		
		return array	

def main():
    img = ImageProcessor()
    slic = ScrapBooker()
    array = img.load("../assets/blue.png")
    retArray = slic.crop(array, (200, 100))
    img.display(retArray)
    retArray = slic.thin(array, 4, 0)
    img.display(retArray)
    retArray = slic.juxtapose(array, 2, 0)
    img.display(retArray)
    retArray = slic.mosaic(array, (10, 4))
    img.display(retArray)

if __name__ == "__main__":
    main()