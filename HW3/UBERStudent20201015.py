#!/usr/bin/python3
import sys
import calendar

rslt = []
dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
f = open(sys.argv[1])

for line in f:
	list = line.split(",")

	date = list[1].split("/")
	#print(date)
	day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
	#print(dayofweek[day])
	list[1] = day

	#list[3] = list[3].replace("\n", "")
	
	rslt.append(list)

rslt.sort()
#for value in list:
	

wf = open(sys.argv[2], "wt")
for uLine in rslt:
	wf.write(uLine[0] + "," + dayofweek[uLine[1]] + " " + uLine[2] + "," + uLine[3])
	#print(uLine[0] + "," + dayofweek[uLine[1]] + " " + uLine[2] + "," + uLine[3], end="")
f.close()
wf.close()
