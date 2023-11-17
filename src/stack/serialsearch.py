from node.node import *
from stack.stack import *

def serialsearch(a: stack, first: int, size: int, target):
    """Searches for a desired element in a list of elements
    starting at a[first].

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target: the element to search for

    Returns:
        int: If target appears in the list, index of the element
        that contains target; else -1
    """    
    # set an int variable i to 0
    i = 0

    # set a boolean variable found to false
    found = False

    # while there are more elements to search
    # and the target hasn't been found
    # i plus first doesn't exceed i + first
    while ((i < size) and not found and (i + first < a.size())):
        # if the current element is the target 
        # if (a[i + first] == target)
        if (a.setData(i + first) == target):
            # set found to true
            found = True
        else:
            # incremement i by 1
            i += 1
        
    # check if the target was found
    if (found):
        #return index of target
        return i + first
    else:
        # return negative 1
        return -1