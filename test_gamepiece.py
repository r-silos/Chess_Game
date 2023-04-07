import unittest
from gamepiece import Gamepiece, Rook, Pawn, King, Knight, Queen, Bishop
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

    def test_top_and_bottom_start_pieces(self):
        set = GameBoard(8)
        set.set_start_chess_board()
        # test for top row
        self.assertIsInstance(
            set.board[0][0].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, set.board[0][0].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][1].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, set.board[0][1].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][2].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, set.board[0][2].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][3].get_piece_on_spot(), Queen)
        self.assertEqual(
            True, set.board[0][3].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][4].get_piece_on_spot(), King)
        self.assertEqual(
            True, set.board[0][4].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][5].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, set.board[0][5].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][6].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, set.board[0][6].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            set.board[0][7].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, set.board[0][7].get_piece_on_spot().color_checker("Black"))

        # test for bottom row
        self.assertIsInstance(
            set.board[7][0].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, set.board[7][0].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][1].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, set.board[7][1].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][2].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, set.board[7][2].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][3].get_piece_on_spot(), Queen)
        self.assertEqual(
            True, set.board[7][3].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][4].get_piece_on_spot(), King)
        self.assertEqual(
            True, set.board[7][4].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][5].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, set.board[7][5].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][6].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, set.board[7][6].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            set.board[7][7].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, set.board[7][7].get_piece_on_spot().color_checker("White"))

    def test_pawn_rows(self):
        set = GameBoard(8)
        set.set_start_chess_board()

        # check black row of pawns
        for i in range(8):
            self.assertIsInstance(
                set.board[1][i].get_piece_on_spot(), Pawn)

        # check white row of pawns
        for i in range(8):
            self.assertIsInstance(
                set.board[6][i].get_piece_on_spot(), Pawn)

    def test_print_board_with_pieces(self):
        set = GameBoard(8)
        set.set_start_chess_board()
        print("")
        set.print_board()


if __name__ == '__main__':
    unittest.main()
