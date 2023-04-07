from gamepiece import Gamepiece, Rook, Knight, Bishop, Queen, King, Pawn
from colorama import Fore, Style, Back


class GameBoard:
    def __init__(self, game_dimension):
        self.board = GameBoard.make_gameboard(game_dimension)
        self.game_dimension = game_dimension
        self.algebra_dict = self.set_up_chess_dictionary()

    # function takes in a dimension i and returns an ixi 2d array
    def make_gameboard(dimensions):
        mainboard = []
        # making double change
        for i in range(dimensions - 1, -1, -1):
            temp = []
            start_letter = 'a'
            for j in range(0, dimensions):
                current_label = "{}{}".format(start_letter, i)
                # print("the current x is {} and y is {}".format(j, i))
                temp.append(BoardSquare(j, i, current_label))
                start_letter = chr(ord(start_letter) + 1)
            mainboard.append(temp)
            # print("New Row!")
        return mainboard

    # iterate through gameboard and print out internal labels
    def display_gameboard_internal_labels(self):
        # this solo print because not alignted in test case termianl
        print("")
        for row in self.board:
            for element in row:
                print("{} ".format(element.get_internal_label()), end="")
            print("")

    def display_gameboard_xy_values(self):
        for row in self.board:
            for element in row:
                print("({},{}) ".format(element.get_x_position(),
                      element.get_y_position()), end="")
            print("")

    def print_board(self):
        # loop to iterate through each row of gameboard and print height in algebraic notation
        for i in range(self.game_dimension):
            print(str(self.board[i][0].get_y_position()), end="  ")
            for j in range(self.game_dimension):
                if self.board[i][j].get_piece_on_spot() == None:
                    print(self.board[i][j].get_external_label(), end=" ")
                else:
                    if self.board[i][j].get_piece_on_spot().get_piece_color() == "Black":
                        print(
                            Fore.BLACK + Back.GREEN + self.board[i][j].get_piece_on_spot().get_label(), end=" ")
                        print(Style.RESET_ALL, end="")
                    else:
                        print(
                            Fore.WHITE + Back.WHITE + self.board[i][j].get_piece_on_spot().get_label(), end=" ")
                        print(Style.RESET_ALL, end="")
            print(" " + str(self.board[i][0].get_y_position()))
        # loop to print letters at bottom of screen
        current_letter = 'a'
        for iter in range(self.game_dimension):
            if iter == 0:
                print("   {}".format(current_letter), end=" ")
                current_letter = chr(ord(current_letter) + 1)
                continue
            print("{}".format(current_letter), end=" ")
            current_letter = chr(ord(current_letter) + 1)
        print("")

    # function to set correct pieces in top/bottom 2 rows so can start game

    def set_start_chess_board(self):
        # set top row
        self.board[0][0].set_piece_on_spot(Rook("Black"))
        self.board[0][1].set_piece_on_spot(Knight("Black"))
        self.board[0][2].set_piece_on_spot(Bishop("Black"))
        self.board[0][3].set_piece_on_spot(Queen("Black"))
        self.board[0][4].set_piece_on_spot(King("Black"))
        self.board[0][5].set_piece_on_spot(Bishop("Black"))
        self.board[0][6].set_piece_on_spot(Knight("Black"))
        self.board[0][7].set_piece_on_spot(Rook("Black"))

        # set bottom row
        self.board[7][0].set_piece_on_spot(Rook("White"))
        self.board[7][1].set_piece_on_spot(Knight("White"))
        self.board[7][2].set_piece_on_spot(Bishop("White"))
        self.board[7][3].set_piece_on_spot(Queen("White"))
        self.board[7][4].set_piece_on_spot(King("White"))
        self.board[7][5].set_piece_on_spot(Bishop("White"))
        self.board[7][6].set_piece_on_spot(Knight("White"))
        self.board[7][7].set_piece_on_spot(Rook("White"))

        # set black pawns
        self.board[1][0].set_piece_on_spot(Pawn("Black"))
        self.board[1][1].set_piece_on_spot(Pawn("Black"))
        self.board[1][2].set_piece_on_spot(Pawn("Black"))
        self.board[1][3].set_piece_on_spot(Pawn("Black"))
        self.board[1][4].set_piece_on_spot(Pawn("Black"))
        self.board[1][5].set_piece_on_spot(Pawn("Black"))
        self.board[1][6].set_piece_on_spot(Pawn("Black"))
        self.board[1][7].set_piece_on_spot(Pawn("Black"))

        # set white pawns
        self.board[6][0].set_piece_on_spot(Pawn("White"))
        self.board[6][1].set_piece_on_spot(Pawn("White"))
        self.board[6][2].set_piece_on_spot(Pawn("White"))
        self.board[6][3].set_piece_on_spot(Pawn("White"))
        self.board[6][4].set_piece_on_spot(Pawn("White"))
        self.board[6][5].set_piece_on_spot(Pawn("White"))
        self.board[6][6].set_piece_on_spot(Pawn("White"))
        self.board[6][7].set_piece_on_spot(Pawn("White"))

    # will allow to to create a dictionary of the positons refrenced by algebraic chess position (makes moving pieces considerably easier)
    def set_up_chess_dictionary(self):
        algebraic_pos_dict = {}
        for i in range(self.game_dimension):
            for j in range(self.game_dimension):
                algebraic_pos_dict[self.board[i]
                                   [j].get_internal_label()] = self.board[i][j]
        return algebraic_pos_dict

    def get_algebraic_dictionary(self):
        return self.algebra_dict

    def get_spot_from_algebraic_dictionary(self, al_position):
        return self.algebra_dict[al_position]

    def get_piece_from_algebraic_dictionary(self, al_position):
        return self.algebra_dict[al_position].get_piece_on_spot()

    def check_piece_color_from_dictionary(self, al_position, color):
        return self.algebra_dict[al_position].get_piece_on_spot().color_checker(color)

    def move_piece(self, original_position, final_position):
        # this line will change the piece on final spot to have the piece on starting spot
        self.get_spot_from_algebraic_dictionary(final_position).set_piece_on_spot(
            self.get_piece_from_algebraic_dictionary(original_position))
        # this line will get spot on original position and set it so piece on that spot is none (set_piece_on_spot called w/o args will set piece on spot as being none)
        self.get_spot_from_algebraic_dictionary(
            original_position).set_piece_on_spot()


class ChessBoard(GameBoard):
    def __init__(self):
        # ChessBoard class will just initialize the Gameboard class in 8x8 dims
        super().__init__(8)
        self.set_start_chess_board()


class BoardSquare:
    def __init__(self, x_pos, y_pos, label, color="white"):
        self.x = x_pos
        self.y = y_pos
        # this is the color of the square on board (black/white)
        self.board_color = color
        self.internal_label = label
        # external label will be what square displays at its position (ie chess piece)
        self.external_label = "x"
        # this is where we hold chess piece object
        self.piece_on_spot = None
        self.xy_coord = (x_pos, y_pos)

    def get_x_position(self):
        return self.x

    def get_y_position(self):
        return self.y

    def get_internal_label(self):
        return self.internal_label

    def get_color(self):
        return self.board_color

    def get_external_label(self):
        return self.external_label

    def get_piece_on_spot(self):
        return self.piece_on_spot

    def get_xy_coord(self):
        return self.xy_coord

    def print_xy_coord(self):
        return ("{},{}".format(self.x, self.y))

    def set_piece_on_spot(self, piece=None):
        if piece == None:
            self.piece_on_spot = None
        else:
            self.piece_on_spot = piece
            piece.set_y_value(self.get_y_position())
            piece.set_x_value(self.get_x_position())
