import unittest
from conwaysGame2 import ConwaysGame

class TestGame(unittest.TestCase):

    def testNumOfNeighbors(self):
        board = [[True, False, True], [True, True, False], [False, True, True]]
        game = ConwaysGame(board)
        self.assertEquals(game.findNearbyNeighbors(1, 1), 5)

    def testNumOfNeighborsOnEdge(self):
        board = [[True, False, True], [True, True, False], [False, True, True]]
        game = ConwaysGame(board)
        self.assertEquals(game.findNearbyNeighbors(0, 0), 2)
        self.assertEquals(game.findNearbyNeighbors(2, 1), 3)

        

if __name__ == '__main__':
    unittest.main()
