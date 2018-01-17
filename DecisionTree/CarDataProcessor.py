"""" 
Car MPG program [our goal: if we input random attributes 2-8 (except for MPG), it would give us MPG 

1. Create labels -> group rows by mpg, each of which will be casted to int. aka create map<car_hash, mpg>
2. get data ready to construct decision tree
3. splitter to make labels???

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
