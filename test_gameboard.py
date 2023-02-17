import unittest
from gameboard import GameBoard
# unit test video: https://www.youtube.com/watch?time_continue=763&v=6tNS--WetLI&embeds_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Drun%2Bunit%2Btests%2Bpython%26rlz%3D1C1ONGR_enUS976US976%26sxsrf%3DAJOqlzUWca9VYEDJSSuw8Gkgw8CYLJma6w%3A16766630&feature=emb_logo


class TestGameBoard(unittest.TestCase):

    # Qnd function just to check if able to run test
    def test_able_to_run(self):
        self.assertEqual(10, 10)

    def test_first_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[0][0].x, (board_dim - 1))
        self.assertEqual(set.board[0][0].y, (board_dim - 1))
        self.assertEqual(set.board[0][0].internal_label, "a7")
        self.assertEqual(set.board[0][0].color, "white")

    def test_second_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[0][1].x, (board_dim - 2))
        self.assertEqual(set.board[0][1].y, (board_dim - 1))
        self.assertEqual(set.board[0][1].internal_label, "b7")
        self.assertEqual(set.board[0][0].color, "white")

    def test_2ndlast_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[board_dim - 1][board_dim - 2].x, 1)
        self.assertEqual(set.board[board_dim - 1][board_dim - 2].y, 0)
        self.assertEqual(set.board[board_dim - 1]
                         [board_dim - 2].internal_label, "g0")
        self.assertEqual(set.board[board_dim - 1]
                         [board_dim - 2].color, "white")

    def test_last_added_gameboard_position(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[board_dim - 1][board_dim - 1].x, 0)
        self.assertEqual(set.board[board_dim - 1][board_dim - 1].y, 0)
        self.assertEqual(set.board[board_dim - 1]
                         [board_dim - 1].internal_label, "h0")
        self.assertEqual(set.board[board_dim - 1]
                         [board_dim - 1].color, "white")

    def test_middle_postion_added(self):
        board_dim = 8
        set = GameBoard(board_dim)
        self.assertEqual(set.board[4][4].x, 3)
        self.assertEqual(set.board[4][4].y, 3)
        self.assertEqual(set.board[4][4].internal_label, "e3")
        self.assertEqual(set.board[4][4].color, "white")


if __name__ == '__main__':
    unittest.main()
