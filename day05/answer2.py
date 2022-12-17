
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    
    # STEP 1 - extract the state of the stacks before the start of the procedure
    startStack = []
    i = 0
    while (not ('1' in lines[i])) and (i < len(lines)):    # i'm assuming that the lines specifying the numbers of each crate will always contain at least '1' for 1 stack
        startStack.append(lines[i].rstrip())
        i += 1
    # Extract how many stacks we have in total
    lastLine = lines[i].strip().split(' ')
    numStacks = int(lastLine[len(lastLine)-1])
    
    # Create as many stacks as we should have
    stacks = []
    for x in range(numStacks):
        stacks.append([])
    
    # DEBUGGING
    #print(f'The file contains {numStacks} stacks.\nThe stacks are currently:')
    #print(stacks)
    
    
    # at this point, all lines of the starting setup of the stack will be in "startStack"
    # --> now need to extract on which stack each part is
    for line in startStack:
        n = line.find('[')  # find the index of the first "[" on that line
        # the index of "[" will always be a multiple of 4, i.e.:
        # - for stack 1: index "[" = 0
        # - for stack 2: index "[" = 4
        # - for stack 3: index "[" = 8
        # ...
        # - for stack n: index "[" = 4 * (n-1)
        
        while n != -1:
            # compute the stack index
            stackIndex = n // 4
            
            # DEBUGGING
            #print(f'Currently at line "{line}", found a match at index {n}, which results in adding item to stack with index {stackIndex}')
            
            # extract the symbol (note that I make the assumption that the symbol is a single character, right after the "["
            letter = line[n+1:n+2]
            
            # add the letter to the correct stack, such that the top of the stack will be at index 0 and bottom at index len(stack)-1
            stacks[stackIndex].append(letter)
            
            # find the next "[" if any
            n = line.find('[', n+1)
    
    
    # DEBUGGING
    #print("Start stack is the following (remember, top is beginning of list):")
    #print(stacks)
    
    # then, apply all the moves
    i += 1  # to skip over the line of " 1   2  ..."
    i += 1  # to skip over the empty line
    while i < len(lines):
        # find the indexes of everything on this line
        quantityStart = lines[i].find('move') + len('move')
        quantityEnd = lines[i].find('from')
        fromStart = lines[i].find('from') + len('from')
        fromEnd = lines[i].find('to')
        toStart = lines[i].find('to') + len('to')
        toEnd = len(lines[i])
        
        # extract the numbers
        quantity = int(lines[i][quantityStart:quantityEnd].strip())
        fromStackIndex = int(lines[i][fromStart:fromEnd].strip()) -1    # why -1 ? because the indexes start at 0
        toStackIndex = int(lines[i][toStart:toEnd].strip()) -1
        
        # DEBUG PRINT
        #print(f'Taking {quantity} blocks from stack with index {fromStackIndex} to stack with index {toStackIndex}')
        
        # apply the change, "quantity" items at a time
        
        for x in range(quantity, 0, -1):
            # take the item from the top of the "from" stack
            item = stacks[fromStackIndex].pop(x-1)  # why x-1 ? indexing starts at 0 !
            
            # put it on top of the "to" stack
            stacks[toStackIndex].insert(0, item)
        
        # go to the next line
        i += 1
    
    # finally, read off the result
    result = ''
    for n in range(len(stacks)):
        result += str(stacks[n][0])
    # TODO: this could probably be made using some kind of map, by:
    # stacks.map(f x: str(x[0]))    and then concatenating (apply "+" operator) to the result to get the output.
    # PROBLEM is i don't know the exact python syntax, I should look into that later when I got network access
    
    print(f"The crates which will end up on top of the stacks are {result}")