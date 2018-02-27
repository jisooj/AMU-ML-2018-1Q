from IndexFileReader import IndexFileReader
from k_means import KMeansClusterer


"""
train-images.idx3-ubyte: training set images 
train-labels.idx1-ubyte: training set labels 
t10k-images.idx3-ubyte:  test set images 
t10k-labels.idx1-ubyte:  test set labels
"""
def main():
	"""
	IndexFileReader:
	self.dataset = []
	self.dimensions = []
	self.fileName = fileName
	"""
	trainingImagesReader = IndexFileReader("train-images.idx3-ubyte")
	trainingImagesReader.readFile()

	trainingLabelsReader = IndexFileReader("train-labels.idx1-ubyte")
	trainingLabelsReader.readFile()

	clusterer = KMeansClusterer()

if __name__ == "__main__":
   main()