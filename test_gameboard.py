import unittest
from gameboard import GameBoard, BoardSquare, ChessGame
from gamepiece import Rook, Knight, Pawn, Queen, King, Bishop
from main import gameboard_creator
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

    def test_print_sample_board_8dim(self):
        print("")
        board_dim = 8
        set = GameBoard(board_dim)
        set.print_sample_board()

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

    def test_print_sample_board_7dim(self):
        print("")
        board_dim = 7
        set = GameBoard(board_dim)
        set.print_sample_board()

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

    def test_print_sample_board_3dim(self):
        print("")
        board_dim = 3
        set = GameBoard(board_dim)
        set.print_sample_board()

    # need to rework test so follows proper abstraction barriers!
    # test to see if list with positions is working, try to automate testing with for loop!
    def test_algebraic_start_pieces_dictionary(self):
        current_gameboard = ChessGame()

        # test top row of dictionary
        self.assertIsInstance(
            current_gameboard.get_piece_from_algebraic_dictionary("a7"), Rook)
        self.assertEqual(
            True, current_gameboard.get_piece_color_from_algebraic_dictionry("a7", "Black"))
        """
        self.assertIsInstance(
            pos_list["b7"].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, pos_list["b7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["c7"].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, pos_list["c7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["d7"].get_piece_on_spot(), Queen)
        self.assertEqual(
            True, pos_list["d7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["e7"].get_piece_on_spot(), King)
        self.assertEqual(
            True, pos_list["e7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["f7"].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, pos_list["f7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["g7"].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, pos_list["g7"].get_piece_on_spot().color_checker("Black"))
        self.assertIsInstance(
            pos_list["h7"].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, pos_list["h7"].get_piece_on_spot().color_checker("Black"))

        # test bottom row of dictionary
        self.assertIsInstance(
            pos_list["a0"].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, pos_list["a0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["b0"].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, pos_list["b0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["c0"].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, pos_list["c0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["d0"].get_piece_on_spot(), Queen)
        self.assertEqual(
            True, pos_list["d0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["e0"].get_piece_on_spot(), King)
        self.assertEqual(
            True, pos_list["e0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["f0"].get_piece_on_spot(), Bishop)
        self.assertEqual(
            True, pos_list["f0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["g0"].get_piece_on_spot(), Knight)
        self.assertEqual(
            True, pos_list["g0"].get_piece_on_spot().color_checker("White"))
        self.assertIsInstance(
            pos_list["h0"].get_piece_on_spot(), Rook)
        self.assertEqual(
            True, pos_list["h0"].get_piece_on_spot().color_checker("White"))

        # test row of black pawns
        for i in range(current_gameboard.game_dimension):
            self.assertIsInstance(pos_list["{}6".format(
                chr(ord("a") + i))].get_piece_on_spot(), Pawn)
            self.assertEqual(True, pos_list["{}6".format(
                chr(ord("a") + i))].get_piece_on_spot().color_checker("Black"))

        # test row of white pawns
        for i in range(current_gameboard.game_dimension):
            self.assertIsInstance(pos_list["{}1".format(
                chr(ord("a") + i))].get_piece_on_spot(), Pawn)
            self.assertEqual(True, pos_list["{}1".format(
                chr(ord("a") + i))].get_piece_on_spot().color_checker("White"))

    # makes sure in the position dictionary, the algrbeiac spaces holding refefrence to spots w/o pieces are correctly blank
    def test_algebraic_non_piece_places(self):
        current_gameboard = gameboard_creator(8)
        pos_list = current_gameboard.set_up_chess_dictionary()
        for i in range(2, 6):
            for j in range(current_gameboard.game_dimension):
                self.assertEqual(pos_list["{}{}".format(
                    chr(ord("a") + j), i)].get_piece_on_spot(), None)
"""


if __name__ == '__main__':
    unittest.main()
