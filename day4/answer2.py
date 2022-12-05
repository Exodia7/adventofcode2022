
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    
    totalFullDuplicates = 0
    for line in lines:
        # separate the two elves' ranges
        first, second = line.strip().split(',')
        # and further, extract the start and end of each range
        first = first.split('-')
        first[0] = int(first[0])
        first[1] = int(first[1])
        second = second.split('-')
        second[0] = int(second[0])
        second[1] = int(second[1])
        
        # DEBUGGING
        #print(f"First range = from {first[0]} to {first[1]}\nSecond range = from {second[0]} to {second[1]}")
        
        # check whether one of the two overlaps with the other
        if (second[0] <= first[0] <= second[1]) or (second[0] <= first[1] <= second[1]) or (first[0] <= second[0] <= first[1]) or (first[0] <= second[1] <= first[1]):
            totalFullDuplicates += 1
            #print("  and that is a duplicate !")
    
    print(f"There are {totalFullDuplicates} of assignment pairs where one range overlaps with the other one.")