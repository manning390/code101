# Tic Tac Toe
import random

# Print the board for the user
# Can specify via print flag that we want input numbers to be printed in empty spaces
def drawBoard(board, flag = True):
    printBoard = getBoardCopy(board)
    if flag:
        for i in range(0, 9):
            if isSpaceFree(board, i):
                printBoard[i] = i + 1
    print('   |   |')
    print(' {0} | {1} | {2}'.format(printBoard[0], printBoard[1], printBoard[2]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' {0} | {1} | {2}'.format(printBoard[3], printBoard[4], printBoard[5]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' {0} | {1} | {2}'.format(printBoard[6], printBoard[7], printBoard[8]))
    print('   |   |')

# Sets a letter in the board
def makeMove(board, letter, move):
    board[move] = letter

# Returns boolean on whether a space is empty or not
def isSpaceFree(board, move):
    return board[move] == ' '

# Get whether the player wants to play X or O
def inputPlayerLetter():
    letter = ''
    print('Do you want to be X or O?')
    while not (letter == 'X' or letter == 'O'):
        letter = input().upper()

    # Player is always the first element of this list
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# Ask a player for a move
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split(' ') or not isSpaceFree(board, int(move) - 1):
        print('What is your next move? (1-9)')
        move = input()
    return int(move) - 1

# Determine who goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# Ask the player if they want to play again
# Returns a boolean
def playAgain():
    print('Do you want to play again? (y/n)')
    return input().lower().startswith('y')

# Given a board and a letter determine if the letter has a winning state
def isWinner(b, l):
    # Given a board and a player's letter, this function returns True if that player has won.
    # we use b instead of board and l instead of letter so we don't type as much
    return ((b[0] == l and b[1] == l and b[2] == l) or # top
            (b[3] == l and b[4] == l and b[5] == l) or # middle
            (b[6] == l and b[7] == l and b[8] == l) or # bottom
            (b[0] == l and b[3] == l and b[6] == l) or # left
            (b[1] == l and b[4] == l and b[7] == l) or # center
            (b[2] == l and b[5] == l and b[8] == l) or # right
            (b[0] == l and b[4] == l and b[8] == l) or # top left to bottom right
            (b[6] == l and b[4] == l and b[2] == l))   # bottom left to top right

# Duplicate a board, to avoid a reference error
def getBoardCopy(board):
    bus = []
    for i in board:
        bus.append(i)
    return bus

# Most basic AI, chooses randomly
def getRandomMove(board):
    if isBoardFull(board):
        return None
    while True:
        move = random.randint(0, 8)
        if isSpaceFree(board, move):
            return move

# Checks if the board is full
# Returns boolean
def isBoardFull(board):
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Get the player letter
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Search for a winning move
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Search for blocking winning move
    for i in range(0, 9):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Grab a corner
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return move

    # Grab the center
    if isSpaceFree(board, 4):
        return 4

    # Grab a side
    return chooseRandomMoveFromList(board, [1, 3, 5, 7])


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard, false)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard, false)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
