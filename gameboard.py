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
                print("{} ".format(element.internal_label), end="")
            print("")

    def display_gameboard_xy_values(self):
        for row in self.board:
            for element in row:
                print("({},{}) ".format(element.x, element.y), end="")
            print("")


class BoardSquare:
    def __init__(self, x_pos, y_pos, label, color="white"):
        self.x = x_pos
        self.y = y_pos
        self.color = color
        self.internal_label = label
        # external label will be what square displays at its position (ie chess piece)
        self.external_label = ""

    def get_x_position(self):
        return self.x

    def get_y_position(self):
        return self.y
