def intro():
    print("The positions are shown below as p1 to p9.")
    print("When it's you're turn, pick a position and")
    print("type it in when prompted.")
    print(   "1|2|3\n" +
             "-+-+-\n" +
             "4|5|6\n" +
             "-+-+-\n" +
             "7|8|9\n")

    #Initial positions are all single whitespaces
    global positions
    positions = [
                    [" "," "," "],
                    [" "," "," "],
                    [" "," "," "]
                ]
    #Board layout with spaces.
    global board
    board = [positions[0][0]  + "|" + positions[0][1]  + "|" + positions[0][2],
            "-"           + "+" + "-" + "+"     + "-"              ,  
            positions[1][0]  + "|" + positions[1][1]  + "|" + positions[1][2],  
            "-"           + "+" + "-" + "+"     + "-"              ,  
            positions[2][0] + "|" + positions[2][1]  + "|" + positions[2][2]]

def checkRowAndColDictionary(location):
    rowAndColDictionary = {
        1: [0,0], 2: [0,1], 3: [0,2],
        4: [1,0], 5: [1,1], 6: [1,2],
        7: [2,0], 8: [2,1], 9: [2,2]    
    }
    return rowAndColDictionary[location]

def checkWinner(gameBoard):
    for i in [0,1,2]:
        if gameBoard[i][0] == "o" and gameBoard [i][1] == "o" and gameBoard [i][2] == "o":
            print("o wins!")
            return True
        if gameBoard[0][i] == "o" and gameBoard [1][i] == "o" and gameBoard [2][i] == "o":
            print("o wins!")
            return True
        if gameBoard[i][0] == "x" and gameBoard [i][1] == "x" and gameBoard [i][2] == "x":
            print("x wins!")
            return True
        if gameBoard[0][i] == "x" and gameBoard [1][i] == "x" and gameBoard [2][i] == "x":
            print("x wins!")
            return True


def playGame():
    currentTurnLetter = "x"
    spacesLeft = 9
    while True:   
        if spacesLeft == 0:
             print("Game tied.")
             break
        try:
            print("It is " + currentTurnLetter + "'s turn. Where would you like to go? ")
            
            location = int(input("Which spot?"))
            row, col = checkRowAndColDictionary(location)
            #row = currentCellBeingPlayed[0]
            #col = currentCellBeingPlayed[1]
            if (row >=0 and row <=2) and (col >=0 and col <=2) and positions[row][col] == " ":
                positions[row][col] = currentTurnLetter
            elif positions[row][col] != " ":
                print("Current space is already taken. Please select another location")
                continue
        except (ValueError,KeyError,IndexError):
            print("Please enter a valid location")
            continue
            
        if currentTurnLetter == "x": currentTurnLetter = "o"
        elif currentTurnLetter == "o": currentTurnLetter = "x"
        spacesLeft -= 1
        board = [positions[0][0]  + "|" + positions[0][1]  + "|" + positions[0][2],
                "-"           + "+" + "-" + "+"     + "-"              ,  
                positions[1][0]  + "|" + positions[1][1]  + "|" + positions[1][2],  
                "-"           + "+" + "-" + "+"     + "-"              ,  
                positions[2][0] + "|" + positions[2][1]  + "|" + positions[2][2]]
        for row in board:
             print(row)
        if checkWinner(positions) == True:
            return None

def main():
    intro()
    playGame()


    
