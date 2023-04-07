class Gamepiece:
    def __init__(self):
        self.display = "T"
        self.piece_color = "default color"

    def get_x_position(self):
        return self.x_value

    def get_y_position(self):
        return self.y_value

    def set_y_value(self, y_pos):
        self.y_value = y_pos

    def set_x_value(self, x_pos):
        self.x_value = x_pos

    def get_label(self):
        return self.display

    def get_piece_color(self):
        return self.piece_color

    def color_checker(self, comp_color):
        return True if comp_color == self.piece_color else False

    # write function that validates move from start to end,
    # and allows for each piece to input args to validate their respective motions


class Pawn(Gamepiece):
    def __init__(self, color):
        self.display = "P"
        self.piece_color = color


class King(Gamepiece):
    def __init__(self, color):
        self.display = "K"
        self.piece_color = color
        # this attribute used for castling
        self.has_moved = False
        # attribute to see if king under attack from opponeant piece as they determines what moves player has
        self.is_under_attack = False


class Bishop(Gamepiece):
    def __init__(self, color):
        self.display = "B"
        self.piece_color = color


class Queen(Gamepiece):
    def __init__(self, color):
        self.display = "Q"
        self.piece_color = color


class Rook(Gamepiece):
    def __init__(self, color):
        self.display = "R"
        self.piece_color = color
        # this attribute used for castling
        self.has_moved = False


class Knight(Gamepiece):
    def __init__(self, color):
        self.display = "H"
        self.piece_color = color
