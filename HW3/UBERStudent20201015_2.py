#!/usr/bin/python3
import sys
import calendar

rslt = {}
dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
f = open(sys.argv[1])

for line in f:
	list = line.split(",")

	date = list[1].split("/")
	#print(date)
	day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
	#print(dayofweek[day])
	list[1] = dayofweek[day]

	list[3] = list[3].replace("\n", "")
	
	key = (list[0] + "," + list[1])
	print(key)
	rslt[key] = (list[2] + "," + list[3])
	print(rslt[key])
print(rslt)
wf = open(sys.argv[2], "wt")
for k, v in rslt.items():
	wf.write(k + " " + v)
	wf.write("\n")

f.close()
wf.close()
