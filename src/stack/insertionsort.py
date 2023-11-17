from node.node import *
from stack.stack import *

def insertionsort(data: stack, first: int):
    """sorts a list of integers from the smallest to largest
    bypassing the nodes to the left of first.

    Args:
        data (stack): stack to be sorted
        first (int): the node position at which the sort will begin
    """    
    # initialize loop counter variable i to 1
    i = 1

    #initialize loop counter variable j to 0
    j = 0

    # initialize next value to 0

    
    

    # loop through list as many times as speciified by the 
    # length of the list and first
    # this loop represents the blue arrow in the slides
    while(i < data.size() - first):
        # store a copy of a number in index position first + i 
        # in next value

        head = node(data.pop(), None)
        while i in range(data.size()):
            head = node(data.pop(), head)

        # loop through the list starting at the same index as
        # next value and iterate back toward first as long as 
        # the element to the left of next value is greater than
        # next value and we're not the whole way back to first
        j = first + i
        while(j > first and data.size() > node.listLength(head)):
            # shift the element to the left of the next value right
            # ward one position

            head = head.getLink()

            # insert next value into the element that was just
            # shifted
            data = node.setDataAtPosition(head.getData(), data)
            data = data.push(data)

            # decrement j by 1
            j = j-1

        # increment i by 1
        i = i + 1

        return data