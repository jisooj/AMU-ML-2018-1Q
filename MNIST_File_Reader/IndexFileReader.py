class IndexFileReader:
   """
   train-images.idx3-ubyte: training set images 
   train-labels.idx1-ubyte: training set labels 
   t10k-images.idx3-ubyte:  test set images 
   t10k-labels.idx1-ubyte:  test set labels
   """
   def __init__(self, fileName):
      self.dataset = []
      self.dimensions = []
      self.fileName = fileName

   # reads through the specified index file passed in the constructor.
   # then populates dataset and dimensions as defined in MNIST website
   def readFile(self):
      with open(self.fileName, 'rb') as f:
         magicNumber = self.byteArrayToInt(f.read(4))
         dataSize, numDimensions = self.processMagicNumber(magicNumber)
         if dataSize == 0:
            exit("The given file is using an unsupported data type")
         
         self.dimensions = []
         for i in range(0, numDimensions):
            dim = self.byteArrayToInt(f.read(4))
            self.dimensions.append(dim)

         numItems, singleItemSize = self.getItemMetaData(self.dimensions)

         self.dataset = []
         item = []
         for i in range(0, numItems * singleItemSize):
            item.append(self.byteArrayToInt(f.read(1)))
            if (i + 1) % singleItemSize == 0:
               self.dataset.append(item)
               item = []

         print("singleItemSize = " + str(singleItemSize))
         print("dataset length = " + str(len(self.dataset)))
         print("item length = " + str(len(item)))
         print("DONE")

   """
   magic number format where MSB is first. 
   First byte that read() returns is 00

   0x00000801 means

   Byte 1: always 0 
   Byte 2: always 0
   Byte 3: describes the type of the data
      0x08: unsigned byte 
      0x09: signed byte 
      0x0B: short (2 bytes) 
      0x0C: int (4 bytes) 
      0x0D: float (4 bytes) 
      0x0E: double (8 bytes)
   Byte 4: number of dimensions
   """
   def byteArrayToInt(self, byteArray):
      x = 0
      for byte in byteArray:
         x = (x << 8) | byte
      return x

   def processMagicNumber(self, magicNumber):
      dataType = (magicNumber >> 8) & 0xFF
      numDimensions = magicNumber & 0xFF
      dataSize = 0
      if dataType == 0x08 or dataType == 0x09:
         dataSize = 1
      elif dataType == 0x0B:
         dataSize = 2
      elif dataType == 0x0C or dataType == 0x0D:
         dataSize = 4
      elif dataType == 0x0E:
         dataSize = 8

      return (dataSize, numDimensions)

   # Takes in dimensions and returns a tuple (numItems, singleItemSize) where
   # numItems = total number of items in this file
   # singleItemSize = number of data points to represent a single item (image or label)
   def getItemMetaData(self, dimensions):
      singleItemSize = 1
      numItems = 0
      if len(dimensions) > 0:
         numItems = dimensions[0]
         for i in dimensions[1:]:
            singleItemSize *= i

      return (numItems, singleItemSize)


def main():
   reader = IndexFileReader("t10k-labels.idx1-ubyte")
   reader.readFile()
   print(reader.dataset)
   print(reader.dimensions)

if __name__ == "__main__":
   main()