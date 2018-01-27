from random import *
import numpy as np


class KMeansClusterer:
   IMG_HEIGHT = 28
   IMG_WIDTH = 28

   def __init__(self, dataset, k):
      self.dataset = dataset
      self.k = k

   # 1. Initialize k starting centers by randomly 
   # choosing k points from your data set. You should
   # implement this in the initialize function
   def initialize(self):
      centerPoints = []
      for i in range(0, self.k):
         randIndex = randint(0, len(self.dataset) - 1)
         randDataPoint = self.dataset[randIndex]
         centerPoints.append(randDataPoint)
      return centerPoints

   # 2. Assign each data point to the cluster associated 
   # with the nearest of the k center points. 
   # Implement this by filling in the assign function
   def assign(self, centerPoints):
      groups = {} # dict()
      for point in self.dataset: 
         k = self.getKValue(point, centerPoints)
         if k not in groups:
            groups[k] = []
         groups[k].append(point)
      return groups

   def getKValue(self, point, centerPoints):
      minDist = float('inf')
      k = 0
      for i in len(centerPoints):
         dist = self.dist(point, centerPoints[i])
         if dist < minDist:
            minDist = dist
            k = i
      return k

   def dist(self, x1, x2):
      if len(x1) != len(x2):
         return -1
      sqSum = 0
      for i in range(0, len(x1)):
         diff = x1[i] - x2[i]
         sqSum += math.pow(diff, 2)
      return math.sqrt(sqsum)


   # 3. Re-calculate the centers as the mean vector of each cluster from (2). 
   # Implement this by filling in the update function
   def update(self, groups):
      newCenterPoints = []
      for k in groups:
         newCenterPoints.append(self.getMeanVector(groups[k]))
      return newCenterPoints

   def getMeanVector(self, group):
      # 28*28 by 1 column vector
      meanVector = np.zeros((IMG_WIDTH * IMG_HEIGHT, 1))
      for point in group:
         meanVector = np.add(meanVector, point)
      return meanVector / len(group)


   # 4. Repeat steps (2) and (3) until convergence. 
   # This wrapping is already done for you in the loop
   # function, which lives inside the cluster function.
   # def loop():
   def cluster(self):
      currentCenterPoints = self.initialize()
      epsilon = 0.000001
      distDiff = epsilon * 10
      while (distDiff > epsilon):
         groups = self.assign(self.dataset, currentCenterPoints)
         newCenterPoints = self.update(groups)
         distDiff = self.dist(self.currentCenterPoints, newCenterPoints)
         currentCenterPoints = newCenterPoints

      return currentCenterPoints