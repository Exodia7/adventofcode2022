
# a directory, which holds other Directories or Files as children
class Directory:
    def __init__(self, name:str, parent):
        # save the parameters
        self.name = name
        self.parent = parent
        self.children = []
        # and make sure that the list of children of the parent stays up to date
        if parent != None:
            parent.children.append(self)
    
    def get_full_path_name(self):   # will give a fully qualified path name
        if (self.parent == None):
            return self.name
        else:
            return f"{self.parent.get_full_path_name()}/{self.name}"
    
    def get_size(self, cache={}):
        ''' COMMENTED OUT, WANTED TO GET MORE EFFICIENCY BY USING A CACHE BUT IT'S BECOMING TOO CUMBERSOME
        full_name = self.get_full_path_name()
        if full_name in cache:  # if result is cached, we just return cache entry
            return cache[full_name], cache
        else:
            # compute total size
            total_size = map(lambda x: x.get_size()[0], self.children)
            # update the cache with the new result
            cache[full_name] = total_size
            
            return total_size, cache
        '''
        return sum(map(lambda x: x.get_size(), self.children))


# a file, which has a certain size
class File:
    def __init__(self, name:str, parent : Directory, size:int):
        # save the parameters
        self.name = name
        self.parent = parent
        self.size = size
        # and make sure that the list of children of the parent stays up to date
        if parent != None:
            parent.children.append(self)
    
    def get_full_path_name(self):   # will give a fully qualified path name
        if (self.parent == None):
            return self.name
        else:
            return f"{self.parent.get_full_path_name()}/{self.name}"
    
    def get_size(self, cache={}):
        ''' COMMENTED OUT, WANTED TO GET MORE EFFICIENCY BY USING A CACHE BUT IT'S BECOMING TOO CUMBERSOME
        full_name = self.get_full_path_name()
        if full_name in cache:  # if result is cached, we just return cache entry
            return cache[full_name], cache
        else:
            # update cache and return size
            cache[full_name] = self.size
            return self.size, cache
        '''
        return self.size


# computes the sum of the directories in the file system which pass a certain filter
#   the filter function takes a directory's size and then returns whether or not the directory should be included in the count
def get_total_size(d : Directory, filter_func = (lambda x: True)):
    total_size = 0
    children_to_explore = [child for child in d.children]
    while len(children_to_explore) > 0:
        curr_child = children_to_explore[0]
        if isinstance(curr_child, Directory):
            # Check whether the directory passes the filter
            dir_size = curr_child.get_size()
            if filter_func(dir_size):
                total_size += dir_size  # and if so, add its size to the count
            
            # Finally, add its children to the list to explore
            new_children_to_explore = [child for child in curr_child.children]
            children_to_explore = children_to_explore + new_children_to_explore
        
        # Pop the current child
        children_to_explore.remove(curr_child)
    
    return total_size


def print_filesystem(d: Directory, indent=0):
    print(" " * indent, end='')
    print(d.name)
    
    for child in d.children:
        if isinstance(child, Directory):
            print_filesystem(child, indent+2)
        else:
            print(" " * (indent+2), end='')
            print(f"{child.name} {child.size}")


# some constants
FILE_NAME = "input.txt"

CD_CMD_START = "$ cd "
ROOT_DIR_NAME = "/"
GO_UP_ONE_DIR = ".."
LS_CMD = "$ ls"
DIR_INDICATOR = "dir"

MAX_SIZE = 100000


# the actual program
with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    
    root_dir = Directory(ROOT_DIR_NAME, None)
    
    curr_dir = None
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        
        if l.startswith(CD_CMD_START):  # we're reading a cd command
            # extract the directory we're going to
            cd_dir_name = l[len(CD_CMD_START):]
            
            # three cases:
            if cd_dir_name == GO_UP_ONE_DIR:    # go up one level
                curr_dir = curr_dir.parent
            elif cd_dir_name == ROOT_DIR_NAME:  # go to root dir
                curr_dir = root_dir
            else:                   # go down one level
                # check whether that child already existed
                found_dir = False
                for c in curr_dir.children:
                    if c.name == cd_dir_name:
                        # if so, take that directory as current directory
                        curr_dir = c
                        found_dir = True
                
                # if not, we create a new object for it     
                if not found_dir:
                    d = Directory(cd_dir_name, curr_dir)
                    # and update the current directory to it
                    curr_dir = d
        
        elif l == LS_CMD:
            # read the next lines until the next line is a command again
            next_line = ''
            while i+1 < len(lines) and (not lines[i+1].startswith(CD_CMD_START) or lines[i+1] == LS_CMD):
                # read the next line and process it depending on whether it's a file or directory
                next_line = lines[i+1].strip()
                
                part1, part2 = next_line.split(" ")
                new_child = None
                if part1 == DIR_INDICATOR:
                    # it's a directory
                    new_child = Directory(part2, curr_dir)
                else:
                    # it's a file, which means part1 is its size
                    new_child = File(part2, curr_dir, int(part1))
                
                # and go to next line
                i += 1
        else:
            print(f"Something went really wrong, can't parse line '{line}'")
        
        # go to next line to parse
        i += 1
    
    ''' DEBUGGING '''
    print_filesystem(root_dir)
    
            
    # finally, go through our file system and make the sum of all objects larger than a certain size
    result = get_total_size(root_dir, lambda x: x < MAX_SIZE)
    # Find all of the directories with a total size of at most 100000, 
    #   then calculate the sum of their total sizes
    
    print(f"The total sum of the sizes of directories of size smaller than {MAX_SIZE} is {result}")
    
    # TRIES:
    # try1 159244055 --> too high
    #   (added condition to only sum the directories)
    # try2 1432936  --> CORRECT !