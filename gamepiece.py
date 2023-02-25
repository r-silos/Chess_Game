class Gamepiece:
    def __init__(self):
        self.display = "T"

    def get_x_position(self):
        return self.x_value

    def get_y_position(self):
        return self.y_value

    def set_y_value(self, y_pos):
        self.y_value = y_pos

    def set_x_value(self, x_pos):
        self.x_value = x_pos


class Pawn(Gamepiece):
    def __init__(self, color):
        self.display = "P"
        self.piece_color = color


class King(Gamepiece):
    def __init__(self, color):
        self.display = "K"
        self.piece_color = color


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


class Knight(Gamepiece):
    def __init__(self, color):
        self.display = "K"
        self.piece_color = color
