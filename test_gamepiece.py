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
            set.board[0][0].get_piece_on_spot(), type(Rook("Black")))
        self.assertIsInstance(
            set.board[0][1].get_piece_on_spot(), type(Knight("Black")))
        self.assertIsInstance(
            set.board[0][2].get_piece_on_spot(), type(Bishop("Black")))
        self.assertIsInstance(
            set.board[0][3].get_piece_on_spot(), type(Queen("Black")))
        self.assertIsInstance(
            set.board[0][4].get_piece_on_spot(), type(King("Black")))
        self.assertIsInstance(
            set.board[0][5].get_piece_on_spot(), type(Bishop("Black")))
        self.assertIsInstance(
            set.board[0][6].get_piece_on_spot(), type(Knight("Black")))
        self.assertIsInstance(
            set.board[0][7].get_piece_on_spot(), type(Rook("Black")))

        # test for bottom row
        self.assertIsInstance(
            set.board[7][0].get_piece_on_spot(), type(Rook("White")))
        self.assertIsInstance(
            set.board[7][1].get_piece_on_spot(), type(Knight("White")))
        self.assertIsInstance(
            set.board[7][2].get_piece_on_spot(), type(Bishop("White")))
        self.assertIsInstance(
            set.board[7][3].get_piece_on_spot(), type(Queen("White")))
        self.assertIsInstance(
            set.board[7][4].get_piece_on_spot(), type(King("White")))
        self.assertIsInstance(
            set.board[7][5].get_piece_on_spot(), type(Bishop("White")))
        self.assertIsInstance(
            set.board[7][6].get_piece_on_spot(), type(Knight("White")))
        self.assertIsInstance(
            set.board[7][7].get_piece_on_spot(), type(Rook("White")))

    def test_pawn_rows(self):
        set = GameBoard(8)
        set.set_start_chess_board()

        # check black row of pawns
        for i in range(8):
            self.assertIsInstance(
                set.board[1][i].get_piece_on_spot(), type(Pawn("Black")))

        # check white row of pawns
        for i in range(8):
            self.assertIsInstance(
                set.board[6][i].get_piece_on_spot(), type(Pawn("White")))

    def test_print_board_with_pieces(self):
        set = GameBoard(8)
        set.set_start_chess_board()
        print("")
        set.print_sample_board()


if __name__ == '__main__':
    unittest.main()
