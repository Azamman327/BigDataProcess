#!/usr/bin/python3
import sys

dic = {}
f = open(sys.argv[1])

for line in f:
	list = line.split("::")
	#print(list[2])
	gStr = list[2].replace("\n", "")
	#print(gStr, type(gStr))
	genre = gStr.split("|")
	#print(genre[1], type(genre))

	for v in genre:
		if v not in dic:
			dic[v] = 1
		else:
			dic[v] += 1
#print(dic)
wf = open(sys.argv[2], "wt")
for k, v in dic.items():
	wf.write(k + " " + str(v) + "\n")

f.close()
wf.close()
