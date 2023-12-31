from node.node import *
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from stack.serialsearch import *
from stack.insertionsort import *
from queues.queue import *
from queues.palindrome import *
from queues.palindromerewrite import *
from queues.palindromefeedback import *
from queues.palindromeAnswerKey import *
from loops import *
from recursion import *

def main():
    #testEnqueue()
    #testQueueIsEmpty()
    #testDequeue()
    #testQueuePeek()
    #testPalindrome()
    #testPalindromeRewrite()
    #testPalindromeFeedback()
    #testPalindromeAnswerKey()
    santaClaus()
    getPalindromes()
    recursion_func()

def santaClaus():
    # 1
    s = node('S', None)
    s.addNodeAfter('A')
    s.addNodeAfter('N')
    s.addNodeAfter('T')
    s.addNodeAfter('A')

    # 2
    c = node('C', None)
    c.addNodeAfter('L')
    c.addNodeAfter('A')
    c.addNodeAfter('U')
    c.addNodeAfter('S')

    # 3
    selection = s

    # 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    # 5
    s = node(s, c)

    # santa radar holly kayak civic merry level noon cookies elves

def getPalindromes():
    words = list(input("Enter ten words separated by a space: ").split())
    i = 0
    yes_palindrome = []
    no_palindrome = []

    for i in words:
        if(palindrome.isPalindrome(i)):
            yes_palindrome.append(i)
        else:
            no_palindrome.append(i)

    print("These words are palindromes:", *yes_palindrome)
    print("These words are not palindromes:", *no_palindrome)


def recursion_func():
    print("LOOP")
    loops.evens(-10, 10)
    print("\nRECURSION")
    recursion.evens(-10, 10)
    
    
    


    


def testPalindromeFeedback():
    exp = input("Please enter an expression: ")

    if(palindrome.isPalindrome(exp)):
        print("Your expression is a palindrome!")
    else:
        print("Your expression is not a palindrome.")
        print("Mismatch detected at:", palindrome.isNotPalindrome(exp))

def testPalindromeRewrite():
    exp = input("Please enter an expression: ")
    while exp != '':
        if(palindrome.isPalindrome(exp)):
            print("Your expression is a palindrome!")
        else:
            print("Your expression is not a palindrome.")

        exp = input("Please enter an expression: ")

def testPalindrome():
    exp = input("Please enter an expression: ")

    if(palindrome.isPalindrome(exp)):
        print("Your expression is a palindrome!")
    else:
        print("Your expression is not a palindrome.")

def testEnqueue():
    print("Testing Enqueue Method in Queue Class")

    q = queue()
    print("Queue size is:", q.size())   # 0
    print("Queue contains:", q)         #[]

    q.enqueue("S")
    print("Queue size is:", q.size())   # 1
    print("Queue contains:", q)         #[Q]

    # q.enqueue("B")
    q.enqueue(1)
    print("Queue size is:", q.size())   # 2
    print("Queue contains:", q)         #[Q 1]

    # q.enqueue("O")
    q.enqueue((1,2))
    print("Queue size is:", q.size())   # 3
    print("Queue contains:", q)         #[Q 1 (1 , 2)]

    # q.enqueue("J")
    q.enqueue([1,2,3])
    print("Queue size is:", q.size())   # 4
    print("Queue contains:", q)         #[Q 1 (1 , 2) [1,2,3]]

def testQueueIsEmpty():
    print("Testing Is Empty Method in Queue Class")

    q = queue()
    q.enqueue("S")
    q.enqueue("B")
    q.enqueue("O")
    q.enqueue("J")

    print("Queue size is:", q.size())   # 4
    print("Queue contains:", q)         # [J O B S]

    while(not q.isEmpty()):
        print("Just popped:", q.dequeue())

    print("Queue size is:", q.size())   # 0
    print("Queue contains:", q)         # []

def testDequeue():
    print("Testing Dequeue Method in Queue Class")

    q = queue()
    q.enqueue("S")
    q.enqueue("B")
    q.enqueue("O")
    q.enqueue("J")

    print("Queue size is:", q.size())   # 4
    print("Queue contains:", q)         # [J O B S]
    print("Just popped:", q.dequeue())      # J

    print("Queue size is:", q.size())   # 3
    print("Queue contains:", q)         # [O B S]
    print("Just popped:", q.dequeue())      # Opush

    print("Queue size is:", q.size())   # 2
    print("Queue contains:", q)         # [B S]
    print("Just popped:", q.dequeue())      # B

    print("Queue size is:", q.size())   # 1
    print("Queue contains:", q)         # [S]
    print("Just popped:", q.dequeue())      # S

def testQueuePeek():
    print("Testing Peek Method in Queue Class")
    q = queue()
    print("Queue size is:", q.size())               # 0
    print("Queue contains:", q)                     # []
    q.enqueue("S")
    print("Queue size is:", q.size())               # 1
    print("Queue contains:", q)                     #[S]
    print("Top element in queue is:", q.peek())     # S
    q.enqueue("B")
    print("Queue size is:", q.size())               # 2
    print("Queue contains:", q)                     # [B S]
    print("Top element in queue is:", q.peek())     # B
    q.enqueue("O")
    print("Queue size is:", q.size())               # 3
    print("Queue contains:", q)                     # [O B S]
    print("Top element in queue is:", q.peek())     # O
    q.enqueue("J")
    print("Queue size is:", q.size())               # 4
    print("Queue contains:", q)                     # [J O B S]
    print("Top element in queue is:", q.peek())     # J

def testInsertionSort():

    # create an empty queue
    data = queue()

    # initialize first
    first = 0

    # push -7 onto the top of the queue
    data.push('-7')

    # push 42 onto the top of the stack
    data.push('42')

    # push 70 onto the top of the stack
    data.push('70')

    # push 39 onto the top of the stack
    data.push('39')

    # push 3 onto the top of the stack
    data.push('3')

    # push 63 onto the top of the stack
    data.push('63')

    # push 8 onto the top of the stack
    data.push('8')

    # print unsorted stack
    print(data)

    # call insertion sort method
    data = insertionsort(data, 1)

    # print sorted stack
    print(data)



    
def testSerialSearch():
    # create an empty stack
    a = stack()

    # initialize first
    first = 0
    
    # initialize size
    size = 0
    
    # initialize target
    target = ''
    
    # push -7 onto the top of the stack
    a.push(-7)

    # push 42 onto the top of the stack
    a.push(42)
    
    # push 70 onto the top of the stack
    a.push(70)
    
    # push 39 onto the top of the stack
    a.push(39)
    
    # push 3 onto the top of the stack
    a.push(3)
    
    # push 63 onto the top of the stack
    a.push(63)
    
    # push 8 onto the top of the stack
    a.push(8)

    # print the stack
    print(a)

    # call serial search method and display its return.
    print(serialsearch(a, 1, 7, 70))



def testPeek():
    print("Testing Pop Method in Stack Class")
    s = stack()
    print("Stack size is:", s.size())               # 0
    print("Stack contains:", s)                     # []
    s.push("Q")
    print("Stack size is:", s.size())               # 1
    print("Stack contains:", s)                     #[Q]
    print("Top element in stack is:", s.peek())     # Q
    s.push("B")
    print("Stack size is:", s.size())               # 2
    print("Stack contains:", s)                     # [B Q]
    print("Top element in stack is:", s.peek())     # B
    s.push("O")
    print("Stack size is:", s.size())               # 3
    print("Stack contains:", s)                     # [O B Q]
    print("Top element in stack is:", s.peek())     # O
    s.push("J")
    print("Stack size is:", s.size())               # 4
    print("Stack contains:", s)                     # [J O B Q]
    print("Top element in stack is:", s.peek())     # J


    

def testIsEmpty():
    print("Testing Is Empty Method in Stack Class")

    s = stack()
    s.push("Q")
    s.push("B")
    s.push("O")
    s.push("J")

    print("Stack size is:", s.size())   # 4
    print("Stack contains:", s)         # [J O B Q]

    while(not s.isEmpty()):
        print("Just popped:", s.dequeue())

    print("Stack size is:", s.size())   # 0
    print("Stack contains:", s)         # []


def testPop():
    print("Testing Pop Method in Stack Class")

    s = stack()
    s.push("Q")
    s.push("B")
    s.push("O")
    s.push("J")

    print("Stack size is:", s.size())   # 4
    print("Stack contains:", s)         # [J O B Q]
    print("Just popped:", s.pop())      # J

    print("Stack size is:", s.size())   # 3
    print("Stack contains:", s)         # [O B Q]
    print("Just popped:", s.pop())      # O

    print("Stack size is:", s.size())   # 2
    print("Stack contains:", s)         # [B Q]
    print("Just popped:", s.pop())      # B

    print("Stack size is:", s.size())   # 1
    print("Stack contains:", s)         # [Q]
    print("Just popped:", s.pop())      # Q


def testPush():
    print("Testing Push Method in Stack Class")

    s = stack()
    print("Stack size is:", s.size())   # 0
    print("Stack contains:", s)         #[]

    s.push("Q")
    print("Stack size is:", s.size())   # 1
    print("Stack contains:", s)         #[S]

    # s.push("B")
    s.push(1)
    print("Stack size is:", s.size())   # 2
    print("Stack contains:", s)         #[B S]

    # s.push("O")
    s.push((1,2))
    print("Stack size is:", s.size())   # 3
    print("Stack contains:", s)         #[O B S]

    # s.push("J")
    s.push([1,2,3])
    print("Stack size is:", s.size())   # 4
    print("Stack contains:", s)         #[J O B S]


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