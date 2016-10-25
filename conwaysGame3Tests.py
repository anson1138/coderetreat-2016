import unittest
from conwaysGame3 import ConwaysGame
from TestBoard import TestBoard

class TestConwaysGame(unittest.TestCase):

    def testNearbyNeighbors(self):
        board = TestBoard([[True, True, False], [False, False, True], [True, True, True]])
        game = ConwaysGame(board)
        self.assertEquals(game.numNearbyNeighbors(1, 1), 6)
        
              

if __name__ == '__main__':
    unittest.main()
