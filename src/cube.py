from cell import Cell
from board import Board

class Cube:
    def __init__(self, height: int, width: int, num_boards: int=4):
        """Creates a cube consisting of four boards.

        Args:
            height (int): The number of cells high the game is(the number of rows).
            width (int): the number of cells wide the game is (the number of columns).
            num_boards (int, optional): The number of boards to create on the cube. Defaults to 4.
        """
        self.height = height
        self.width = width
        self.num_boards = num_boards
        self.boards = [Board(height, width, face) for face in range(self.num_boards)]
    
    def __repr__(self):
        """Return a string representation of the cube"""
        cube_repr = ""
        for idx, board in enumerate(self.boards):
            cube_repr += f"Face{idx}:\n"
            for row in range(board.height):
                for col in range (board.width):
                    cell = board.cells[row * board.width + col]
                    cube_repr += f"{cell}\t"
                cube_repr += "\n"
            cube_repr += "\n"
        return cube_repr