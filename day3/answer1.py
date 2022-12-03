
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
	lines = f.readlines()
	
	totalPriorities = 0
	for i in range(len(lines)):
		# remove any leading or trailing whitespace
		line = lines[i].strip()
		
		# split it in half
		first = line[0:len(line)//2]
		second = line[len(line)//2:len(line)]
		
		# find the common letter
		n = 0
		for n in range(len(first)):
			if first[n] in second:	# we found our common item type
				# find the corresponding priority and add it to the sum
				#print(f"#{i}. Found letter '{first[n]}' as common item type.")
				if first[n].islower():
					totalPriorities += ord(first[n]) - ord('a') + 1
					#print(f" - added priority = {ord(first[n]) - ord('a')}")
				else:
					totalPriorities += ord(first[n]) - ord('A') + 27
					#print(f" - added priority = {ord(first[n]) - ord('A') + 27}")
				break
	
	
	print(f"The sum of priorities of item types present in both compartments of all rucksacks is {totalPriorities}")
