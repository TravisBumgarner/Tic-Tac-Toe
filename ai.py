import random
def easyAI(positions, spacesLeft, computerMarker = "o"):
    while True:
        randNumberRow = random.randint(0,2)
        randNumberCol = random.randint(0,2)
        if positions[randNumberRow][randNumberCol] == " ":
            positions[randNumberRow][randNumberCol] = computerMarker
            return positions
        elif spacesLeft == 0:
            return None
        else:
            continue
def printRowsOfGameBoard(gameBoard):
    for each in gameBoard:
        print(str(each))

def analyzeBestPlay(positions,computerMarker,playerMarker):
    #rowAnalysis checks each row for quantity of x markers, o markers, and empty spaces.
    rowAnalysis = []
    for rowIndex, row in enumerate(positions):
        emptyCells = []
        emptyCellsCount = 0
        computerCounter = 0
        playerCounter = 0
        for cellIndex, cell in enumerate(row): #Go through each row and check how many x's and o's are there.
            if cell == computerMarker:
                computerCounter +=1
            elif cell == playerMarker:
                playerCounter +=1
            else: #This line sets the location of an empty cell in a row. This is only used if one and only one cell is empty for making a move in the next few lines of code.
                emptyCells.append([rowIndex,cellIndex])
                emptyCellsCount +=1
        #Creates list of analyzed rows including the number of the row, how many markers the computer and player have and where the empty spaces are.
        rowAnalysis.append([rowIndex, computerCounter, playerCounter, emptyCells])
    print("The rowAnalysis is")
    printRowsOfGameBoard(rowAnalysis)
    playAnalysis = []
    #Play analysis will check each potential spot to move and give it a rating.
    #15 = win
    #10 = add a second marker to a row
    #5  = add a single marker to an empty row
    #0  = add a single marker to a non-empty row (Probably just going for a tie
    #-1 = unassigned value to a play
    #I picked spaced out numbers so that I could weigh different conditions later and they'd be easier to add. 
    for each in rowAnalysis:
        #Each row in rowAnalysis is laid out as: [rowIndex, computerCounter, playerCounter, emptyCells]
        playValue = -1
        rowIndex = each[0]
        computerCounter = each[1]
        playerCounter = each[2]
        emptyCells = each[3]
        if computerCounter == 2 and playerCounter ==0:
            playValue = 15
            #This previous line of code should always lead to game over.
        elif computerCounter == 1 and playerCounter == 0:
            #This will find a row with a single computerMarker and no playerMarker and go there.
            playValue = 10
        elif computerCounter == 0 and playerCounter == 0:
            playValue = 5
        else:
            playValue = 0
        if len(emptyCells) > 1:
            #If there is more emptyCells than 1, in the cases of there being a single or no marker in a row, the computer will randomly pick a move 
            randomEmptyCell = random.randint(0,len(emptyCells)-1)
            emptyCells = emptyCells[randomEmptyCell]
        playAnalysis.append([playValue,emptyCells])
    print("The playAnalysis is")
    printRowsOfGameBoard(playAnalysis)
    return playAnalysis
            
    

def mediumAI(positions, spacesLeft, computerMarker = "o"):
    if computerMarker == "o": playerMarker = "x"
    elif computerMarker == "x": playerMarker = "o"
    analyzeBestPlay(positions,computerMarker,playerMarker)
    easyAI(positions,spacesLeft)


positions = [
                    ["x","x"," "],
                    ["o","o"," "],
                    [" ","o","x"]
                ]
mediumAI(positions,4)

        
            
            
            
            



'''
In case I need it:

    def checkWinner(gameBoard):
    for i in [0,1,2]:
        if ((gameBoard[i][0] == "o" and gameBoard [i][1] == "o" and gameBoard [i][2] == "o") or
            (gameBoard[0][i] == "o" and gameBoard [1][i] == "o" and gameBoard [2][i] == "o")):
            print("o wins!")
            return True        
        elif ((gameBoard[i][0] == "x" and gameBoard [i][1] == "x" and gameBoard [i][2] == "x") or
              (gameBoard[0][i] == "x" and gameBoard [1][i] == "x" and gameBoard [2][i] == "x")):
            print("x wins!")
            return True
    if ((gameBoard[0][0] == "o" and gameBoard [1][1] == "o" and gameBoard [2][2] == "o") or
        (gameBoard[0][2] == "o" and gameBoard [1][1] == "o" and gameBoard [2][0] == "o")):
            print("o wins!")
            return True

    if ((gameBoard[0][0] == "x" and gameBoard [1][1] == "x" and gameBoard [2][2] == "x") or
        (gameBoard[0][2] == "x" and gameBoard [1][1] == "x" and gameBoard [2][0] == "x")):
            print("x wins!")
            return True

'''
