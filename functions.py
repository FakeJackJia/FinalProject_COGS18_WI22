"""A collection of function for doing my project."""

import random # import random library 
from classes import GameManager # import class GameManager from classes

def introduction(): # function for introduction of the game
    """Print out the the sentences that introduce how this game works

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    
    # for the all belowings: print out the words for introduction of the game
    print("Welcome to the game of wisdom and luckiness!!!!!!!!!!!!!!!!!!!!!!") 
    print("#**") 
    print("***")
    print("***")
    print("As you can see, this game is constructed of * and #")
    print("For this game, you need to fulfill all the spaces with all #")
    print("Here comes the Rule")
    print("-----------------------------------------------------------------------")
    print("For this game, by entering the row and column, you could only click '#'")
    print("Then, the space around '#' will become '#' and itself will become *")
    print("For instance:")
    print("#*")
    print('**')
    print("will become")
    print("*#")
    print("#*")
    print("So, in this game, you can only click on '#' and the goal is to make '#'")
    print("all the space, and the last '#' you click would not become '*")
    print("-----------------------------------------------------------------------")
    print("SO, GAME START!")

def function(map, n): # function for how the game works
    """Returns "Congratulation" if the map has been fulfilled else return the function itself to continue working

    Parameters
    ----------
    map : array
        Two-dimensional array that stores the '#' and '*'
    n : integer
        The length of the array map

    Returns
    -------
    function() : function
        Function that let the user to play the game by entering their choices

    "Congratulation" : string
        Returns "Congratulation" on the screen
    """

    check = False # set variable check as False

    for x in range(n): # for loop within a range of n
        for y in range(n): # for loop within a range of n
            print(map[x][y], end='') # print out the element at row x and column y in map array with no change of the line
        print("") # switch to the next line

    row = int(input("Please enter a row\n>")) # ask for input and store in row
    column = int(input("Please enter a column\n>")) # ask for input and store in column

    while (row > n or row < 0) or (column > n or column < 0) or (map[row - 1][column - 1] == '*'): # check row and column are within the range and check the position in map also matches
        print("----------------------Invalid move--------------------------") # print out the notification
        row = int(input("Please enter a valid row\n>")) # reenter the row
        column = int(input("Please enter a valid column\n>")) # reenter the column
    
    # for the belowings:
    # first check whether row and column are out of bound
    # if not out of bound, check what is the position stored in map right now
    # turn into '#' if it is '*' else turn into '*'
    if row < n: 
        if map[row][column - 1] == '*': 
            map[row][column - 1] = '#' 
        else:
            map[row][column - 1] = '*'
    if column < n:
        if map[row - 1][column] == '*': 
            map[row - 1][column] = '#'
        else:
            map[row - 1][column] = '*'
    if row - 2 >= 0:
        if map[row - 2][column - 1] == '*':
            map[row - 2][column - 1] = '#'
        else:
            map[row - 2][column - 1] = '*'
    if column - 2 >= 0:
        if map[row - 1][column - 2] == '*':
            map[row - 1][column - 2] = '#'
        else:
            map[row - 1][column - 2] = '*'
    
    # for these belowings:
    # check whether each position in map is '#'
    # if yes then check is True else Check is False
    for i in range(n):
        for j in range(n): 
            if map[i][j] == '#': 
                check = True 
            else:
                check = False
                break
        if check == False:
            break

    map[row - 1][column - 1] = '*' # turn its original position in map as '*'

    if check == False: # if check is False which means the game is not finished
        return function(map, len(map)) # call the function itself to run again
    else:
        return "Congratulation!!" # else return the words

def customize(): # function to customize the game
    """
    Create a two-dimensional array according to the requirement of the user

    Parameters
    ----------
    None

    Returns
    -------
    customize_map : array
        Returns the two-dimensional array that contains '#' and '*'
    """
    
    # For the belowings:
    # To initialize the size of map and number of '#' in the map
    # And initialize the map according to the requirement
    n = int(input("How many nxn do you want to have\n>"))
    num = int(input("How many '#' do you want to have\n>"))
    customize_map = [['*' for x in range(n)] for j in range(n)]
    position = [] # array to store position of '#'

    # For the belowings:
    # To randomly generate position for '#' and store it in the position
    for count in range(num):
        coordinates = [random.randint(0, n - 1), random.randint(0, n - 1)]
        while coordinates in position == True: # to avoid repeated position
            coordinates = [random.randint(0, n - 1), random.randint(0, n - 1)]
        position.append(coordinates)

    # initialize '#' in the map    
    for coordinate in position:
        customize_map[coordinate[0]][coordinate[1]] = '#'

    return customize_map # return the customize_map

def main_page(): # Function for storing main menu
    """Print out the menu that the user could choose

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    
    # For the belowings: print out the main_page 
    print("---------------------------------------")
    print("              Level 1                  ")
    print("              Level 2                  ")
    print("              Level 3                  ")
    print("             Customize                 ")
    print("---------------------------------------")


def run(flag=False): # function that call all other function to run the game
    """
     The function that combines all other sub-functions to make the game running

     Parameters
     ----------
     flag : boolean
        To check whether it needs to print out the introduction() again and with a default value False

     Returns
     -------
     run : function
         Returns the function itself after the user has accomplished one level 
     """
    
    if flag == False: # check whether the introduction has been given 
        introduction() # call the function

    main_page() # call the function
    Level = GameManager() # initialize GameManager object
    choice = input("Enter the entire name you want to have or enter 'quit' to quit\n>") # ask for user input to enter their choice
    
    if choice == 'quit': # if 'quit' is inputed
        print("Bye~~~~") # print out the response
    elif choice == 'Level 1': # if 'Level 1' entered
        print(function(Level.level1(), len(Level.level1()))) # call the function by passing the level 1 map in Level and the size of the map
        return run(flag=True) # call function itself again after passing the Level 1 game
    elif choice == 'Level 2': # if 'Level 2' entered
        print(function(Level.level2(), len(Level.level2()))) # call the function by passing the level 2 map in Level and the size of the map
        return run(flag=True) # call the function again
    elif choice == 'Level 3': # if 'Level 3' entered
        print(function(Level.level3(), len(Level.level3()))) # call the function by passing the level 3 map in Level and the size of the map
        return run(flag=True) # call the function again
    elif choice == 'Customize': # if 'Customize' entered
        current_map = customize() # let user customize the map
        print(function(current_map,len(current_map))) # then call the function to play
        return run(flag=True) # call the function again
    else:
        return run(flag=True) # if invalid input, then run the function again
