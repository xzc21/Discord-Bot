import random
import copy

class TicTacToe():

  def __init__(self):
    """Initiates required game variables"""
    self.board = [['-' for i in range(3)] for j in range(3)]
    self.PlayerPlayed = True
    
  def CheckWin(self, board):
    """Checks to see whether either the user of the CPU has won the game"""
    if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
        return 'tie'
    for i in range(3):
      if board[i] == ['X','X','X']:
        return 'player'
      elif board[i] == ['O','O','O']:
        return 'cpu'
      elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
        return 'player'
      elif board[0][i] == 'O' and self.board[1][i] == 'O' and board[2][i] == 'O':
        return 'cpu'
      elif board[0][0] == 'X' and self.board[1][1] == 'X' and board[2][2] == 'X':
        return 'player'
      elif board[0][0] == 'O' and self.board[1][1] == 'O' and board[2][2] == 'O':
        return 'cpu'
      elif board[0][2] == 'X' and self.board[1][1] == 'X' and board[2][0] == 'X':
        return 'player'
      elif board[0][2] == 'O' and self.board[1][1] == 'O' and board[2][0] == 'O':
        return 'player'
    return False

  def PlayerInput(self, input):
    """Get's the user's input and plays their piece if the input is valid"""
    row = input.upper()[0]
    column = int(input.upper()[1])-1
    rowMap = {'A':0, 'B':1, 'C':2}

    if self.board[rowMap[row]][column] == '-':
      self.board[rowMap[row]][column] = 'X'
      self.PlayerPlayed = True
    else:
      self.PlayerPlayed = False
    

  def CPUTurn(self):
    """Makes the CPU pick a random point to play their piece"""
    # row = random.randint(0,2)
    # column = random.randint(0,2)

    # if self.board[row][column] == '-':
    #   self.board[row][column] = 'O'
    # else:
    #   self.CPUTurn()

    #brute forcing algo
    possibleMoves = []
    for i in range(3):
      for b in range(3):
        if self.board[i][b] == '-':
          possibleMoves.append([i, b])


    
    #check winning move
    for move in possibleMoves:
      boardCopy = copy.deepcopy(self.board)
      boardCopy[move[0]][move[1]] = 'O'
      if self.CheckWin(boardCopy) == 'cpu':
        print('a')
        self.board[move[0]][move[1]] = 'O'
        return None
    
    #check for blocking Win
    for move in possibleMoves:
      boardCopy = copy.deepcopy(self.board)
      boardCopy[move[0]][move[1]] = 'X' #check if the player wins
      if self.CheckWin(boardCopy) == 'player':
        self.board[move[0]][move[1]] = 'O'
        return None

    #check for center
    if self.board[1][1] == '-':
      self.board[1][1] = 'O'
      return None
    
    #check for corners
    for i in possibleMoves:
      if i in [[0,0], [2,2], [0,2], [2,0]]:
        self.board[i[0]][i[1]] = 'O'
        return None

    #otherwise just pick the first choice
    self.board[possibleMoves[0][0]][possibleMoves[0][1]] = 'O'
    return None


  def d(self, value):
    if (value == 'X'):
      return '❌'
    if (value == 'O'):
      return '⭕'
    else:
      return '⬛'

      
  def PrintBoard(self):
    """Creates a string that represents the game board for output on Discord"""
    boardOutput = '```  1  2  3'
    boardOutput += f'\nA {self.d(self.board[0][0])}{self.d(self.board[0][1])}{self.d(self.board[0][2])}'
    boardOutput += f'\nB {self.d(self.board[1][0])}{self.d(self.board[1][1])}{self.d(self.board[1][2])}'
    boardOutput += f'\nC {self.d(self.board[2][0])}{self.d(self.board[2][1])}{self.d(self.board[2][2])}```'
    
    return boardOutput