
FILE_NAME = "input.txt"

scoreOwnChoice = {
	'X': 1, 
	'Y': 2,
	'Z': 3
}

mapOtherChoice = {
	'A': 'X',
	'B': 'Y',
	'C': 'Z'
}

with open(FILE_NAME, 'r') as f:
	lines = f.readlines()
	
	totalScore = 0
	for i in range(len(lines)):
		currScore = 0
		# Extract my and the opponent's choices
		other, mine = lines[i].strip().split(" ")
		other = mapOtherChoice[other]
		
		# Add the score from my choice
		currScore += scoreOwnChoice[mine]
		
		# And then, add the score from whether we won or not
		if (mine == other):	# draw
			currScore += 3
		elif (mine == 'X' and other == 'Z') or (mine == 'Y' and other == 'X') or (mine == 'Z' and other == 'Y'):	# we win
			currScore += 6
		#else we lose, and the score stays
		
		
		# DEBUGGING:
		#print(f"#{i}\n - my choice = '{mine}'\n - opponent choice = '{other}'")
		#print(f" - score: {currScore}\n - total score so far: {totalScore}")
		
		totalScore += currScore
	
	print(f"The total score obtained by following the strategy guide is {totalScore}")
		
