from collections import OrderedDict


# until i write a proper GUI Window, to enter the letters in positions, i will use the following board variable
board = OrderedDict()

       #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
board["A"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#A
board["B"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#B
board["C"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#C
board["D"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#D
board["E"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#E
board["F"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#F
board["G"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#G
board["H"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#H
board["I"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#I
board["J"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#J
board["K"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#K
board["L"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#L
board["M"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#M
board["N"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#N
board["O"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#O
       #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15


boardSize = [len(board.keys()), len(list(board.values())[0])] #it is now [15,15]


def printBoard(_board = board):
    #board is an optional argument of a Dictionary
    columnNumbering = "#     1    2    3    4    5    6    7    8    9    10   11   12   13   14   15"
    print(columnNumbering)
    for rowLetter, row in board.items(): #read the board
        print(rowLetter + ":\t" + str(row) + " #" + rowLetter) #print the board in the format we want
    print(columnNumbering)


def setLetterInPosition(letter,position):
    #position is a string, letter is a string e.g. position=A12 letter=Γ
    #check if the parameters are correct
    if (len(position)>=2 #position parameter has the correct size
            and len(letter)==1 #letter parameter has the correct size
            and position[1:].isdigit() #the column is defined as a number
            and position[0] in board.keys()  #the row is a character already in the board's rows
            and int(position[1:]) <= len(board[position[0]])): #the column is a number smaller than the boards max columns number
        row, column = position[0].upper(), position[1:] #get the column and the row from position string. Row is the character A-O and Column is the Number 1-15
        board[row][int(column)] = letter.upper() #set the letter to it's position in the dictionary-matrix, and ensure it is Uppercase
        print("Letter " + letter + " added in position " + position) #print a confirmation message
    else:
        print("Check you input!") #the input is somehow not correct, so inform the user!
    printBoard(board)

def getPositionsOfLettersOnBoard(_board=board):
    for j, (rowLetter, row) in enumerate(_board.items(), 1): # enumerate starting from 1
        for i, cell in enumerate(row, 1): # enumerate starting from 1
            if " " not in cell:
                print("Letter " + cell + " in " + str(i) + "," + str(j))




#################################################################################
############################################################    TESTING    AREA
setLetterInPosition("Z","A3")#debugging
getPositionsOfLettersOnBoard()#debugging