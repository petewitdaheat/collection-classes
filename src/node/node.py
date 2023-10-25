class node:
    """The node class holds a collection of values using nodes. It includes
    methods that allow nodes to be manipulated and modified.
    """    
    def __init__(self, data, link):
        """Constructs a node using the specified data value and link.

        :ivar __data: data value of node
        :ivar__lin: link portion of node

        Args:
            data: specified data value
            link: specified link
        """        
        self.__data = data
        self.__link = link
