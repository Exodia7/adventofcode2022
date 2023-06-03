
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

def print_trees(trees):
    print("The trees look like this:")
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            t = trees[row][col]
            print(t.height, end="")
        print()


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
    
    # Now, we have all our trees and we need to check their scenic scores
    ''' # UNCOMMENT THIS TO PRINT THE TREES
    print_trees(trees)
    '''
    
    selected_pos = [None, None]
    selected_scenic_score = 0
    for row in range(len(trees)):
        # if row == 0 or row == len(trees)-1:
        # a tree on the top row or last row has (at least) one scenic distance of zero, hence they can not be selected (0 times anything else = 0)
        if row > 0 and row < len(trees)-1:
            for col in range(len(trees[row])):
                #if col == 0 or col == len(trees[row])-1:
                # a tree on the left-most or right-most column has one scenic distance of zero, hence they can not be selected (0 times anything else = 0)
                if col > 0 and col < len(trees[row])-1:
                    # We have to check all directions one by one
                    t = trees[row][col]
                    move_directions = [lambda tree: tree.left,
                                       lambda tree: tree.top,
                                       lambda tree: tree.right,
                                       lambda tree: tree.bottom]
                    # Loop over all directions
                    i = 0
                    curr_scenic_score = 1
                    while i < len(move_directions):
                        move_op = move_directions[i]
                        
                        current = move_op(t)
                        viewing_dist = 1
                        while (current.height < t.height):
                            current = move_op(current)
                            if current != None:
                                viewing_dist += 1
                            else:
                                # we stop counting the distance when we reach the border
                                break
                        
                        # Multiply the scenic score by the viewing distance in that direction
                        curr_scenic_score *= viewing_dist
                        
                        i += 1
                    
                    if curr_scenic_score > selected_scenic_score:
                        selected_pos = [col, row]
                        selected_scenic_score = curr_scenic_score
    
    print(f"The tree with the best scenic score out of all trees has score: {selected_scenic_score}\nIt is at position {selected_pos}")

# SOLUTION: best scenic score is 574080, achieved by tree at position [52, 78] (with indexing starting at 0, i.e. it's the 53rd column and 79th row)
# CORRECT !