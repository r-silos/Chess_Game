class GameBoard:
    def __init__(self, game_dimension):
        self.board = GameBoard.make_gameboard(game_dimension)

    # function takes in a dimension i and returns an ixi 2d array
    def make_gameboard(self, dimensions):
        mainboard = []
        for i in range(dimensions, 0, -1):
            temp = []
            start_letter = 'a'
            for j in range(dimensions, 0, -1):
                current_label = "{}{}".format(start_letter, i)
                temp.append(GameBoard(j, i, current_label))
                start_letter = chr(ord(start_letter) + 1)
            mainboard.append(temp)
        return mainboard

# class representing each square on gameboard


class BoardSquare:
    def __init__(self, x_pos, y_pos, label, color="white"):
        self.x = x_pos
        self.y = y_pos
        self.color = color
        self.label = label
        self.color = color

    def get_x_position(self):
        return self.x

    def get_y_position(self):
        return self.y
