
FILE_NAME = "test.txt"

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
        
        print(f"Performing move #{i}: In direction {direction}, doing {amount} steps")
        
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
            
            print(f"Step #{j} - ", end="")
            if (dist_X > 1 or dist_Y > 1):
                print(f"move necessary with head={head} and tail={tail}")
            
                # a move is necessary
                if dist_X == 2:
                    print("  moving on X")
                    # move horizontally (left or right)
                    tail[0] = (head[0] + tail[0]) // 2
                    
                    # if we're not perfectly aligned on Y (i.e. we have a distance of 1), also move on Y, which means we end up in the same row as the head
                    if dist_Y > 0:
                        tail[1] = head[1]
                if dist_Y == 2:
                    print("  moving on Y")
                    # move vertically (up or down)
                    tail[1] = (head[1] + tail[1]) // 2
                    
                    # if we're not perfectly aligned on X (i.e. we have a distance of 1), also move on Y, which means we end up in the same column as the head
                    if dist_X > 0:
                        tail[0] = head[0]
            else:
                print("No move necessary")
        
            # NOTE: 
            # in both cases, i compute the new position of the tail by taking the average of the two coordinates.
            # This only works since the tail and head's coordinates can only be 0, 1 or 2 apart.
            # If the head could move more steps before the tail followed, or the distance between the two was longer, 
            # this would probably need to change
            
            
            # Record the position if it's new
            if tail not in positions_visited_by_tail:
                positions_visited_by_tail.append([tail[0], tail[1]])
        
        i += 1

    print(f"Here the full record of visited positions: \n{positions_visited_by_tail}")
    
    print(f"The number of positions visited by the rope tail is {len(positions_visited_by_tail)}")

# TRIES:
# 1) 9316 --> too high
