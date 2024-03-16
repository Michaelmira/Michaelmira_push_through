from cell import Cell
from board import Board

class Cube:
    def __init__(self, height: int, width: int):
        """Creates a cube consisting of four boards.

        Args:
            height (int): The number of cells high the game is(the number of rows).
            width (int): the number of cells wide the game is (the number of columns).
        """
        self.boards = [Board(height, width, face) for face in range(4)]
    
    def __repr__(self):
        """Return a string representation of the cube"""
        cube_repr = ""
        for idx, board in enumerate(self.boards):
            cube_repr += f"Face{idx}:\n{board}\n\n"
        return cube_repr
        # return '\n\n'.join([f'Face {idx}:\n{board}' for idx, board in enumerate(self.boards)])