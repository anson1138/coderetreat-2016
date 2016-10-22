import random

class ConwaysGame:
  NUM_OF_ROWS = 10

  game = [[x for x in range(NUM_OF_ROWS)] for y in range(NUM_OF_ROWS)]

  def createTable(self):
    for row in range(0, self.NUM_OF_ROWS):
      for col in range(0, self.NUM_OF_ROWS):
        chance = random.uniform(0, 1)
        self.game[row][col] = chance < .33

game = ConwaysGame()
game.createTable()
print(game.game)
