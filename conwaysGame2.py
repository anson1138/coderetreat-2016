class ConwaysGame:
  def __init__(self, board):
    self.board = board

  def findNearbyNeighbors(self, coordX, coordY):
    # For every coordinate adjacent to X, Y
    # if board[x][y] is alive
    countState = 0
    listToCheck = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for offset in listToCheck:
  
      valueX = coordX + offset[0]
     
      valueY = coordY + offset[1] 
      
      
      if (valueX < 0) or (valueY < 0):
        continue
      # add to neighbor count
      if self.board[valueX][valueY]:
        countState +=1
       

    # return neighborCount
    return countState
    

    
    # 
    
    
