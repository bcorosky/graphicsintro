import random
import time

def displayIntro():
	print ('You are on a planet full of dragons. In front of you,')
	print ('you see two caves. In one cave, the dragon is friendly')
	print ('and will share his treasure with you. The other dragon')
	print ('is greedy and hungry, and will eat you on sight.')
	print
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2' and cave != '3':
		print ('Which cave will you go into? (1, 2 or 3?)')
		cave = raw_input()
	return cave
def cave1():
	print ('Gives you his treasure!')
def cave2():
	print ('You DIE!!!')
def cave3():
	print ('You DIE!!!!')

def checkCave(chosenCave):
	
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(2)
		
	friendlyCave = (1)
	deadlyCave = (2)
	cliff = (3)
	
	if chosenCave == str(friendlyCave):
		friendlyCave = cave1()
	elif chosenCave == str(deadlyCave):
		deadlyCave = cave2()
	elif chosenCave == str(cliff):
		cliff = cave3()
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		checkCave(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
