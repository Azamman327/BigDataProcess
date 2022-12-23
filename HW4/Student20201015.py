#!/usr/bin/python3

import numpy as np
import operator
from pathlib import Path
import sys

def createDataSet(filePath):
	fileNames = []
	for file in Path(filePath).iterdir():
		fileNames.append(str(file))	
	
	labels = []
	for v in fileNames:
		temp = v.split('/')
		labelName = temp[1][0]
		#print(temp[1], labelName)
		labels.append(labelName)

	data = []
	line = []
	for i in range(0, len(fileNames)):
		group = []
		file = open(fileNames[i], "r")
		content = file.read()
		for w in content:
			if (w != '\n'):
				group.append(int(w))
		data.append(group)
	#print(data)
	dataList = np.array(data)

	file.close()
	return dataList, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	#print(diffMat)
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5	
	#print(distances)
	sortedDistIndicies = distances.argsort()
	#print(sortedDistIndicies)
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	#print(classCount)
	sortedClassCount = sorted(classCount.items(),
		key = operator.itemgetter(1), reverse = True)
	#print(sortedClassCount)
	return sortedClassCount[0][0]

filePath = str(sys.argv[1])
traindata, trainLabels = createDataSet(filePath)
#print(traindata[0])
#print(trainLabels)

for k in range(1, 21):
	fileLength = 0
	dirPath = str(sys.argv[2])
	data = []

	errorCount = 0
	for file in Path(dirPath).iterdir():
		fileLength += 1
		fileName = str(file)
		strSplit = fileName.split('_')
		testLabels = strSplit[0][-1]
		#print(strSplit, strSplit[0][-1])
		
		f = open(file, "r")
		content = f.read()
		group = []
		for w in content:
			if (w != '\n'):
				group.append(int(w))
		inX = np.array(group)
		#print(inX)
		rslt = classify0(inX, traindata, trainLabels, k)
		
		#print(testLabels, rslt, testLabels[-1] == rslt)
		if (testLabels != rslt):
			errorCount += 1	
	#print(errorCount)
	errorRate = errorCount / fileLength * 100
	print(int(errorRate))		
