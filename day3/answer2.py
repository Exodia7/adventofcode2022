
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
	lines = f.readlines()
	
	totalBadgePriorities = 0
	i = 0
	while i+2 < len(lines):
		one = lines[i]
		two = lines[i+1]
		three = lines[i+2]
		
		# find the common letter
		n = 0
		for n in range(len(one)):
			if one[n] in two and one[n] in three:	# we found our common item type
				# find the corresponding priority and add it to the sum
				#print(f"#{i}. Found letter '{one[n]}' as common item type.")
				if one[n].islower():
					totalBadgePriorities += ord(one[n]) - ord('a') + 1
					#print(f" - added priority = {ord(one[n]) - ord('a')}")
				else:
					totalBadgePriorities += ord(one[n]) - ord('A') + 27
					#print(f" - added priority = {ord(one[n]) - ord('A') + 27}")
				break
		
		i += 3
	
	print(f"The sum of priorities of the elves badges is {totalBadgePriorities}")
