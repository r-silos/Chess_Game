from gameboard import GameBoard, BoardSquare
from gamepiece import Gamepiece, Rook
from chess_game import Chess_Game


# will set the chess pieces outside the Gameboard class so gameboard can be used for diffrent types of games


def main():
    game = Chess_Game("Jack", "John")
    game.user_input_move_pieces()


main()
