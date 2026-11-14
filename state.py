"""State of the Board ;)"""
import copy
from typing import Optional

from piece import Orientation, Piece
from board import Board
from sample_openings.standard import SAMPLE_GRID, PAWN_GRID, STANDARD_GRID

DIRECTIONS = ["left", "right", "up", "down"]


class State:
    """
    A state records the current state of the board and create successors
    """
    def __init__(self, board: Board, parent: Optional["State"]):
        self.board = board
        self.parent = parent

        self.depth = 0
        self.steps_to = 0
        self.heuristic_to = 0
        self.cost_to = 0

    def get_state_key(self):
        return tuple(tuple(row) for row in self.board.board)

    def create_successors(self) -> list["State"]:
        successors = []
        for i, p in enumerate(self.board.pieces):
            direction_allowed_list = self.get_legal_directions(p)
            # print(direction_allowed_list)
            for direct_index, direct_allowed in enumerate(direction_allowed_list):
                if direct_allowed:
                    new_board = copy.deepcopy(self.board)
                    # print(p.orient, "can move ", DIRECTIONS[direct_index])
                    new_piece = new_board.pieces[i]
                    row, col = new_piece.piece_map[DIRECTIONS[direct_index]]

                    # print("Direction:", DIRECTIONS[direct_index])
                    # print("Current:", (new_piece.row, new_piece.col))
                    # print("Destination:", (row, col))
                    # print("Difference:", (row - new_piece.row, col - new_piece.col))
                    assert abs(row - new_piece.row) + abs(col - new_piece.col) == 1
                    new_piece.row, new_piece.col = row, col
                    new_piece.piece_map = new_piece.create_piece_map()
                    # print("OG     ", new_piece.occupied)

                    # REFRESH ALL
                    new_piece.occupied = new_piece.get_occupied_cells()
                    new_piece.need_blanks = new_piece.find_blanks()
                    new_board.board = new_board.render_board()

                    # new_board.print_board()
                    # print("updated", new_piece.occupied)

                    # new_board.print_board()
                    successors.append(State(new_board, self))

        return successors

    def is_blank_spot(self, coor):
        row = coor[0]
        col = coor[1]
        if 0 <= row <= 4 and 0 <= col <= 3:
            return self.board.board[row][col] == Orientation.BLANK.value
        return False

    def get_legal_directions(self, piece: Piece):
        dirs = []
        final = []
        for direction in piece.need_blanks:
            for spots in direction:
                dirs.append(self.is_blank_spot(spots))
            final.append(all(dirs))
            dirs = []

        return final

    def is_goal(self):
        for p in self.board.pieces:
            if p.orient == Orientation.CAOCAO:
                return p.row == 3 and p.col == 1

        return False

    def goal_to_parent(self) -> list["State"]:
        path = []
        curr = self
        while curr.parent is not None:
            # print("has a mommy")
            path.append(curr)
            curr = curr.parent
        path.append(curr)
        print("length of path", len(path))
        path.reverse()
        return path

    def cost_value(self, steps_away: int):
        cao = next(p for p in self.board.pieces if p.orient == Orientation.CAOCAO)

        distance = abs(3 - cao.row)

        blocking = 0
        for col in range(cao.col, cao.col + 2):
            if self.board.board[4][col] != "_":
                blocking += 1

        assert distance + blocking > 0
        return distance + blocking


if __name__ == "__main__":
    bored = Board(SAMPLE_GRID)
    state = State(bored, None)
    sux = state.create_successors()
    print("total moves", len(sux))
    # for s in sux:
    #     print(s.parent)
    #     s.board.print_board()
    #     s.parent.board.print_board()
