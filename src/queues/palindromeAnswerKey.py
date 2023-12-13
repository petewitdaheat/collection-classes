from stack.stack import *
from queues.queue import *


@staticmethod
def isPalindromeDetected(expression: str):
    q = queue() # queue to read the expression forward
    s = stack() # stack to read the expression backward

    line = queue() # second queue

    mismatches = 0 # used to keep track of the differences in the queue and stack

    matches = 1 # used to keep track of how many characters correctly match

    # loop through expression a character at a time
    for e in expression:
        # if the current character is an alphabetic character
        if e.isalpha():
            # enqueue it on the line queue
            line.enqueue(e)

    # convert the expression to upper-case
    expression = expression.upper()

    # loop through expression a character at a time
    for e in expression:
        # if the current character is an alphabetic character
        if e.isalpha():
            # push it onto the stack and enqueue it on the queue
            s.push(e)
            q.enqueue(e)

    # while the queue isn't empty
    while(not q.isEmpty()):
    # if the element at the front of the queue isn't
    # equal to the element at the top of the stack
        if (q.dequeue() != s.pop()):
        # increment mismatches
            mismatches = mismatches + 1
            break
        else:
        # increment matches
            matches += 1

    # if no mismatches are detected, expression is a palindrome
    if (mismatches == 0):
        print("Your expression is a palindrome.")

    else:
        # expression is not a palindrome
        print("Your expression is not a palindrome.")
        print("Mismatch detected at:", end=" ")
        i = 1

    while (i <= matches):
    # print an appropriate amount of the line queue in the output message
        print(line.dequeue(), end="")
        i += 1
    print()