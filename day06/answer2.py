
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
    line = f.readline()
    
    i = 13
    while i < len(line):
        # check whether there are any duplicates in the 4 characters ending at index i
        current = line[i-13:i+1]
        
        if (len(current) == len(set(current))): # if there are no duplicates, we found the marker
            break
        else:
            i += 1
    
    
    print(f"The number of characters before the start-of-packet marker is {i+1}")