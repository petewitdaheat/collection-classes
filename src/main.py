from node.node import *

def main():
    testInit()

def testInit():
    print("Testing Node Init")

    # construct a node with data equal to 5 and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head
    head = node('B', head) # B -> S

    #construct a node with data equal to  0and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to 5 and link equal to head
    # and assign its reference to head
    head - node('J', head) # J -> O -> B -> S

    print()

if __name__ == "__main__":
    main()