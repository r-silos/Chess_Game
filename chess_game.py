# from gamepiece import Gamepiece, Pawn, King, Knight, Bishop, Rook, Queen
# from gameboard import GameBoard, BoardSquare


class Chess_Game:
    def __init__(self, white_piece_player, black_piece_player, chess_board):
        self.game_turn = 0
        self.white_player = white_piece_player
        self.black_player = black_piece_player
        self.chess_board = chess_board
