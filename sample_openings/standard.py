"""Standard Opening as a List"""
from piece import Piece, Orientation

cao = Piece(Orientation.CAOCAO, 0, 1)
pawn_1 = Piece(Orientation.PAWN, 4, 0)
pawn_2 = Piece(Orientation.PAWN, 4, 3)
pawn_3 = Piece(Orientation.PAWN, 3, 1)
pawn_4 = Piece(Orientation.PAWN, 3, 2)
enem = Piece(Orientation.ENEMY, 2, 1)
g_1 = Piece(Orientation.GENERAL, 0, 0)
g_2 = Piece(Orientation.GENERAL, 0, 3)
g_3 = Piece(Orientation.GENERAL, 2, 0)
g_4 = Piece(Orientation.GENERAL, 2, 3)


STANDARD_LIST = [
    cao,
    pawn_1,
    pawn_2,
    pawn_3,
    pawn_4,
    enem,
    g_1,
    g_2,
    g_3,
    g_4,
]

EMPTY_GRID = [
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
]

PAWN_GRID = [
    ['O', '_', '_', '_'],
    ['_', '_', '_', 'O'],
    ['_', '_', 'O', '_'],
    ['_', '_', '_', '_'],
    ['_', 'O', '_', '_'],
]


SAMPLE_GRID = [
    ['_', 'C', 'C', '_'],
    ['_', 'C', 'C', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
]

ENEMY_GRID = [
    ['_', '<', '>', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
]

STANDARD_GRID = [
    ['^', 'C', 'C', '^'],
    ['V', 'C', 'C', 'V'],
    ['^', '<', '>', '^'],
    ['V', 'O', 'O', 'V'],
    ['O', '_', '_', 'O'],
]

STANDARD_GRID_2 = [
    ['^', '<', '>', '^'],
    ['V', 'O', 'O', 'V'],
    ['_', 'C', 'C', '^'],
    ['^', 'C', 'C', 'V'],
    ['V', 'O', 'O', '_'],
]

STANDARD_GRID_3 = [
    ['C', 'C', '^', '^'],
    ['C', 'C', 'V', 'V'],
    ['<', '>', 'O', 'O'],
    ['^', 'O', '_', '^'],
    ['V', 'O', '_', 'V'],
]


ALMOST_DONE = [
    ['^', '<', '>', '^'],
    ['V', 'O', 'O', 'V'],
    ['^', 'C', 'C', '^'],
    ['V', 'C', 'C', 'V'],
    ['_', 'O', 'O', '_'],
]
