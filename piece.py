"""HRD Piece Class"""
from enum import Enum


class Orientation(Enum):
    """Orienatation of the pieces"""
    CAOCAO = "C"
    PAWN = "O"
    GENERAL = "^"
    ENEMY = "<"
    BLANK = "_"


class Piece:
    """PIECE"""

    directions_map = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
    ]

    def __init__(self, orient: Orientation, row, col, ):
        """Init the declaration"""
        self.col = col
        self.row = row
        self.orient = orient
        # above this is fine

        self.occupied = self.get_occupied_cells()
        self.need_blanks = self.find_blanks()
        self.make_moves = self.move_coordinates()
        # self.piece_map = {
        #                 "left": (self.row, self.col - 1),
        #                 "right": (self.row, self.col + 1),
        #                 "up": (self.row - 1, self.col),
        #                 "down": (self.row + 1, self.col),
        # }
        self.piece_map = self.create_piece_map()
        assert len(self.occupied) > 0

    def create_piece_map(self):
        return {
            "left": (self.row, self.col - 1),
            "right": (self.row, self.col + 1),
            "up": (self.row - 1, self.col),
            "down": (self.row + 1, self.col),
        }

    def move_coordinates(self) -> list[tuple[int, int]]:
        """
        Valid moves for the Piece as per the boundary only
        """
        successors = []

        for d in self.directions_map:
            n_row = self.row + d[0]
            n_col = self.col + d[1]

            # PAWN
            if self.orient == Orientation.PAWN:
                if 0 <= n_row <= 4 and 0 <= n_col <= 3:
                    successors.append((n_row, n_col))
                else:
                    successors.append((self.row, self.col))
            # ENEMY
            elif self.orient == Orientation.ENEMY:
                if 0 <= n_row <= 4 and 0 <= n_col <= 2:
                    successors.append((n_row, n_col))
                else:
                    successors.append((self.row, self.col))
            # GENERAL
            elif self.orient == Orientation.GENERAL:
                if 0 <= n_row <= 3 and 0 <= n_col <= 3:
                    successors.append((n_row, n_col))
                else:
                    successors.append((self.row, self.col))
            # CAOCAO
            elif self.orient == Orientation.CAOCAO:
                if 0 <= n_row <= 3 and 0 <= n_col <= 2:
                    successors.append((n_row, n_col))
                else:
                    successors.append((self.row, self.col))
            # elif self.orient == Orientation.BLANK:
            #     if 0 <= n_row <= 4 and 0 <= n_col <= 3:
            #         successors.append((n_row, n_col))
            else:
                pass

        return successors

    def find_blanks(self):
        needed_cardinal_blanks = []
        if self.orient == Orientation.PAWN:
            needed_cardinal_blanks = [
                [(self.row, self.col - 1)],
                [(self.row, self.col + 1)],
                [(self.row - 1, self.col)],
                [(self.row + 1, self.col)]
            ]
        elif self.orient == Orientation.ENEMY:
            needed_cardinal_blanks = [
                [(self.row, self.col - 1)],
                [(self.row, self.col + 2)],
                [(self.row - 1, self.col), (self.row - 1, self.col + 1)],
                [(self.row + 1, self.col), (self.row + 1, self.col + 1)]
            ]
        elif self.orient == Orientation.GENERAL:
            needed_cardinal_blanks = [
                [(self.row, self.col - 1), (self.row + 1, self.col - 1)],
                [(self.row, self.col + 1), (self.row + 1, self.col + 1)],
                [(self.row - 1, self.col)],
                [(self.row + 2, self.col)]
            ]
        elif self.orient == Orientation.CAOCAO:
            needed_cardinal_blanks = [
                [(self.row, self.col - 1), (self.row + 1, self.col - 1)],
                [(self.row, self.col + 2), (self.row + 1, self.col + 2)],
                [(self.row - 1, self.col), (self.row - 1, self.col + 1)],
                [(self.row + 2, self.col), (self.row + 2, self.col + 1)]
            ]
        else:
            assert Exception("no other orientation should be allowed")
        return needed_cardinal_blanks

    def get_occupied_cells(self) -> list:
        """
        Get occupied cells of the piece based on top left corner
        This should be called everytime the top left is reassigned !!!!!!

        WHAT DOES blank_list DO ?????
        WHAT DOES top_left_candidates DO ?????

        top_left_candidates is the same for all !!!!
        """
        top_left_candidates = [
            (self.row, self.col - 1), (self.row, self.col + 1),
            (self.row - 1, self.col), (self.row + 1, self.col)
        ]

        if self.orient == Orientation.PAWN:
            top_left_candidates = [
                (self.row, self.col - 1), (self.row, self.col + 1),
                (self.row - 1, self.col), (self.row + 1, self.col)
            ]
            return [(self.row, self.col)]

        elif self.orient == Orientation.ENEMY:
            return [
                (self.row, self.col),
                (self.row, self.col + 1)
            ]

        elif self.orient == Orientation.GENERAL:
            return [
                (self.row, self.col),
                (self.row + 1, self.col)
            ]

        elif self.orient == Orientation.CAOCAO:
            return [
                (self.row, self.col),
                (self.row, self.col + 1),
                (self.row + 1, self.col),
                (self.row + 1, self.col + 1)
            ]
        else:
            pass
        return blank_list


if __name__ == "__main__":
    from sample_openings.standard import STANDARD_LIST

    for p in STANDARD_LIST:
        print(p.orient, len(p.occupied), p.occupied)
