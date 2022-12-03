

FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
	input = f.readlines()
	
	maxSum1 = -1
	maxSum2 = -1
	maxSum3 = -1
	i = 0
	currSum = 0
	while (i < len(input)):
		if (input[i] == "\n"):	# end of one elf's list of rations
			if (maxSum1 < currSum):
				maxSum3 = maxSum2
				maxSum2 = maxSum1
				maxSum1 = currSum
			elif (maxSum2 < currSum):
				maxSum3 = maxSum2
				maxSum2 = currSum
			elif (maxSum3 < currSum):
				maxSum3 = currSum
			
			currSum = 0
		else:	# elf's list of rations is still going on
			currSum += int(input[i])
		
		i += 1
	
	# check if the last elf's sum of rations is larger
	if (maxSum1 < currSum):
		maxSum3 = maxSum2
		maxSum2 = maxSum1
		maxSum1 = currSum
	elif (maxSum2 < currSum):
		maxSum3 = maxSum2
		maxSum2 = currSum
	elif (maxSum3 < currSum):
		maxSum3 = currSum
	
	print(f"The maximum sum of calories is {maxSum1 + maxSum2 + maxSum3}")
