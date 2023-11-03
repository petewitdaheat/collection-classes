from node.node import *

def main():
    # testInit()
    #testGettersAndSetters()
    #testAddNodeAfter()
    #testRemoveNodeAfter()
    # review()
    # testListLength()
    # testListSearch()
    # testListPosition()
    #testListCopy()
    testListCopyWithTail()

def testListCopyWithTail():
    print("Testing list copy with tail")
    print("Testing list copy")
    # construct a node with data equal to 5 and link equal to source
    # and assign its reference to source
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to source
    # and assign its reference to source
    source = node('B', source) # B -> S

    #construct a node with data equal to O and link equal to source
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct a node with data equal to 5 and link equal to source
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopyWithTail(source)    # J -> O -> B -> S, but at a different memory location

    print("Source contains", node.listPosition(source, 1).getData(),
         node.listPosition(source, 2).getData(),
         node.listPosition(source, 3).getData(),
         node.listPosition(source, 4).getData())
    
    print("Copy Head contains", node.listPosition(copy[0], 1).getData(),
         node.listPosition(copy[0], 2).getData(),
         node.listPosition(copy[0], 3).getData(),
         node.listPosition(copy[0], 4).getData())
    
    
    print("Copy tail contains", node.listPosition(copy[1], 1).getData())

def testListPosition():
    print("Testing list position")
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
    head = node('J', head) # J -> O -> B -> S

    print("First node contains data:", node.listPosition(head, 1).getData())    #J -> O -> B -> S
    print("Second node contains data:", node.listPosition(head, 2).getData())   # O -> B -> S
    print("Third node contains data:", node.listPosition(head, 3).getData())
    print("Fourth node contains data:", node.listPosition(head, 4).getData())

    if (node.listPosition(head, 5) != None):
        print("Fifth node contains data:", node.listPosition(head, 5).getData())
    else:
        print("There is no fifth node.")



def testListCopy():
    print("Testing list copy")
    # construct a node with data equal to 5 and link equal to source
    # and assign its reference to source
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to source
    # and assign its reference to source
    source = node('B', source) # B -> S

    #construct a node with data equal to O and link equal to source
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct a node with data equal to 5 and link equal to source
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source)    # J -> O -> B -> S, but at a different memory location

    print("Source contains", node.listPosition(source, 1).getData(),
         node.listPosition(source, 2).getData(),
         node.listPosition(source, 3).getData(),
         node.listPosition(source, 4).getData())
    
    print("Copy contains", node.listPosition(copy, 1).getData(),
         node.listPosition(copy, 2).getData(),
         node.listPosition(copy, 3).getData(),
         node.listPosition(copy, 4).getData())

def testListPosition():
    print("Testing list position")
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
    head = node('J', head) # J -> O -> B -> S

    print("First node contains data:", node.listPosition(head, 1).getData())    #J -> O -> B -> S
    print("Second node contains data:", node.listPosition(head, 2).getData())   # O -> B -> S
    print("Third node contains data:", node.listPosition(head, 3).getData())
    print("Fourth node contains data:", node.listPosition(head, 4).getData())

    if (node.listPosition(head, 5) != None):
        print("Fifth node contains data:", node.listPosition(head, 5).getData())
    else:
        print("There is no fifth node.")


def testListSearch():
    print("Testing list search")
    
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
    head = node('J', head) # J -> O -> B -> S

    print("Head contains", node.listSearch(head, 'J').getData())
    print("Head contains", node.listSearch(head, 'O').getData())
    print("Head contains", node.listSearch(head, 'B').getData())
    print("Head contains", node.listSearch(head, 'S').getData())

    if (node.listSearch(head, 'Z') != None):
        print("Head contains", node.listSearch(head, 'Z').getData())
    else:
        print("Head doesn't contain Z")


def testListLength():
    print("Testing list length")

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
    head = node('J', head) # J -> O -> B -> S

    print("Length of head is:", node.listLength(head))
 


def review():
    print("Review")

    #question 1
    head = node('X', None)
    print("The head node contains data:", head.getData())
    head = node('X', head)
    print("The head node contains data:", head.getData())
    head = node('X', head)
    print("The head node contains data:", head.getData())
    head = node('X', head)
    print("The head node contains data:", head.getData())

    # question 2
    selection1 = head

    #question 3
    selection1.addNodeAfter("O")

    # question 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # question 5
    selection1.addNodeAfter("O")

    # question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    #question 7
    selection1.addNodeAfter("O")

    # question 8
    tail = head

    # question 9
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # question 10
    selection2 = head

    # question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    # question 12
    head.setData("A")
    selection2.setData("A")
    selection1.setData("A")
    tail.setData("A")

    # question 13
    head.removeNodeAfter()
    selection2.removeNodeAfter()
    selection1.removeNodeAfter()
    tail.removeNodeAfter()







def testRemoveNodeAfter():
    print("Testing Remove Node After")

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
    head = node('J', head) # J -> O -> B -> S

    print("The head node contains data:", head.getData())

    # remove the node after the head refers to (node that contains data value equal to 0)
    head.removeNodeAfter()

    head = head.getLink()

    print("The head node contains data:", head.getData())

    # remove the node after the head refers to (node that contains data value equal to 0)
    #head.removeNodeAfter() #B

    #print("The head node contains data:", head.getData())


def testAddNodeAfter():
    print("Testing Add Node After")

    # construct a node with data equal to 5 and link equal to None
    # and assign its reference to head
    head = node('J', None) # J

    print("The head node contains data:", head.getData())

    # declare a new node named selection and make it refer 
    # to the sane node as head
    selection = head

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to O after the node selection
    # refers to
    selection.addNodeAfter('O') # J -> O

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to B after the node selection
    # refers to
    selection.addNodeAfter('B') # O -> B

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # B

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to S after the node selection
    # refers to
    selection.addNodeAfter('S') # B -> S

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # S

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # declare a new node named tail and make it refer to the same 
    # node as head
    tail = head

    # get tail's link and assign its reference to tail
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a new node with data equal to Z after the node tail
    # refers to 
    tail.addNodeAfter('Z')

    tail = tail.getLink()

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())
    print("The tail node contains data:", tail.getData())


def testGettersAndSetters():
    print("Testing Getters And Setters")

    # construct a node with data equal to 5 and link equal to None
    # and assign its reference to head
    head = node('R', None) # R

    print("The head node contains data:", head.getData())

    head.setData('S')
    print("The head node contains data:", head.getData())

    head = node('B', head) # B -> S
    print("The head node contains data:", head.getData())

    head = node('O', head) # O -> B -> S
    print("The head node contains data:", head.getData())

    head = node('J', head) # J -> O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # O -> B -> S
    print("The head node contains data:", head.getData())

        # get head's link and assign its reference back to head
    head = head.getLink() # B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    """head = head.getLink() # O -> B -> S
    print("The head node contains data:", head.getData())
    """    

    print("The head node contains link:", head.getLink())

    # set head's link to a new node
    head.setLink(node('O', None)) # S -> O


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
    head = node('J', head) # J -> O -> B -> S

    head = node(1, head) # 1 -> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1,2], head) # [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node(('A', 'B'), head) # ('A', 'B') -> [1,2] -> 1.5 -> 1 -> J -> O -> B -> S

    print()

if __name__ == "__main__":
    main()