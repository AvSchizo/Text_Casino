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
		}
	


	def addStack(self, type, value, pID):

		if type in self.stacks.keys():
			self.stacks[type].append(cp["afunc"]["stackClass"](value, pID, type))

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
					# print(f"{s.type}, ${s.value}")
		return ao

cp["afunc"]["playerClass"] = playerClass




def breakStacks(wanted, ID):

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
			print("Bets on the board:")
			for key in cp["board"].stacks.keys():
				print(key, end=":")
				for s in cp["board"].stacks[key]:
					print(f" [${s.value}; ID={s.id}]", end="")
				print()
			
			print()
			print(f"Player ID: {p.id}")
			print(f"Player money: {p.money}")
			#
			
			pin = input("New bet: ")
			if pin == "STOP":
				pass
			else:
				for s in cp["afunc"]["breakStacks"](pin):
					cp["board"].addStack(s[0], s[1], p.id)

			prop = p.getBets(cp["board"])

			if len(prop) > 0:
				cp["afunc"]["next"]()
		

		# rolling
		rolls = []
		for i in range(2):
			rolls.append(random.randint(1,6))
		result = 0
		for i in range(2):
			result += rolls[i]
		
		
		# givin out
		if cp["point"] == None:

			if result == 7 or result == 11:
				pass

cp["mainLoop"] = mainLoop







if __name__ != "__main__":
	quit()
cp["mainLoop"]()
