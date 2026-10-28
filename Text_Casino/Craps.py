import random
from time import sleep

cp = {
	"afunc": {},
	"stacks": [],
	"players": [],
	"point": None,
	"startingPlayers": [
		# person controlled
		1,
		# com
		4,
	],
	"placeNames": [
		[
			"pass bar",
			"no pass bar",
		],
		[
			"Pass Bar",
			"Don't Pass Bar",
		]
	],
}



def next(fax=False):
	input("PRESS ENTER TO CONTINUE")
	if fax:
		print()

cp["afunc"]["next"] = next




class stackClass():

	def __init__(self, inValue, inID, inPlace):
		
		self.value = inValue
		self.id = inID
		self.place = inPlace

cp["afunc"]["stackClass"] = stackClass




class boardClass():

	def __init__(self):
		
		self.stacks = {
			"pass bar": [],
			"no pass bar": [],
			"come": [],
			"no come": [],
		}
	


	def addStack(self, type, value, pID, taking=True):

		if type in self.stacks.keys():
			self.stacks[type].append(cp["afunc"]["stackClass"](value, pID, type))
			if taking:
				cp["players"][pID].money -= value

cp["afunc"]["boardClass"] = boardClass




class playerClass():

	def __init__(self, inID, inMoney=1000, inControlled=False):
		
		self.id = inID

		self.money = inMoney

		# true if person, false if bot
		self.playerControlled = inControlled
	


	def getBets(self, board):

		ao = []
		for l in [board.stacks[key] for key in board.stacks.keys()]:
			for s in l:
				if s.id == self.id:
					ao.append(s)
					# print(f"{s.place}, ${s.value}")
		return ao

cp["afunc"]["playerClass"] = playerClass




def breakStacks(wanted):

	wantSect = wanted.split(";")

	data = []
	for each in wantSect:
		swatch = each.split(",")
		eek = [
			swatch[0],
			int(swatch[1]),
		]
		data.append(eek)
	
	return data

cp["afunc"]["breakStacks"] = breakStacks



def returnToPlayer(stack):

	for p in cp["players"]:

		if p.id == stack.id:
			p.money += stack.value





def mainLoop():

	# setup
	cp["board"] = cp["afunc"]["boardClass"]()

	for i in range(cp["startingPlayers"][0]+cp["startingPlayers"][1]):
		startingID = 0
		while True:
			for e in cp["players"]:
				if e.id == startingID:
					startingID += 1
					continue
			break
		if len(cp["players"]) < cp["startingPlayers"][0]:
			pc = True
		else:
			pc = False
		cp["players"].append(cp["afunc"]["playerClass"](inID=startingID, inControlled=pc))
	
	
	# non setup
	while True:

		for p in cp["players"]:
			if not p.playerControlled:
				continue
			
			# UI
			## printing player bets
			print("Your bets:")
			playerBets = p.getBets(cp["board"])

			printingPlace = {}
			for key in cp["board"].stacks.keys():
				printingPlace[key] = "None"

			for b in playerBets:
				a = b.place
				v = b.value
				if printingPlace[a] == "None":
					printingPlace[a] = ""
				else:
					printingPlace[a] += ", "
				printingPlace[a] += str(v)

			for e in printingPlace.keys():
				print(f"{e}: {printingPlace[e]}")
			
			# if len(playerBets) == 0:
			# 	print("None")
			# else:
			# 	for s in playerBets:
			# 		print(f"{s.place}, ${s.value}")


			
			print()
			print(f"Player ID: {p.id}")
			print(f"Player money: {p.money}")
			#
			
			pin = input("New bet: ")
			if pin == "none":
				pass
			else:
				# adding bets
				for s in cp["afunc"]["breakStacks"](pin):
					if p.money >= s[1]:
						cp["board"].addStack(s[0], s[1], p.id)


		print()
		

		# rolling
		rolls = []
		for i in range(2):
			rolls.append(random.randint(1,6))
		result = 0
		for i in range(2):
			result += rolls[i]
		print(f"Rolled {result}")
		next(True)
		

		# deciding what to

		winCause = {
			"pass bar": 1,
			"no pass bar": -1,
		}

		loseCause = {
			"pass bar": -1,
			"no pass bar": 1,
		}

		snaple = {}
		if cp["point"] == None:

			if result == 7 or result == 11:
				snaple = winCause

			elif result in [2, 3, 12]:
				snaple = loseCause

			else:
				cp["point"] = result

		else:

			if result in [7, 11]:
				if result == 7:
					result = loseCause
				result["come"] = 1
				result["no come"] = -1


		# givin out
		for key in snaple.keys():
			for i, s in enumerate(cp["board"].stacks[key]):

				if snaple[key] == 1:
					returnStack = s
					returnStack.value *= 2
					returnToPlayer(returnStack)
					cp["board"].stacks[key].pop(0)

				elif snaple[key] == -1:
					cp["board"].stacks[key].pop(0)


cp["mainLoop"] = mainLoop







if __name__ != "__main__":
	quit()
cp["mainLoop"]()
