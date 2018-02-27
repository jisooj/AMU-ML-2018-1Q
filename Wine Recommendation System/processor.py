"""
Scans 130k wine reviews and prints out the word frequencies
used throughout all the reviews
"""

import json
from pprint import pprint


def countWords(reviewCount):
	data = json.load(open('winemag-data-130k-v2.json'))
	vocabMap = {};
	punctuations = '-–—.,?!\'":;‘()“”’…`¬\r\n';
	filterTable = str.maketrans(dict.fromkeys(punctuations))
	# x = "\'a\'sd\' hi, my name's sam.!??ASdda"
	# print(x.translate(filterTable))

	for i in range(1, reviewCount + 1):
		printProgress(i, reviewCount)
		review = data[i]
		words = review["description"].translate(filterTable).upper().strip().split(" ")
		for word in words:
			if len(word) > 0:
				if word not in vocabMap:
					vocabMap[word] = 0
				vocabMap[word] += 1

	pprint(vocabMap)
	print(len(vocabMap))

def printProgress(i, reviewCount):
	if (i % int(reviewCount / 10) == 0):
		percentage = int(i / reviewCount * 100)
		print(f"{percentage}% : Processed {i} reviews...")



reviewCount = 50000
countWords(reviewCount)