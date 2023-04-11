from gamepiece import Gamepiece, Pawn, King, Knight, Bishop, Rook, Queen
from gameboard import GameBoard, BoardSquare, ChessBoard

# should find a way to incorprate serialization!!


class Chess_Game:
    def __init__(self, white_piece_player, black_piece_player):
        # keep track of game turn b/c certain rules apply on which turn it is
        self.game_turn = 0
        # white player name
        self.white_player = white_piece_player
        # black player name
        self.black_player = black_piece_player
        # gameboard with chess dimensions
        self.chess_board = ChessBoard()

    def get_chess_board(self):
        return self.chess_board

    def get_white_player(self):
        return self.white_player

    def get_black_player(self):
        return self.black_player

    # function just test if able to move pieces. NOTE to self: will have to validate that starting postion actually has a chess piece!
    def user_input_move_pieces(self):
        # .lower is method to dataclean as all algebraic postions are lowercase
        original_piece = input(
            "Type algebraic position of piece you want to move: ").lower()
        while original_piece not in self.chess_board.get_algebraic_dictionary().keys():
            original_piece = input(
                "That position does not exist! Please type in algebraic position of piece you want to move: ").lower()
        final_position = input(
            "Please type in algebraic position of where you want to move chosen piece: ").lower()
        while final_position not in self.chess_board.get_algebraic_dictionary().keys():
            final_position = input(
                "That position does not exist! Please type in algebraic position of where you want to move chosen piece: ").lower()

    # move_checker will be all-encompassing as will hold variables to check for en passant, pawn double move, etc ...
    # goal of move checker is to validate if specific move is viable,
    def move_checker(self, start_postion, end_position, pawn_double_move_bool=False, en_passant_bool=False, castling_bool=False):
        pass
