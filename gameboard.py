class GameBoard:
    def __init__(self):
        pass

    # function that allows to make gameboard to spec
    def make_gameboard(self, dimensions):
        mainboard = []
        for i in range(dimensions, 0, -1):
            temp = []
            start_letter = 'a'
            for i in range(dimensions):
                temp.append("{}{}".format(start_letter, i + 1))
                start_letter = chr(ord(start_letter) + 1)
            mainboard.append(temp)
        return mainboard
