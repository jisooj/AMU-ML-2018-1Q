from CarInfo import CarInfo, Feature

class DecisionTree:
   class Node:
      """
      NOTE: Use named parameter when consctructing leaf nodes
      
      leaf = Node(dataset, predictedLabel=decision)
      nonLeaf = Node(dataset, left, right)
      """
      def __init__(self, dataset, left=None, right=None, feature=None, predictedLabel=None):
         self.dataset = dataset
         self.left = left
         self.right = right
         self.feature = feature
         self.predictedLabel = predictedLabel

      def isLeaf(self):
         return self.left == None and self.right == None

   def __init_(self, dataset, features):
      self.root = None
      self.dataset = dataset
      self.features = features

   # Returns a tuple (guess, ambiguity) where:
   # - guess: most frequent label found in the given datset
   # - ambiguity: compares the number of negative and positive
   # examples and is True if results are ambiguous and returns
   # False otherwise. Ambiguous means that the ratio isn't N:0 or 0:N
   def getDatasetInfo(self, dataset):
      negativeCount, positiveCount = self.splitExamples(dataset)
      ambiguity = (positiveCount != 0 and negativeCount != 0)
      guess = 0
      if (negativeCount < positiveCount):
         guess = 1
      return (guess, ambiguity)

   # Returns majority count for negative/positive examples
   def getMajorityVote(self, dataset):
      negativeCount, positiveCount = self.splitExamples(dataset)
      return max(positiveCount, negativeCount)

   # Returns count for both negative/positive examples
   def splitExamples(self, dataset):
      negativeCount = 0
      positiveCount = 0
      for carInfo in dataset:
         if carInfo.label == 1:
            positiveCount += 1
         else:
            negativeCount += 1
      return (negativeCount, positiveCount)

   # Core training algorithm that build up decision tree.
   # Params:
   # - dataset: list of CarInfo with mix of positive/negative examples
   # - features: array of features, each of which is a function that 
   # decides how to split the given dataset
   def decisionTreeTrain(self):
      self.root = self.decisionTreeTrain(self.dataset, self.features)

   def decisionTreeTrainHelper(self, dataset, features):
      # most frequent answer in dataset
      guess, ambiguity = self.getDatasetInfo(dataset)
      if (not ambiguity) or (len(features) == 0):
         # using named parameter
         return Node(dataset, predictedLabel=guess)
      else:
         bestFeature = None
         maxScore = 0
         for feature in features:
            noSet, yesSet = feature.split(dataset)
            score = len(self.getMajorityVote(noSet)) + \
                  len(self.getMajorityVote(yesSet))
            if score > maxScore:
               maxScore = score
               bestFeature = feature
         noSet, yesSet = bestFeature.split(dataset)
         # TODO: test remove funciton for custom class
         features.remove(bestFeature)
         left = self.decisionTreeTrainHelper(noSet, features)
         right = self.decisionTreeTrainHelper(yesSet, features)
         return Node(dataset, left, right)

   # Predicts whether a car has an efficient mpg based on the given carInfo
   # Returns 1 if efficient and returns 0 otherwise 
   def decisionTreeTest(self, carInfo):
      return self.decisionTreeTest(self.root, carInfo)

   def decisionTreeTestHelper(self, root, carInfo):
      if root.isLeaf():
         return root.predictedLabel
      if root.feature.getFeatureValue(carInfo) == 0:
         return self.decisionTreeTestHelper(root.left, carInfo)
      else:
         return self.decisionTreeTestHelper(root.right, carInfo)
