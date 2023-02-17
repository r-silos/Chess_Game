class GameBoard:
    def __init__(self, game_dimension):
        self.board = GameBoard.make_gameboard(game_dimension)

    # function takes in a dimension i and returns an ixi 2d array
    def make_gameboard(dimensions):
        mainboard = []
        # making double change
        for i in range(dimensions - 1, -1, -1):
            temp = []
            start_letter = 'a'
            for j in range(dimensions - 1, -1, -1):
                current_label = "{}{}".format(start_letter, i)
                print("the current x is {} and y is {}".format(j, i))
                temp.append(BoardSquare(j, i, current_label))
                start_letter = chr(ord(start_letter) + 1)
            mainboard.append(temp)
            print("New Row!")
        return mainboard

    # iterate through gameboard and print out internal labels
    def display_gameboard(self):
        pass
        # class representing each square on gameboard


class BoardSquare:
    def __init__(self, x_pos, y_pos, label, color="white"):
        self.x = x_pos
        self.y = y_pos
        self.color = color
        self.internal_label = label
        # external label will be what square displays at its position
        self.external_label = ""

    def get_x_position(self):
        return self.x

    def get_y_position(self):
        return self.y
