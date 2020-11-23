from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter(object):

	@staticmethod
	def invert(array):
		array[:, :, :3] = 1.0 - array[:, :, :3]
		return array

	@staticmethod
	def to_blue(array):
		array[..., 0] = 0
		array[..., 1] = 0
		return array

	@staticmethod
	def to_green(array):
		array[..., 0] = 0
		array[..., 2] = 0
		return array

	@staticmethod
	def to_red(array):
		array[..., 1] = 0
		array[..., 2] = 0
		return array
	
	@staticmethod
	def to_celluloid(array):
		return array



def main():
	img = ImageProcessor()
	array = img.load("../assets/img.png")
	img.display(array)
	img.display(ColorFilter.invert(array))
	array = img.load("../assets/img.png")
	img.display(ColorFilter.to_blue(array))
	array = img.load("../assets/img.png")
	img.display(ColorFilter.to_green(array))
	array = img.load("../assets/img.png")
	img.display(ColorFilter.to_red(array))



if __name__ == "__main__":
    main()