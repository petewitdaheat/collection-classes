from queues.queue import *
from stack.stack import *

class palindrome:
    @staticmethod
    def isPalindrome(expression: str):
        """Checks if the expression given reads the same forward
        and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindromw, else 
            False.
        """
        q = queue()     # queue to read the expression forward
        s = stack()     # stack to read the expression backward

        mismatches = 0  # used to keep track of the differences in the queue and stack

        # convert expression to all uppercase
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the current character is an alphabetic character
            if e.isalpha():
                # push it onto the stack and add it to the queue
                s.push(e)
                q.enqueue(e)
        # while the queue isn't empty 
        while (not q.isEmpty()):
            # if the element at the front of the queue isn't
            # equal to the element at the top of the stack
            if (q.dequeue() != s.pop()):
                # increment mismatches
                mismatches += 1

        # return True if muismatches is zero, else return false
        return (mismatches == 0)
    
    @staticmethod
    def isNotPalindrome(expression: str):
        """Checks if the expression given reads the same forward
        and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindrome, else 
            False.
        """
        q = queue()     # queue to read the expression forward
        s = stack()     # stack to read the expression backward

        count = 0


        # convert expression to all uppercase
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the current character is an alphabetic character
            if e.isalpha():
                # push it onto the stack and add it to the queue
                s.push(e)
                q.enqueue(e)
        # while the queue isn't empty 
        while (not q.isEmpty()):
            # if the element at the front of the queue isn't
            # equal to the element at the top of the stack
            while (q.dequeue() != s.pop()):
                count += 1

            new_exp = expression[0:count]


        return new_exp



            

