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
        if len(emptyCells) != 0:
            #No need to analyze a row that's empty
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
        if len(emptyCells) == 0:
            emptyCells == None
        if len(emptyCells) > 1:
            #If there is more emptyCells than 1, in the cases of there being a single or no marker in a row, the computer will randomly pick a move 
            randomEmptyCell = random.randint(0,len(emptyCells)-1)
            emptyCells = [emptyCells[randomEmptyCell]]
        playAnalysis.append([playValue,emptyCells[0]]) #[0] for emptyCells because all the other list elements get stripped away 
    print("The playAnalysis is")
    printRowsOfGameBoard(playAnalysis)
    return playAnalysis  
    

def mediumAI(positions, spacesLeft, computerMarker = "o"):
    if computerMarker == "o": playerMarker = "x"
    elif computerMarker == "x": playerMarker = "o"
    pointValues = analyzeBestPlay(positions,computerMarker,playerMarker)
    #analyzeBestPlay returns playAnalysis that is a list of [playValue,emptyCell]
    playToMake = [-1,[-1,-1]]
    for pointValue in pointValues:
        if pointValue[0] > playToMake[0]:
            playToMake = pointValue
    print(playToMake)
    #print(playToMake)
    print(playToMake[0])
    playRow = playToMake[1][0]
    print(playToMake[1][1])
    playCol = playToMake[1][1]
    positions[playRow][playCol] = computerMarker
    return positions                             
positions = [
                    ["o","o"," "],
                    [" "," "," "],
                    [" "," "," "]
                ]
mediumAI(positions,4)
