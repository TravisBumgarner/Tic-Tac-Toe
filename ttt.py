import re #regular expressions

#Initial positions are all single whitespaces
positions = [None, #None acts as a spaceholder so board numbers line up correctly.
             " "," "," ",
             " "," "," ",
             " "," "," "]

#Board layout with spaces.
board = [positions[1]  + "|" + positions[2]  + "|" + positions[3],
        "-"           + "+" + "-" + "+"     + "-"              ,  
        positions[4]  + "|" + positions[5]  + "|" + positions[6],  
        "-"           + "+" + "-" + "+"     + "-"              ,  
        positions[7]  + "|" + positions[8]  + "|" + positions[9]]

def intro():
    print("The positions are shown below as p1 to p9.")
    print("When it's you're turn, pick a position and")
    print("type it in when prompted.")
    print(   "1|2|3\n" +
             "-+-+-\n" +
             "4|5|6\n" +
             "-+-+-\n" +
             "7|8|9\n")

def checkWinner(gameBoard):
    for eachRow in gameBoard:
        if eachRow[0] == "o" and eachRow[2] == "o" and eachRow[4] == "o": print("o wins!")
        if eachRow[0] == "x" and eachRow[2] == "x" and eachRow[4] == "x": print("x wins!")

def playGame():
    currentTurnLetter = "x"
    spacesLeft = 9
    while True:   
        if spacesLeft == 0:
             print("Game tied.")
             break
        try:
            position = int(input("It is " + currentTurnLetter + "'s turn. Where would you like to go? "))
            if position >=1 and position <=9 and positions[position] == " ":
                positions[position] = currentTurnLetter
            elif positions[position] != " ":
                print("Current space is already taken. Please select another location")
                continue
        except (IndexError, ValueError):
            print("Please enter a valid location")
            continue
            
        if currentTurnLetter == "x": currentTurnLetter = "o"
        elif currentTurnLetter == "o": currentTurnLetter = "x"
        spacesLeft -= 1
        board = [[positions[1]  + "|" + positions[2]  + "|" + positions[3]],
            ["-"           + "+" + "-" + "+"     + "-"              ],  
            [positions[4]  + "|" + positions[5]  + "|" + positions[6]],  
            ["-"           + "+" + "-" + "+"     + "-"              ],  
            [positions[7]  + "|" + positions[8]  + "|" + positions[9]]]
        for row in board:
             print(row)
        checkWinner(board)             

def main():
    intro()
    playGame()


    
