import funtions
import random

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

def CheckHorizontal():
    global Winner
    global CurrentPlayer
    if board[0] == board[1] == board[2] and board[1] != '-':
        Winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[4] != '-':
        Winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[7] != '-':
        Winner = board[6]
        return True
    
def CheckVertical():
    global Winner
    global CurrentPlayer
    if board[0] == board[3] == board[6] and board[0]!= '-':
        Winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1]!= '-':
        Winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2]!= '-':
        Winner = board[2]
        return True
    
def CheckDiagonal():
    global Winner
    if board[0] == board[4] == board[8] and board[0]!= '-':
        Winner = board[4]
        return True
    if board[2] == board[0] == board[6] and board[2]!= '-':
        Winner = board[2]
        return True
    
def CheckForWinner():
    global GameRunning
    if CheckHorizontal() or CheckVertical() or CheckDiagonal():
        printBoard(board)
        print(f"O vencedor é {Winner}")
        GameRunning = False
    
def CheckTie():
    global GameRunning
    if '-' not in board and Winner == None:
        print("É um empate")
        GameRunning = False
    else:
        return True
    

def SwitchPlayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"

def checkMove(Player_Input):
    if Player_Input == False:
        print ("Numero invalido!")
        return False
    if Player_Input <= 1 and Player_Input >= 9:
        print("Número fora do intervalo válido!")
        return False
    elif board[Player_Input-1] != emptySpace:
        print ("Posição ocupada!")
        return False
    else:
        return True
        
def checkMoveComputer(Player_Input):
    if Player_Input == False:
        return False
    if Player_Input <= 1 and Player_Input >= 9:
        return False
    elif board[Player_Input-1] != emptySpace:
        return False
    else:
        return True

def computer():
    global CurrentPlayer
    while CurrentPlayer == "O" and GameRunning:
        RandomNumber = random.randint(1,9)
        if checkMoveComputer(RandomNumber) == True:
            PutImputOnBoard(RandomNumber)
            SwitchPlayer()

def playerInput():
    while True:
        Player_Input = funtions.isInteger(input("Digite um numero de 1 a 9: "))
        if checkMove(Player_Input) == True:
            PutImputOnBoard(Player_Input)
            break
       


        
while GameRunning:
    printBoard(board)
    playerInput()
    CheckForWinner()
    CheckTie()
    SwitchPlayer()
    if GameRunning:
        computer()
        CheckForWinner()
        CheckTie()
    