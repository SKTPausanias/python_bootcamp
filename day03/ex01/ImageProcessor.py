from matplotlib import image as mpimg
from matplotlib import pyplot as plt

class ImageProcessor(object):
    
    def load(self, path):
        return mpimg.imread(path)
    
    def display(self, arr):
        plt.imshow(arr)

if __name__ == "__main__":
    imp = ImageProcessor()
    data = imp.load("../resources/42AI.png")
    print(data)
    imp.display(data)
    plt.show()