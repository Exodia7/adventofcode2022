
FILE_NAME = "input.txt"

with open(FILE_NAME, 'r') as f:
    # OPTIONS:
    # - modelling the rope ends using X, Y coordinates VS moving them around in a 2D-list
    #       PROBLEM with list: the moves might bring the rope ends out
    #   --> X, Y it is
    
    # - modelling the two rope ends as a class VS as 2-item list
    #   --> let's just try list for now, we'll see if we need an actual class later
    
    # - representing head as absolute coordinates and tail as relative coordinates compared to head?
    #       --> though then need both to compute absolute position of tail
    #     VS
    #   representing both head and tail as absolute coordinates
    #   --> feel like absolute coordinates for both will be easier
    
    # origin is at bottom left corner, increasing coordinates is towards right or upwards
    head = [0, 0]
    tail = [0, 0]
    positions_visited_by_tail = [[tail[0], tail[1]]]  # already start with the starting position
    
    allLines = f.readlines()
    i = 0
    while i < len(allLines):
        # Extract the move
        direction, amount = allLines[i].strip().split(" ")
        direction = direction.upper()
        amount = int(amount)
        
        # Apply it, one by one
        for j in range(amount):
            # Move the head
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] += 1
        
            # Move the tail if any move is required
            dist_X = abs(head[0] - tail[0])
            dist_Y = abs(head[1] - tail[1])
            if (dist_X > 1 or dist_Y > 1):
                # a move is necessary
                if dist_X == 2:
                    # move horizontally (left or right)
                    tail[0] = (head[0] + tail[0]) // 2
                if dist_Y == 2:
                    # move vertically (up or down)
                    tail[1] = (head[1] + tail[1]) // 2
        
            # NOTE: 
            # in both cases, i compute the new position of the tail by taking the average of the two coordinates.
            # This only works since the tail and head's coordinates can only be 0, 1 or 2 apart.
            # If the head could move more steps before the tail followed, or the distance between the two was longer, 
            # this would probably need to change
            
            
            # Record the position if it's new
            if tail not in positions_visited_by_tail:
                positions_visited_by_tail.append([tail[0], tail[1]])
        
        i += 1

    
    print(f"The number of positions visited by the rope tail is {len(positions_visited_by_tail)}")

# TRIES:
# 1) 9316 --> too high
