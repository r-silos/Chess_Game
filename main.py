from gameboard import GameBoard


def gameboard_creator(dims):
    burd = GameBoard(dims)
    burd.set_start_chess_board()
    return burd


def main():
    current_gameboard = gameboard_creator(8)
    current_gameboard.print_sample_board()
    print("\033[31mHello, world!\033[0m")


main()
