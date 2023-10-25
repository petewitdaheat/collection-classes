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

    def getData(self):
        """Returns the data value stored in the calling node

        Returns:
            _type_: data value stored in the calling node
        """        
        return self.__data
    
    def setData(self, data):
        """Sets the data value stored in the calling node to the 
        specified data value

        Args:
            data (_type_): specified data value
        """        
        self.__data = data

    def getLink(self):
        """Returns the link stored in the calling node.

        Returns:
            node: link stored in the calling node
        """        
        return self.__link
    
    def setLink(self, link):
        """Sets the link stored in the calling node to the specified link.

        Args:
            link (node): specified list
        """        
        self.__link = link

    def addNodeAfter(self, element):
        """Add a new node containing a specified element value 
        at a selected position in the calling node.

        Args:
            element (_type_): specified element value
        """        
        self.__link = node(element, self.__link)



    
