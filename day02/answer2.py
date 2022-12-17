
FILE_NAME = "input.txt"

scoreOwnChoice = {
	'A': 1, 	# Rock
	'B': 2,		# Paper
	'C': 3		# Scissors
}

'''
If win (outcome == 'Z'):
	'A' -> mychoice = 'B' --> score addition is 2	# (1 % 3) + 1 = 2
	'B' -> mychoice = 'C' --> score addition is 3	# (2 % 3) + 1 = 3
	'C' -> mychoice = 'A' --> score addition is 1	# (3 % 3) + 1 = 1

If lose (outcome == 'X'):
	'A' -> mychoice = 'C' --> score addition is 3	# (1 - 2) % 3 + 1 = -1%3 + 1 = 2 + 1 = 3
	'B' -> mychoice = 'A' --> score addition is 1	# (2 - 2) % 3 + 1 = 0%3 + 1 = 0 + 1 = 1
	'C' -> mychoice = 'B' --> score addition is 2 	# (3 - 2) % 3 + 1 = 1%3 + 1 = 1 + 1 = 2
'''

DEBUG = False

with open(FILE_NAME, 'r') as f:
	lines = f.readlines()
	
	totalScore = 0
	for i in range(len(lines)):
		currScore = 0
		# Extract my and the opponent's choices
		other, outcome = lines[i].strip().split(" ")
		
		# check whether we won or not and add the score of that
		
		# And then, add the score from whether we won or not
		if (outcome == 'Y'):	# draw
			currScore += 3
			# if we draw, we use the same symbol as the opponent
			currScore += scoreOwnChoice[other]
		elif (outcome == 'Z'):	# we win
			currScore += 6
			# if we win, we use the symbol one higher
			currScore += (scoreOwnChoice[other] % 3) + 1
		else:			# we lose
			# if we lose, we use the symbol one lower
			currScore += ((scoreOwnChoice[other] - 2) % 3) + 1
			# the problematic case is when scoreOwnChoice[other] == 1, as then we need to map it not to 0, but to 3.
			# hence, subtract 2 to make it go negative, do % 3 to get it to 2 instead, and add 1 to the result.
			# if the scoreOwnChoice is 2 or 3, the "-2 %3" is not gonna do anything --> (2-2) % 3 + 1 = 0%3 + 1 = 1, (3-2) % 3 + 1 = 1%3 + 1 = 2
		
		# DEBUGGING:
		if (DEBUG):
			print(f"#{i}\n - outcome = '{outcome}'\n - opponent choice = '{other}'")
			print(f" - score: {currScore}\n - total score so far: {totalScore}")
		
		totalScore += currScore
	
	print(f"The total score obtained by following the strategy guide is {totalScore}")
		
