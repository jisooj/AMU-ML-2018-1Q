import json
from pprint import pprint

# data = json.load(open('data.json'))

# pprint(data)

# pprint(data["maps"])
# pprint(data["masks"])


data = json.load(open('winemag-data-130k-v2.json'))
vocabMap = {};
for i in range(1,100000):
	review = data[i]
	description = review["description"].replace(",", "").replace(".", "").upper().strip().split(" ")
	for word in description:
		if word not in vocabMap:
			vocabMap[word] = 0
		vocabMap[word] += 1

pprint(vocabMap)
print(len(vocabMap))

