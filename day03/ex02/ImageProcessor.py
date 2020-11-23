from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np

class ImageProcessor(object):
    
    def load(self, path):
        return mpimg.imread(path)
    
    def display(self, arr):
        plt.imshow(arr)
        plt.show()

if __name__ == "__main__":
    imp = ImageProcessor()
    data = imp.load("../assets/blue.png")
    imp.display(data)
