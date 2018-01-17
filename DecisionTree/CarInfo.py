# CarInfo class which represents single car info with 7 diff attributes
class CarInfo:
   # Car info input file format:
   # 1. mpg:           continuous  <-- this one is going to be used as a label
   # 2. cylinders:     multi-valued discrete
   # 3. displacement:  continuous
   # 4. horsepower:    continuous
   # 5. weight:        continuous
   # 6. acceleration:  continuous
   # 7. model year:    multi-valued discrete
   # 8. origin:        multi-valued discrete
   # 
   # label: Does this car have an efficient mpg or not
   # Let's consider efficient (label = 1) if mpg is higher than average mpg
   # and inefficient (label = 0) otherwise
   def __init__(self, cylinders, displacement, horsepower, weight, acceleration, modelYear, origin):
      self.cylinders = cylinders
      self.displacement = displacement
      self.horsepower = horsepower
      self.weight = weight
      self.acceleration = acceleration
      self.modelYear = modelYear
      self.origin = origin
      self.label = 0

class Feature:
   # feature: function that takes car infos and allocates no/yes set
   def __init__(self, feature):
      self.feature = feature

   # apply feature in the current dataset and split into NO/YES set
   # Returns a tuple with (NO, YES) sets
   def split(self, carInfos):
      for info in carInfos:
         featureValue = self.getFeatureValue(info)
         # no boolean zen here. Just want to be explit
         if featureValue == 0:
            self.noSet.append(info)
         else:
            self.yesSet.append(info)
      return (noSet, yesSet)

   # returns 0 if the given carInfo goes to NO set
   # returns 1 otherwise
   def getFeatureValue(self, carInfo):
      return self.feature(carInfo)
