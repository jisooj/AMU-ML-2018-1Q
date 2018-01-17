"""" 
Car Efficiency Predictor 

From a car info that contains attributes 2-8 (except for MPG) we want to predict 
whether the car has an efficient MPG. For now, efficient MPG is MPG > avg(MPG)

"""

import csv
from CarInfo import CarInfo, Feature

class CarDataProcessor:
   def __init__(self):
      self.dataset = []

   # Reads auto-mpg data and prepares training dataset where each element
   # contains a car infomation about a single car
   # Also labels training dataset
   def processFile(self):
      with open('auto-mpg.data', 'r') as csvfile:
         reader = csv.reader(csvfile, delimiter='\n')
         lineCount = 0
         avgMPG = 0
         for row in reader:
            # def __init__(self, cylinders, displacement, horsepower, weight, acceleration, modelYear, origin):
            col = row[0].split()
            avgMPG += int(float(col[0]))
            info = CarInfo(col[1], col[2], col[3], col[4], col[5], col[6], col[7])
            lineCount += 1
            self.dataset.append(info)

         # Find average MPG used to label data
         avgMPG = avgMPG / lineCount
         # label training data 
         for info in dataset:
            if info.mpg > avgMPG
               info.label = 1


def main():
   processor = CarDataProcessor()
   processor.processFile()
   features = [] # need to put in functions that will be used in training
   tree = DecisionTree(processor.dataset, features)
   # Don't train with 100% of dataset. Try maybe 80% and use remainder as testing units
   tree.decisionTreeTrain()

   # Then do some prediction with unseen car info. 
   # Fill args with appropriate types
   # carInfo = CarInfo("arg1", "arg2", "arg3", "arg4", "arg5", "arg6", "arg7")
   # tree.decisionTreeTest(carInfo)

if __name__ == "__main__":
   main()