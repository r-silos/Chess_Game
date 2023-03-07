from gameboard import GameBoard, BoardSquare
from gamepiece import Gamepiece, Rook


# will set the chess pieces outside the Gameboard class so gameboard can be used for diffrent types of games
def gameboard_creator(dims):
    burd = GameBoard(dims)
    burd.set_start_chess_board()
    return burd


def main():
    current_gameboard = gameboard_creator(8)
    current_gameboard.print_sample_board()
    pos_list = current_gameboard.set_up_chess_dictionary()
    print(pos_list.keys())
    print(pos_list["a7"].get_piece_on_spot().get_label())


main()
