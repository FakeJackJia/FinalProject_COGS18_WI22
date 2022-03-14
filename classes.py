"""Classes used throughout project"""

class GameManager: #class that stores map for each level
    """Class that stores serveral two-dimensional map

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    
    def __init__(self): # constructor for the class
        """Constructors to initialize the map as None

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.map = None # set the attribute map as None

    def level1(self): # methods for level 1 map
        """Store a two-dimentional array containing '*' and '#' in map

        Parameters
        ----------
        None

        Returns
        -------
        map : array
           Return the two-dimensional map that contains '*' and '#'
        """
        self.map = [['#', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] # store two-dimensional array in map

        return self.map # return the attribute map 

    def level2(self): # methods for level 2 map
        """Store a two-dimentional array containing '*' and '#' in map

        Parameters
        ----------
        None

        Returns
        -------
        map : array
           Return the two-dimensional map that contains '*' and '#'
        """
        self.map = [['*', '#', '#', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']] # store two-dimensional array in map

        return self.map # return the attribute map 

    def level3(self): # methods for level 3 map
        """Store a two-dimentional array containing '*' and '#' in map

        Parameters
        ----------
        None

        Returns
        -------
        map : array
           Return the two-dimensional map that contains '*' and '#'
        """
        self.map = [['*', '#', '#', '*', '*'], ['*', '#', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']] # store two-dimensional array in map

        return self.map # return the attribute map 
