from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter(object):

	@staticmethod
	def invert(array):
		array[:, :, :3] = 1.0 - array[:, :, :3]
		return array

	def to_blue(self, array):
		array[..., 0] = 0
		array[..., 1] = 0
		return array

	def to_green(self, array):
		array[..., 0] = 0
		array[..., 2] = 0
		return array

	def to_red(self, array):
		array[..., 1] = 0
		array[..., 2] = 0
		return array
	
	def shade(self, a, b):
		return b * int(a / b)

	def to_celluloid(self, array):
		vfunc = np.vectorize(self.shade)
		for i in np.linspace(0.75, 0.78, num=4):
			array[:, :, :3] = vfunc(array[:, :, :3], (1.0 - i))
		return array



def main():
	img = ImageProcessor()
	cf = ColorFilter()
	array = img.load("../assets/img.png")
	img.display(array)
	img.display(ColorFilter.invert(array))
	array = img.load("../assets/img.png")
	img.display(cf.to_blue(array))
	array = img.load("../assets/img.png")
	img.display(cf.to_green(array))
	array = img.load("../assets/img.png")
	img.display(cf.to_red(array))
	array = img.load("../assets/img.png")
	img.display(cf.to_celluloid(array))



if __name__ == "__main__":
    main()