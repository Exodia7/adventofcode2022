

FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
	input = f.readlines()
	
	maxSum = -1
	i = 0
	currSum = 0
	while (i < len(input)):
		if (input[i] == "\n"):	# end of one elf's list of rations
			if (maxSum < currSum):
				maxSum = currSum
			currSum = 0
		else:	# elf's list of rations is still going on
			currSum += int(input[i])
		
		i += 1
	
	# check if the last elf's sum of rations is larger
	if (maxSum < currSum):
		maxSum = currSum
	
	print(f"The maximum sum of calories is {maxSum}")
