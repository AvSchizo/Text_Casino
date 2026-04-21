import random
import math
import time


def turn(column):
	column.append(column.pop(0))

def turnAll(colms, ref):

	for i in range(3):
		turn(colms[ref[i]])


def showMachine(ref):
	for i in range(3):
		print(f"\t[{cC[ref[0]][i-1]}] [{cC[ref[1]][i-1]}] [{cC[ref[2]][i-1]}]")


c = ["column1", "column2", "column3"]

cC = {}
for i in range(3):
	cC[c[i]] = []
	for e in range(9):
		cC[c[i]].append(e+1)




showMachine(c)


for i in range(15):
	time.sleep(.1)
	turnAll(cC, c)

	print("\033[3F", end="")
	showMachine(c)