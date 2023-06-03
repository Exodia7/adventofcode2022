
FILE_NAME = "input.txt"

class Tree():
    def __init__(self, height, left=None, top=None, right=None, bottom=None):
        self.height = height
        # Save all parameters
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        # And save yourself in the surrounding trees' parameters:
        if (self.left != None):
            self.left.right = self
        if (self.top != None):
            self.top.bottom = self
        if (self.right != None):
            self.right.left = self
        if (self.bottom != None):
            self.bottom.top = self


with open(FILE_NAME, 'r') as f:
    allLines = f.readlines()
    
    trees = []
    for row in range(len(allLines)):
        # Add a new empty row
        trees.append([])
        # Remove whitespace from the line
        allLines[row] = allLines[row].strip()
        
        for col in range(len(allLines[row])):
            # Get the height of the current tree
            h = allLines[row][col]
            
            # Extract the tree on the left column (if any)
            left_tree = None
            if col > 0:
                left_tree = trees[row][col-1]
            # Extract the tree above (if any)
            upper_tree = None
            if row > 0:
                upper_tree = trees[row-1][col]
            
            # Create a new Tree with those 2 as neighbours
            new_tree = Tree(h, left_tree, upper_tree)
            # and add it to the list
            trees[row].append(new_tree)
    
    # Now, we have all our trees and we need to check how many are visible
    number_visible = 0
    total_number = 0        # counting total number as sanity check
    for row in range(len(trees)):
        if row == 0 or row == len(trees)-1:
            # a tree on the top row or last row is always visible
            number_visible += len(trees[row])
            total_number += len(trees[row])
        else:
            for col in range(len(trees[row])):
                total_number += 1
                
                if col == 0 or col == len(trees[row])-1:
                    # a tree on the left-most or right-most column is always visible
                    number_visible += 1
                else:
                    # We have to check all directions one by one
                    t = trees[row][col]
                    done = False
                    move_directions = [lambda tree: tree.left,
                                       lambda tree: tree.top,
                                       lambda tree: tree.right,
                                       lambda tree: tree.bottom]
                    # Loop over all directions
                    i = 0
                    while (i < len(move_directions) and not done):
                        move_op = move_directions[i]
                        
                        current = move_op(t)
                        while (current.height < t.height):
                            current = move_op(current)
                            if current == None:
                                # We reached the end of the grid, i.e. the tree is visible
                                number_visible += 1
                                done = True
                                break
                        i += 1
    
    print(f"The number of visible trees out of all {total_number} trees is: {number_visible}")

# SOLUTION: 1851 visible trees out of a total of 9801
