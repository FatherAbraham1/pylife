import unittest
from life import Board

class TestLifeMethods(unittest.TestCase):
  def setUp(self):
        self.board_simple = Board(2, [(0,0),(0,1),(1,0),(1,1)])

  def test_001_board_cells(self):
      # print(board)
      self.assertEqual(len(self.board_simple.cells), 2)

  def test_002_live_cell_is_alive(self):
      are_alive = all(c.is_alive for c in sum(self.board_simple.cells, []))
      #are_alive = all(for i = 0; i++ ; i< 2; do all([c.is_alive for c in board.cells[i]]))
      self.assertEqual(are_alive, True)

if __name__ == '__main__':
    unittest.main()