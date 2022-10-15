#!/usr/bin/python3
from openpyxl import load_workbook 

import numpy as np

wb = load_workbook(filename = 'student.xlsx')
ws = wb['Sheet1']

r = 1
data = []
for row in ws:
	sum = 0.0
	if r != 1:
		sum += ws.cell(row = r, column = 3).value * 0.3
		sum += ws.cell(row = r, column = 4).value * 0.35
		sum += ws.cell(row = r, column = 5).value * 0.34
		sum += ws.cell(row = r, column = 6).value
		ws.cell(row = r, column = 7, value = sum)

		data.append(ws.cell(row = r, column = 7).value)
	r += 1

#r = 1
#data = []
#for row in ws:
#	if r != 1:
#		data.append(ws.cell(row = r, column = 7).value)
#		#print(data)
#	r += 1
lst = np.array(data)
a = np.quantile(lst, 0.7)
b = np.quantile(lst, 0.3)

aLst = []
bLst = []
cLst = []
for v in data:
	if v > a:
		aLst.append(v)
	elif v > b:
		bLst.append(v)
	else:
		cLst.append(v)

aPlusCut = np.quantile(aLst, 0.5)
bPlusCut = np.quantile(bLst, 0.5)
cPlusCut = np.quantile(cLst, 0.5)

r = 1
for row in ws:
	score = ws.cell(row = r, column = 7).value
	if r != 1:
		if score > aPlusCut:
			ws.cell(row = r, column = 8, value = "A+")
		elif score >= a:
			ws.cell(row = r, column = 8, value = "A0")
		elif score > bPlusCut:
			ws.cell(row = r, column = 8, value = "B+")
		elif score >= b:
			ws.cell(row = r, column = 8, value = "B0")
		elif score > cPlusCut:
			ws.cell(row = r, column = 8, value = "C+")
		else:
			ws.cell(row = r, column = 8, value = "C0")
	r += 1

wb.save("student.xlsx")
		

