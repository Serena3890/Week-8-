# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Amber Conklin
# Creation Date: 7/30/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave(): 
    	 #cave is empty so loop will not run but loop is actually not needed
	 # Invalid while and loop 
	 # can be simplified and by putting this into cave = input()
	cave = input('Which cave will you go into? (1 or 2)')

	return cave # typo caves should be cave

def checkCave(choseCave): # typo should be chooseCave
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if choseCave == str(friendlyCave): # typo should be chooseCave
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')  #missing () making this a syntax error

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': # Syntax error should use == for both conditions
	displayIntro()
	caveNumber = chooseCave() 	# typo should be chooseCave
	checkCave(caveNumber)
    
	 # Can simplify and run smoother by puting this print into input function
	playAgain = input('Do you want to play again? (yes or no)')
	if playAgain == "no" or playAgain == 'n' 	# should add an or == 'n' to match previous options 
		print("Thanks for playing")		# typo in the spelling of "playing"

