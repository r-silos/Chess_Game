import unittest
from gameboard import GameBoard, BoardSquare, ChessBoard
from gamepiece import Rook, Knight, Pawn, Queen, King, Bishop
# unit test video: https://www.youtube.com/watch?time_continue=763&v=6tNS--WetLI&embeds_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Drun%2Bunit%2Btests%2Bpython%26rlz%3D1C1ONGR_enUS976US976%26sxsrf%3DAJOqlzUWca9VYEDJSSuw8Gkgw8CYLJma6w%3A16766630&feature=emb_logo


class TestGameBoard(unittest.TestCase):

    # Qnd function just to check if able to run test
    def test_able_to_run(self):
        self.assertEqual(10, 10)

    def test_first_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[0][0].get_x_position(), 0)
        self.assertEqual(set.board[0][0].get_y_position(), 7)
        self.assertEqual(set.board[0][0].get_internal_label(), "a7")
        self.assertEqual(set.board[0][0].get_color(), "white")

    def test_second_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[0][1].get_x_position(), 1)
        self.assertEqual(set.board[0][1].get_y_position(), 7)
        self.assertEqual(set.board[0][1].get_internal_label(), "b7")
        self.assertEqual(set.board[0][0].get_color(), "white")

    def test_2ndlast_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[7][6].get_x_position(), 6)
        self.assertEqual(set.board[7][6].get_y_position(), 0)
        self.assertEqual(set.board[7][6].get_internal_label(), "g0")
        self.assertEqual(set.board[7][6].get_color(), "white")

    def test_last_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[7][7].get_x_position(), 7)
        self.assertEqual(set.board[7][7].get_y_position(), 0)
        self.assertEqual(set.board[7][7].get_internal_label(), "h0")
        self.assertEqual(set.board[7][7].get_color(), "white")

    def test_middle_postion_added(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[4][4].get_x_position(), 4)
        self.assertEqual(set.board[4][4].get_y_position(), 3)
        self.assertEqual(set.board[4][4].get_internal_label(), "e3")
        self.assertEqual(set.board[4][4].get_color(), "white")

    def test_print_internal_labels_8dim(self):
        print("")
        board_dim = 8
        set = GameBoard(board_dim)
        set.display_gameboard_internal_labels()

    def test_print_xy_values_8dim(self):
        print("")
        board_dim = 8
        set = GameBoard(board_dim)
        set.display_gameboard_xy_values()

    def test_print_board_8dim(self):
        print("")
        board_dim = 8
        set = GameBoard(board_dim)
        set.print_board()

    def test_print_internal_labels_7dim(self):
        print("")
        board_dim = 7
        set = GameBoard(board_dim)
        set.display_gameboard_internal_labels()

    def test_print_xy_values_7dim(self):
        print("")
        board_dim = 7
        set = GameBoard(board_dim)
        set.display_gameboard_xy_values()

    def test_print_board_7dim(self):
        print("")
        board_dim = 7
        set = GameBoard(board_dim)
        set.print_board()

    def test_print_internal_labels_3dim(self):
        print("")
        board_dim = 3
        set = GameBoard(board_dim)
        set.display_gameboard_internal_labels()

    def test_print_xy_values_3dim(self):
        print("")
        board_dim = 3
        set = GameBoard(board_dim)
        set.display_gameboard_xy_values()

    def test_print_board_3dim(self):
        print("")
        board_dim = 3
        set = GameBoard(board_dim)
        set.print_board()

    # need to rework test so follows proper abstraction barriers!
    def test_algebraic_start_pieces_dictionary(self):
        current_gameboard = ChessBoard()

        # test top row of dictionary
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("a7"), Rook)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("a7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("b7"), Knight)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("b7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("c7"), Bishop)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("c7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("d7"), Queen)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("d7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("e7"), King)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("e7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("f7"), Bishop)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("f7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("g7"), Knight)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("g7", "Black"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("h7"), Rook)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("h7", "Black"))

       # test bottom row of dictionary
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("a0"), Rook)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("a0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("b0"), Knight)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("b0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("c0"), Bishop)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("c0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("d0"), Queen)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("d0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("e0"), King)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("e0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("f0"), Bishop)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("f0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("g0"), Knight)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("g0", "White"))
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("h0"), Rook)
        self.assertEqual(
            True, current_gameboard.check_piece_color_from_dictionary("h0", "White"))

        for i in range(current_gameboard.game_dimension):
            # logic to check the black pawn row
            self.assertIsInstance(current_gameboard.get_piece_from_algebraic_dictionary(
                "{}6".format(chr(ord("a") + i))), Pawn)
            self.assertEqual(True, current_gameboard.check_piece_color_from_dictionary("{}6".format(
                chr(ord("a") + i)), "Black"))
            # logic to check the white pawn row
            self.assertIsInstance(current_gameboard.get_piece_from_algebraic_dictionary(
                "{}1".format(chr(ord("a") + i))), Pawn)
            self.assertEqual(True, current_gameboard.check_piece_color_from_dictionary("{}1".format(
                chr(ord("a") + i)), "White"))

    # this tests the remaining spots on position dictionary, which should have no pieces on it
    def test_start_algebraic_blank_spaces(self):
        current_gameboard = ChessBoard()
        for i in range(2, 6):
            for j in range(current_gameboard.game_dimension):
                self.assertEqual(None, current_gameboard.get_piece_from_algebraic_dictionary(
                    "{}{}".format(chr(ord("a") + j), i)))

    def test_move_piece(self):
        current_game = ChessBoard()
        current_game.move_piece("a1", "a2")
        self.assertIsInstance(
            current_game.get_piece_from_algebraic_dictionary("a2"), Pawn)
        self.assertEqual(
            current_game.get_piece_from_algebraic_dictionary("a1"), None)
        print("\nWhite Pawn should have moved one")
        current_game.print_board()
        """print("the x coordinate for the moved piece is: {}".format(
            current_game.get_piece_from_algebraic_dictionary("a2").get_x_position()))
        print("the y coordinate for the moved piece is: {}".format(
            current_game.get_piece_from_algebraic_dictionary("a2").get_y_position()))
        """
        self.assertEqual(current_game.get_piece_from_algebraic_dictionary(
            "a2").get_x_position(), 0)
        self.assertEqual(current_game.get_piece_from_algebraic_dictionary(
            "a2").get_y_position(), 2)
        print("White Queen moved up 3 and right 3")
        current_game.move_piece("d0", "g3")
        current_game.print_board()
        self.assertIsInstance(
            current_game.get_piece_from_algebraic_dictionary("g3"), Queen)
        self.assertEqual(
            current_game.get_piece_from_algebraic_dictionary("d0"), None)
        self.assertEqual(current_game.get_piece_from_algebraic_dictionary(
            "g3").get_x_position(), 6)
        self.assertEqual(current_game.get_piece_from_algebraic_dictionary(
            "g3").get_y_position(), 3)


if __name__ == '__main__':
    unittest.main()
