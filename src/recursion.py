class recursion:
    @staticmethod
    def evens(start: int, end: int):
        i = start
        if i == end:
            if (i % 2 == 0):
                print(i, end = ' ')
        else:
            if (i % 2 == 0):
                print(i, end = ' ')
                recursion.evens(i+1, end)
            else:
                recursion.evens(i+1, end)

