#Function to print the Tic-Tac-Toe Design
def myTicTacToe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")

# Function to print the score-board
def myScoreboard(scoreboard):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")
    listofplayers = list(scoreboard.keys())
    print("\t   ", listofplayers[0], "\t    ", scoreboard[listofplayers[0]])
    print("\t   ", listofplayers[1], "\t    ", scoreboard[listofplayers[1]])
    print("\t--------------------------------\n")

#Defining Function to check Victory
def check_victory(playerPos, curPlayer):

    #All probable winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    #Loop to check whether any winning combination is satisfied or not
    for i in solution:
        if all(j in playerPos[curPlayer] for j in i):
            
            #Return True if any winning combination is satisfied
            return True
    #Return False if no combination is satisfied
    return False

#Defining Function to check if the game is Tied
def check_tie(playerPos):
    if len(playerPos['X']) + len(playerPos['O']) == 9:
        return True
    return False

#Function for a single game of Tic-Tac-Toe
def singleGame(curPlayer):
    #Representing the Tic-Tac_Toe
    val = [' 'for i in range(9)]

    #Storing the positions occupied by X and O
    playerPos = {'X': [], 'O': []}

    #Loop of Game for a single game of Tic-Tac-Toe
    while True:
        myTicTacToe(val)
        #Try-Exception block for CHANCE input
        try:
            print("Player",curPlayer,"turn.Choose your Block:", end="")
            chance = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue
        
        #Sanity check for CHANCE input
        if chance < 1 or chance > 9:
            print("Invalid Input!!! Try Again")
            continue

        #Checking if the block is not occupied already
        if val[chance-1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue

        #updating the game information

        #Update the status of the grid
        val[chance - 1] = curPlayer

        #Update the positions of the player
        playerPos[curPlayer].append(chance)

        #Calling Function to check Victory
        if check_victory(playerPos, curPlayer):
            myTicTacToe(val)
            print("Congratulations! Player ", curPlayer," has won the game!")
            print("\n")
            return curPlayer
        
        #Calling Function to check Tie
        if check_tie(playerPos):
            myTicTacToe(val)
            print("Oh! Game Tied")
            print("\n")
            return'D'
        
        #Switching moves of the player
        if curPlayer == 'X':
            curPlayer = 'O'
        else:
            curPlayer = 'X'

if __name__ == "__main__":

    print("First Player")
    firstPlayer = input("Specify the Name:")
    print("\n")

    print("Second Player")
    secondPlayer = input("Specify the Name:")
    print("\n")

    #Storing the player who chooses X and O
    curPlayer = firstPlayer

    #Storing the Players' choice
    playerChoice = {'X':"",'O':""}

    # Storing the options
    opt = ['X', 'O']

    #Storing the scoreboard
    scoreboard = {firstPlayer: 0, secondPlayer: 0}
    myScoreboard(scoreboard)

    #Loop for a series of Tic-Tac-Toe game
    #The loop executes until the players quit
    while True:

        #Main Menu for Players
        print(curPlayer, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")

        #Try execption for THE_CHOICE input
        try:
            the_choice = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again\n")
            continue

        #Conditions for player choice
        if the_choice == 1:
            playerChoice['X'] = curPlayer
            if curPlayer == firstPlayer:
                playerChoice['O'] = secondPlayer
            else:
                playerChoice['O'] = firstPlayer
        elif the_choice == 2:
            playerChoice['O'] = curPlayer
            if curPlayer == firstPlayer:
                playerChoice['X'] = secondPlayer
            else:
                playerChoice['X'] = firstPlayer
        elif the_choice == 3:
            print("The Final Scores")
            myScoreboard(scoreboard)
            break
        else:
            print("Invalid Selection!! Try Again\n")

        #Storing the winner in a single game of Tic-Tac-Toe
        win = singleGame(opt[the_choice-1])

        #Updating of the scoreboard as per the winner
        if win != 'D':
            playerWon = playerChoice[win]
            scoreboard[playerWon] = scoreboard[playerWon] + 1

        myScoreboard(scoreboard)

        #Switching player who chooses X or O
        if curPlayer == firstPlayer:
            curPlayer = secondPlayer
        else:
            curPlayer = firstPlayer