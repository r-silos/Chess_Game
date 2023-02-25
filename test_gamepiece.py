import unittest
from gamepiece import Gamepiece
from gameboard import GameBoard, BoardSquare


class TestGamePiece(unittest.TestCase):
    # QnD test case to see if testfile executes
    def test_able_to_run(self):
        self.assertEqual(10, 10)

    def test_able_to_get_xy_value(self):
        set = GameBoard(8)
        set.board[0][0].set_piece_on_spot(Gamepiece())
        self.assertEqual(set.board[0][0].piece_on_spot.get_x_position(), 0)
        self.assertEqual(set.board[0][0].piece_on_spot.get_y_position(), 7)


if __name__ == '__main__':
    unittest.main()
