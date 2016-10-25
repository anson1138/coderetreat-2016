class RandomService:
  def __init__(self, result):
    self.totalNumCalled = 0
    self.result = result

  def uniform(lo, hi):
    self.totalNumCalled += 1
    return self.result
