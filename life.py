from pprint import pformat
import copy

class Board:
  def __init__(self, board_size, live_coords):
    self.board_size = board_size
    self.cells = [
      [Cell() for i in range(0, board_size)]
      for i in range(0, board_size )
    ]
    for x, y in live_coords:
      self.cells[x][y].is_alive = True

  def tick(self):
    new_board = Board(self.board_size, [])

    for i, row in enumerate(self.cells):
      for j, cell in enumerate(row):
        north = self.cells[(i-1) % self.board_size][j]
        south = self.cells[(i+1) % self.board_size][j]
        east = self.cells[i][(j+1) % self.board_size]
        west = self.cells[i][(j-1) % self.board_size]

        ne = self.cells[(i-1) % self.board_size][(j+1) % self.board_size]
        nw = self.cells[(i-1) % self.board_size][(j-1) % self.board_size]
        se = self.cells[(i+1) % self.board_size][(j+1) % self.board_size]
        sw = self.cells[(i+1) % self.board_size][(j-1) % self.board_size]

        neighbors = [north, south, east, west, ne, nw, se, sw]
        living = sum(map(lambda x: x.is_alive, neighbors))

        if living == 2:
          new_board.cells[i][j] = cell
        elif living == 3:
          new_board.cells[i][j] = Cell(True)
    self.cells = new_board.cells

  # def get_living_cells(self):
  #   living = []
  #   #for i in range()
  #   #return []

  def __repr__(self):
    return pformat(self.cells).replace(",", "").replace("[", "").replace("]", "").replace("\n", "")

class Cell:
  def __init__(self, is_alive=False):
    self.is_alive = is_alive

  def __repr__(self):
    return "*" if self.is_alive else " "

if __name__ == '__main__':
  board = Board(10, [(0,0),(0,1),(1,0),(1,1)])
  import pdb; pdb.set_trace()
