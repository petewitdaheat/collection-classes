from queues.queue import *

class palindrome:
    @staticmethod
    def isPalindrome(expression: str):
        """Checks if the expression given reads the same forward
        and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression is a palindrome, else 
            False.
        """
        q = queue()     # queue to read the expression forward
        w = queue()    # stack to read the expression backward

        mismatches = 0  # used to keep track of the differences in the queue and stack

        # convert expression to all uppercase
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the current character is an alphabetic character
            if e.isalpha():
                # add it to the queue
                q.enqueue(e)


        for i in list(reversed(expression)):
            if i.isalpha():
                w.enqueue(i)

        # while the queue isn't empty 
        while (not q.isEmpty()):
            # if the element at the front of the queue isn't
            # equal to the element at the top of the stack
            if (q.dequeue() != w.dequeue()):
                # increment mismatches
                mismatches += 1

        # return True if muismatches is zero, else return false
        return (mismatches == 0)
