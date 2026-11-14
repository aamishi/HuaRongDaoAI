"""Board of the Game <3"""
import copy

from sample_openings.standard import STANDARD_GRID, EMPTY_GRID
from piece import Piece, Orientation


class Board:
    """
    In this, the Piece/s are rendered from the raw input
    """
    def __init__(self, raw_input: list[list[int]]):
        self.length = 5
        self.width = 4
        self.pieces = self.render_pieces(raw_input)
        self.board = self.render_board()

    def render_pieces(self, raw_input: list[list[int]]) -> list[Piece]:
        """Given a raw input, convert into pieces on board"""
        pieces = []
        open_cao = 1
        for row in range(self.length):
            for col in range(self.width):
                sym = raw_input[row][col]
                if sym == Orientation.PAWN.value:
                    pieces.append(Piece(Orientation.PAWN, row, col))
                elif sym == Orientation.CAOCAO.value:
                    open_cao -= 1
                    if open_cao > -1:
                        pieces.append(Piece(Orientation.CAOCAO, row, col))
                elif sym == Orientation.CAOCAO.GENERAL.value:
                    pieces.append(Piece(Orientation.GENERAL, row, col))
                elif sym == Orientation.CAOCAO.ENEMY.value:
                    pieces.append(Piece(Orientation.ENEMY, row, col))
                else:
                    pass
        return pieces

    def render_board(self):
        render_grid = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
        ]
        for p in self.pieces:
            for c in p.occupied:
                render_grid[c[0]][c[1]] = p.orient.value
        return render_grid

    def print_board(self):
        for row in self.board:
            print('  '.join(row))
        print("--------------------")


if __name__ == "__main__":
    board = Board(STANDARD_GRID)
