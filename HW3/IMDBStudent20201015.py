#!/usr/bin/python3

dic = {}

f = open("movies.dat")

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
for k, v in dic.items():
	print(k, v)
