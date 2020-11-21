from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np

class ImageProcessor(object):
    
    def load(self, path):
        return mpimg.imread(path)
    
    def display(self, arr):
        plt.imshow(arr)

if __name__ == "__main__":
    imp = ImageProcessor()
    data = imp.load("sm_5a1ad63f21109.png")
    imp.display(data)