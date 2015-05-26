from pprint import pformat


class Board:
  def __init__(self, board_size, live_coords):
    self.cells = [
      [Cell() for i in range(0, board_size)]
      for i in range(0, board_size )
    ]
    for x, y in live_coords:
      self.cells[x][y].is_alive = True

  # def get_living_cells(self):
  #   living = []
  #   #for i in range()
  #   #return []

  def __repr__(self):
    return pformat(self.cells)

class Cell:
  def __init__(self, is_alive=False):
    self.is_alive = is_alive

  def __repr__(self):
    return str(int(self.is_alive))

if __name__ == '__main__':
  board = Board(10, [(0,0),(0,1),(1,0),(1,1)])
  import pdb; pdb.set_trace()
