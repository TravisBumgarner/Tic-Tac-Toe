import random
def easyAI(positions, spacesLeft, playerMarker = "o"):
    while True:
        randNumberRow = random.randint(0,2)
        randNumberCol = random.randint(0,2)
        if positions[randNumberRow][randNumberCol] == " ":
            positions[randNumberRow][randNumberCol] = playerMarker
            return positions
        elif spacesLeft == 0:
            return None
        else:
            continue
            
