import random

class Cell:
  def __init__(self, isLive):
    self.isLive = isLive

  def __repr__(self):
    if self.isLive:
      return 'X'
    else:
      return ' '



class ConwaysGame:
  NUM_OF_ROWS = 10

  def __init__(self):
    self.game = [[x for x in range(self.NUM_OF_ROWS)] for y in range(self.NUM_OF_ROWS)] #type: bool

  def createTable(self):
    for row in range(0, self.NUM_OF_ROWS):
      for col in range(0, self.NUM_OF_ROWS):
        chance = random.uniform(0, 1)
        self.game[row][col] = Cell(chance < .33)

  def printGame(self):
    for row in range(0, len(self.game)):
      for col in range(0, len(self.game[0])):
        print(self.game[row][col], end='')
      print()

  def makeMove(self):
    updated_game = [[x for x in range(self.NUM_OF_ROWS)] for y in range(self.NUM_OF_ROWS)]
    for row in range(0, self.NUM_OF_ROWS):
      for col in range(0, self.NUM_OF_ROWS):
        numAdjLiving = 0
        if row-1 >= 0: # row before
          if self.game[row-1][col].isLive:
            numAdjLiving += 1
          if col-1 >= 0:
            if self.game[row-1][col-1].isLive:
              numAdjLiving += 1
          if col+1 < self.NUM_OF_ROWS:
            if self.game[row-1][col+1].isLive:
              numAdjLiving += 1

        if row+1 < self.NUM_OF_ROWS: # row after
          if self.game[row+1][col].isLive:
            numAdjLiving += 1
          if col-1 >= 0:
            if self.game[row+1][col-1].isLive:
              numAdjLiving += 1
          if col+1 < self.NUM_OF_ROWS:
            if self.game[row+1][col+1].isLive:
              numAdjLiving += 1

        if col-1 >= 0: # same row
          if self.game[row][col-1].isLive:
            numAdjLiving += 1
        if col+1 < self.NUM_OF_ROWS:
          if self.game[row][col+1].isLive:
            numAdjLiving += 1
        
        if self.game[row][col].isLive:
          if numAdjLiving < 2:
            updated_game[row][col] = Cell(False)
          elif numAdjLiving < 4:
            updated_game[row][col] = Cell(True)
          else:
            updated_game[row][col] = Cell(False)
        else:
          if numAdjLiving == 3:
            updated_game[row][col] = Cell(True)
          else:
            updated_game[row][col] = Cell(False)

    self.game = updated_game

  def playGame(self, moves):
    for _ in range(moves):
      self.makeMove()
      self.printGame()
      print()


game = ConwaysGame()
game.createTable()
game.printGame()
print()
game.playGame(4)
