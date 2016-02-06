from collections import OrderedDict


# until i write a proper GUI Window, to enter the letters in positions, i will use the following board variable
board = OrderedDict()

       #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
board["Α"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Α
board["Β"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Β
board["Γ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Γ
board["Δ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Δ
board["Ε"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ε
board["Ζ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ζ
board["Η"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Η
board["Θ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Θ
board["Ι"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ι
board["Κ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Κ
board["Λ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Λ
board["Μ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Μ
board["Ν"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ν
board["Ξ"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ξ
board["Ο"]=[   " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "  ]#Ο
       #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15


cellBonuses = OrderedDict()
             #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
cellBonuses["Α"]=[   "T", " ", " ", "d", " ", " ", " ", "T", " ", " ", " ", "d", " ", " ", "T"  ]#Α
cellBonuses["Β"]=[   " ", "D", " ", " ", " ", "t", " ", " ", " ", "t", " ", " ", " ", "D", " "  ]#Β
cellBonuses["Γ"]=[   " ", " ", "D", " ", " ", " ", "d", " ", "d", " ", " ", " ", "D", " ", " "  ]#Γ
cellBonuses["Δ"]=[   "d", " ", " ", "D", " ", " ", " ", "d", " ", " ", " ", "D", " ", " ", "d"  ]#Δ
cellBonuses["Ε"]=[   " ", " ", " ", " ", "D", " ", " ", " ", " ", " ", "D", " ", " ", " ", " "  ]#Ε
cellBonuses["Ζ"]=[   " ", "t", " ", " ", " ", "t", " ", " ", " ", "t", " ", " ", " ", "t", " "  ]#Ζ
cellBonuses["Η"]=[   " ", " ", "d", " ", " ", " ", "d", " ", "d", " ", " ", " ", "d", " ", " "  ]#Η
cellBonuses["Θ"]=[   "T", " ", " ", "d", " ", " ", " ", "D", " ", " ", " ", "d", " ", " ", "t"  ]#Θ
cellBonuses["Ι"]=[   " ", " ", "d", " ", " ", " ", "d", " ", "d", " ", " ", " ", "d", " ", " "  ]#Ι
cellBonuses["Κ"]=[   " ", "t", " ", " ", " ", "t", " ", " ", " ", "t", " ", " ", " ", "t", " "  ]#Κ
cellBonuses["Λ"]=[   " ", " ", " ", " ", "D", " ", " ", " ", " ", " ", "D", " ", " ", " ", " "  ]#Λ
cellBonuses["Μ"]=[   "d", " ", " ", "D", " ", " ", " ", "d", " ", " ", " ", "D", " ", " ", "d"  ]#Μ
cellBonuses["Ν"]=[   " ", " ", "D", " ", " ", " ", "d", " ", "d", " ", " ", " ", "D", " ", " "  ]#Ν
cellBonuses["Ξ"]=[   " ", "D", " ", " ", " ", "t", " ", " ", " ", "t", " ", " ", " ", "D", " "  ]#Ξ
cellBonuses["Ο"]=[   "T", " ", " ", "d", " ", " ", " ", "T", " ", " ", " ", "d", " ", " ", "T"  ]#Ο
             #        1    2    3    4    5    6    7    8    9    10   11   12   13   14   15



boardSize = [len(board.keys()), len(list(board.values())[0])] #it is now [15,15]

def printSeparator(length, symbol):
    print("\n" + str(symbol)*int(length))


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
    print("\n\t\t\t\t\t\t\t NEW  BOARD  STATE")
    printBoard(board)


def getPositionsOfLettersOnBoard(_board=board):
    printSeparator(25, "_")
    for j, (rowLetter, row) in enumerate(_board.items(), 1): # enumerate starting from 1
        for i, cell in enumerate(row, 1): # enumerate starting from 1
            if " " not in cell:
                print("\tLetter " + cell + " in " , i, "," , j)


def setWordOnBoard(_word, _startingPosition, _horizontal=True):
    _position = [_startingPosition[0], int(_startingPosition[1:])-1 ] # [letter, number]
    if _horizontal:
        for _letter in _word:
            setLetterInPosition(letter=_letter,position= ''.join(str(pos) for pos in _position))
            _position[1] += 1 # set position for the next column
    else:
        for _letter in _word:
            setLetterInPosition(letter=_letter,position= ''.join(str(pos) for pos in _position))
            _position[0] = chr(ord(_position[0]) + 1)#Read the letter as byte, increase it by 1 and convert it back to letter


def getWordsOnBoard(_board=board):
    printSeparator(88, "_")
    wordsList = {"horizontally"  :[],
                 "vertically"     :[]}
    for rowLetter, row in _board.items():
        wordsList["horizontally"].append(''.join(cell.replace(" ","*") for cell in row))
    for columnNum in range(boardSize[1]):
        wordsList["vertically"].append(''.join(word[columnNum] for word in wordsList["horizontally"]))

    print("Horizontal words:\n\t", wordsList["horizontally"])#debugging
    print("Vertical words:\n\t", wordsList["vertically"])#debugging
    print("\t\t\tThe '*' represents (here) an empty space on the board that can take any letter")#debugging





########################################################################################################
########################################################################################################

if __name__ == "__main__":
    print("board.py is being run directly")

    setWordOnBoard("ΖΑΡΙ", "Α3")#debugging
    setWordOnBoard("ΖΩΑ", "Α3", False)#debugging
    setWordOnBoard("ΑΛΛΟ", "Α10")#debugging
    setWordOnBoard("ΛΕΜΟΝΙ", "Α11", False)#debugging
    setWordOnBoard("ΡΕΜΑ", "Α6", False)#debugging
    setWordOnBoard("ΚΟΜΜΑΤΙ", "Γ8")#debugging
    setWordOnBoard("ΚΑΡΕΚΛΑ", "Γ8", False)#debugging
    setWordOnBoard("ΛΕΚΑΝΗ", "Θ8")#debugging
    getWordsOnBoard()#debugging
else:
    print("board.py is being imported into another module")