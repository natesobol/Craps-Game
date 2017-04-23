# Programmer: Nate Sobol
# Last Modified: 4/15/17
# Title: Craps Game

#Import Random for dice
import random

#Declarations
MINVAL = 1
MAXVAL = 6
remainingFunds = 0
winAmount= 0
loseAmount= 0
choice = ''
playerPoint=0
name = ''

# Function Definitions
def createPlayer():
	players = {}
	infile = open(r'players.txt', 'r')
	#allows 5 records
	try:
		readL = infile.readline()
		while readL != '':
			readL=readL.rstrip()
			L = readL.split('|')
			for i in L:
				players[L.pop()] = (L.pop(),L.pop(),L.pop())
			readL = infile.readline()

	finally:
		infile.close()
	return players


	
def printPlayerStatistics(remainingFunds, player, winAmount, loseAmount):
	print('Player:   ' + player)
	print('Funds:  $ %.2f' % (funds))
	print('Wins:     %d'% wins)
	print('Loses:    %d'% loses)

def rollDice():
	roll = ''
	while roll != 'R' and roll != 'r':
		roll = input('Press \'R\' or \'r\' to roll dice: ')
		if roll == 'R' or roll == 'r':
			return roll
		else:
			print('invalid command')

def getValidatedQuit():
	correctInput = 'false'
	inKey = ''
	while correctInput == 'false':
		inKey = input('Really want to quit? (Y = yes, N = no): ')
		if (inKey != 'Y' and inKey != 'y') and (inKey != 'N' and inKey != 'n'):
			print('Incorrect input')
		else:
			return inKey
			
#Main			
oldPlayer = createPlayer()
print('Welcome to craps')
print('by Nate Sobol')
print('--------------------------------------\n')
pFlag = 'false'

while pFlag == 'false':
	name = input('Enter your name: ')
	try:
		currentGameStats = ()
		currentGameStats = oldPlayer[name]
		print('Welcome back ' + name + '!')
		print('Current Game statistics are:')
		winAmount= int(currentGameStats[1])
		remainingFunds = int(currentGameStats[0])
		loseAmount= int(currentGameStats[2])
		printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)
		pFlag = 'true'
	except:
		print('Player doesnt exist yet')
		newPlayer = input('Are you really a new player? (Y = yes, N = no): ')
		if(newPlayer == 'Y' or newPlayer == 'y'):
			print('Creating newly entered player')
			name = input('Enter your name: ')
			winAmount = 0
			loseAmount = 0
			remainingFunds = 1000
			oldPlayer[name] = currentGameStats
			print('Created Player with defualt stats')
			pFlag = 'true'

while choice != '5':
	print('--------------------------------')
	print('\nCraps Menu\n\n' + '1\tPlay the game\n' + '2\tDisplay Available Funds\n' + '3\tReset winnings to Zero\n' + '4\tSave Name and Score\n' + '5\tQUIT\n\n')
	print('--------------------------------')
	choice = input('choice: ')
	if choice == '1':
		print('Play the game\n')
		if(remainingFunds <= 0):
			print('No more funds. game over.')
		else:
			rCMD = ''
			gFlag = 'true'
			turn = 1
			point = 0
			while gFlag == 'true':
				rCMD = rollDice()
				if(rCMD == 'R' or rCMD == 'r'):
					dice1 = random.randint(MINVAL,MAXVAL)
					dice2 = random.randint(MINVAL,MAXVAL)
					point = dice1 + dice2
					print('dice 1:\t %d \n' % (dice1))
					print('dice 2:\t %d \n' % (dice2))
					print('Roll Total:\t %d' % (point))
					if (point == 7 or point == 11) and turn == 1:
						print('You rolled a 7 or 11')
						print('you win!')
						remainingFunds = remainingFunds + 100
						winAmount+= 1
						gFlag = 'false'
					elif (point == 2 or point == 3 or point == 12) and turn == 1:
						print('you lose!')
						remainingFunds = remainingFunds - 100
						loseAmount+= 1
						if(remainingFunds <= 0):
							print('No funds remaining')
							gFlag = 'false'
					else: # play using the 'point'
						turn = turn + 1
						print('Keep rolling')
						while gFlag == 'true':
							rCMD = rollDice()
							if(rCMD == 'r' or rCMD == 'R'):
								dice1 = random.randint(MINVAL,MAXVAL)
								dice2 = random.randint(MINVAL,MAXVAL)
								print('You rolled a:\t %d' % (dice1 + dice2))
								if(point == (dice1 + dice2)):
									print('you win!')
									gFlag = 'false'
									keepRolling = 'false'
									remainingFunds = remainingFunds  + 100
									winAmount+= 1
								elif((dice1 + dice2) == 7):
									print('YOU LOSE!')
									print('You rolled a 7')
									gFlag = 'false'
									keepRolling = 'false'
									remainingFunds = remainingFunds - 100
									loseAmount+= 1
								else:
									print('Roll till you get a %d!\n' % (point))
							if(remainingFunds <= 0):
								print('GAME OVER-YOU ARE OUT OF FUNDS')
								gFlag = 'false'
								break

		printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)

	elif choice == '2':
		print('Display Available Funds\n')
		printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)

	elif choice == '3':
		print('defualt game stats')
		remainingFunds = 1000
		winAmount = 0
		loseAmount = 0
		printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)

	elif choice == '4':
		outfile = open(r'players.txt', 'w')
		print('Saving current game')
		printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)
		oldPlayer[name] = (remainingFunds, winAmount, loseAmount)
		for i in oldPlayer:
			tempTup = oldPlayer[i]
			outfile.write(i + '|' + str(tempTup[2])+ '|' + str(tempTup[1])+ '|' + str(tempTup[0]) + '\n')
		outfile.close()

	elif choice == '5':
		print('Quitting game')
		quitGame = getValidatedQuit()
		if quitGame == 'Y' or quitGame == 'y':
			print('Bye!')
			printPlayerStatistics(remainingFunds, name, winAmount, loseAmount)
			break
		else:
			choice = ''
	else:
		print('must be a number between 1 and 5')
