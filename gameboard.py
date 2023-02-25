from gamepiece import Gamepiece, Rook, Knight, Bishop, Queen, King, Pawn


class GameBoard:
    def __init__(self, game_dimension):
        self.board = GameBoard.make_gameboard(game_dimension)
        self.game_dimension = game_dimension

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

    def print_sample_board(self):
        for i in range(self.game_dimension):
            print(str(self.board[i][0].get_y_position()), end="  ")
            for j in range(self.game_dimension):
                print(str(self.board[i][j].get_external_label()), end=" ")
            print(" " + str(self.board[i][0].get_y_position()))
        current_letter = 'a'
        for iter in range(self.game_dimension):
            if iter == 0:
                print("   {}".format(current_letter), end=" ")
                current_letter = chr(ord(current_letter) + 1)
                continue
            print("{}".format(current_letter), end=" ")
            current_letter = chr(ord(current_letter) + 1)
        print("")


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

    def print_xy_coord(self):
        return ("{},{}".format(self.x, self.y))

    def set_piece_on_spot(self, piece):
        self.piece_on_spot = piece
        # set piece x/y values to x/y values of spot
        piece.set_y_value(self.get_y_position())
        piece.set_x_value(self.get_x_position())
        # print(piece.get_x_position())
        # print(piece.get_y_position())

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
