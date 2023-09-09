import funtions

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-","-"]
CurrentPlayer = "X"
Winner = None
GameRunning = True
emptySpace = '-'

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('---------')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('---------')
    print(board[6] + " | " + board[7] + " | " + board[8])

def PutImputOnBoard(input):
    board[input-1] = CurrentPlayer

def checkMove(Input):
    print(Input)
    if Input == False:
        print ("Numero invalido!")
        playerInput()
    elif Input >= 1 and Input <= 9:
        print ("Numero invalido!")
        playerInput()
    elif board[input-1] != emptySpace:
        print ("Posicao ocupada!")
        playerInput()
    else:
        return True
        

def playerInput():
    Player_Input = funtions.isInteger(input("Digite um numero de 1 a 9: "))
    if checkMove(Player_Input) == True:
        PutImputOnBoard(playerInput)

        
    
        
playerInput()