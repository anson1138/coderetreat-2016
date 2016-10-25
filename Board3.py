import random

class Board3:
  def __init__(self):
    self.board = [[x for x in range(10)] for y in range(10)]
    for row in range(10):
      for col in range(10):
        randomNum = random.uniform(0, 1)
        if randomNum < .33:
          self.board[row][col] = True
        else:
          self.board[row][col] = False
