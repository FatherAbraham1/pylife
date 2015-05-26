import unittest
from life import Board

class TestLifeMethods(unittest.TestCase):

  def test_001_board_cells(self):
      board = Board(2, [(0,0),(0,1),(1,0),(1,1)])
      # print(board)
      self.assertEqual(len(board.cells), 2)

  def test_002_live_cell_is_alive(self):
      board = Board(2, [(0,0),(0,1),(1,0),(1,1)])
      are_alive = all(c.is_alive for c in sum(board.cells, []))
      #are_alive = all(for i = 0; i++ ; i< 2; do all([c.is_alive for c in board.cells[i]]))
      self.assertEqual(are_alive, True)

if __name__ == '__main__':
    unittest.main()