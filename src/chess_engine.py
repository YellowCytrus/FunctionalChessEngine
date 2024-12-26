from principles_parser import PParser, parse_principles
from field_setup_parser import parse_setup
from game_logic import Logic


class Engine:

    def __init__(self):
        self.path_to_principles = "../configs/principles.json"
        self.path_to_setup = "../configs/field_setups/default_start.json"
        self.SETUP = None
        self.logic = None
        self.set_SETUP()
        self.set_logic()

    def set_logic(self):
        self.logic = Logic(
            move_principies=parse_principles(self.path_to_principles)
        )

        pieces = self.SETUP["pieces"]

        if self.SETUP["symetry"]:
            symetry_pieces = {}

            for piece in pieces:
                new_colored_piece = piece[0] + "b"  # todo set_another_color()
                symetry_pieces[new_colored_piece] = []
                for pos in pieces[piece]:
                    X = pos[0]
                    Y = 7 - pos[1]
                    symetry_pieces[new_colored_piece].append([X, Y])
            pieces.update(symetry_pieces)

        self.logic.set_field_status(
            pieces=pieces
        )
        piece = self.logic.get_piece_from_board([0, 0])
        self.logic.get_principial_points(piece, [0, 0])

    def render(self):   # временный метод
        for line in self.logic._board:
            print(line)

    def set_SETUP(self):
        self.SETUP = parse_setup(self.path_to_setup)


e = Engine()
e.render()
