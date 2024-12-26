from typing import Dict, Any
from principles_parser import parse_principles, PParser


class Logic:

    def __init__(self, move_principies, board_width=8, board_height=8):
        self._board_width = board_width
        self._board_height = board_height
        self.empty_cell = "  "
        self._board = [[self.empty_cell] * board_width for lines in range(board_height)]
        self.MOVE_PRINCIPLES = move_principies
        self.parser = PParser()

    def set_field_status(self, pieces: Dict):
        for piece in pieces:
            for position in pieces[piece]:
                X = position[0]
                Y = position[1]
                if self.possible_coo([X, Y]):
                    self._board[Y][X] = piece  # add color to piece
                else:
                    raise ValueError("Attemt to set piece out of field bounds")

    def possible_coo(self, coordinates) -> bool:
        if coordinates is None:
            # throw exception
            return False

        if not 0 <= (X := coordinates[0]) <= 7:
            # throw exception
            return False

        if not 0 <= (Y := coordinates[1]) <= 7:
            # throw exception
            return False

        if not type(X) is int:
            # throw exception
            return False

        if not type(Y) is int:
            # throw exception
            return False

        return True

    def move(self, coordinates_from, coordinates_to):
        if not (self.possible_coo(coordinates_from) and self.possible_coo(coordinates_to)):
            # throw exception
            return

        possible_ways = self.get_possible_ways(self.MOVE_PRINCIPLES["p"], coordinates_from)

        if len(possible_ways) == 0:
            # throw exception
            return

        if coordinates_to in possible_ways:
            self.move(coordinates_from, coordinates_to)

    def get_possible_points(self):
        pass

    def get_board_status(self):
        pass

    def is_shah_mat_pat(self):
        pass

    def get_principial_points(self, piece, coordinates) -> []:
        principial_points = []

        if piece is None:
            return # обработать случай с пустой клеткой

        X = coordinates[0]
        Y = coordinates[1]
        for func in self.MOVE_PRINCIPLES[piece[0]]["func"]:
            parsed_func = self.parser.try_parse_string(func)

            operation_with_X = parsed_func[1]
            operation_with_Y = parsed_func[4]
            if operation_with_X == "":
                operation_with_X = "n"
            if operation_with_Y == "":
                operation_with_Y = "n"

            operand_with_X = parsed_func[2]
            operand_with_Y = parsed_func[5]
            if operand_with_X is None:
                operand_with_X = "0"
            if operand_with_Y is None:
                operand_with_Y = "0"

            for sign_X in operation_with_X:
                for sign_Y in operation_with_Y:

                    if not operand_with_X.isdigit():
                        increment_X = [x for x in range(1, 9)]
                    else:
                        increment_X = [int(operand_with_X)]

                    if not operand_with_Y.isdigit():
                        increment_Y = [y for y in range(1, 9)]
                    else:
                        increment_Y = [int(operand_with_Y)]

                    for x in increment_X:
                        for y in increment_Y:
                            possible_XY = [X, Y]

                            if len(increment_Y) != 1 and len(increment_X) != 1:
                                if x != y:
                                    continue

                            if sign_X == "+":
                                possible_XY[0] += x
                            if sign_Y == "+":
                                possible_XY[1] += y
                            if sign_X == "-":
                                possible_XY[0] -= x
                            if sign_Y == "-":
                                possible_XY[1] -= y

                            if self.possible_coo([possible_XY[0], possible_XY[1]]):
                                principial_points.append(possible_XY)
                                self._board[possible_XY[1]][possible_XY[0]] = "[]"
        print(principial_points)
        return principial_points

    def get_piece_from_board(self, coordinates):
        if not self.possible_coo(coordinates):
            return

        if self._board[Y := coordinates[1]][X := coordinates[0]][0] == self.empty_cell:
            return

        for key in self.MOVE_PRINCIPLES.keys():
            if self._board[Y][X][0] == key:
                return self._board[Y][X]
        else:
            return None

    def move(self, coordinates_from, coordinates_to):

        pass
