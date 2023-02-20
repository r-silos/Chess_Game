import unittest
from gameboard import GameBoard, BoardSquare
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


if __name__ == '__main__':
    unittest.main()
