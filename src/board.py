from typing import List
from cell import Cell

class Board():
    def __init__(self, height: int, width: int, face: int):
        """Creates a game board of specified height and width
        with a reference to the face of the game cube it represents

        Args:
            height (int): The number of cells high the game is (the number of rows).
            width (int): The number of cells wide the game is (the number of columns).
            face (int): Identifier of the face of the cube/shape the game board is on. 
              for instance, a cube has six faces, so this is an integer 0-5 on a cube
        """
        self.height = height
        self.width = width
        self.face = face
        self.cells = self.initialize_cells()
    
    def initialize_cells(self) -> List[List[Cell]]:
        """Creates a 2d list of cells given the game width and height.

        Returns:
            List[List[Cell]]: A list of lists of shape (self.width, self.height)
        """
        my_cells = []
        for col_idx in range(self.width):
            cur_col = []
            for row_idx in range(self.height):
                cur_cell = Cell(col_idx, row_idx, self.face)
                cur_col.append(cur_cell)
            my_cells.append(cur_col)
        return my_cells
        
    def get_cell(self, x: int, y: int) -> Cell:
        """Given an x index (column) and y index (row), return the cell
        on the board from this (x,y) coordinate

        Args:
            x (int): The column number, starting from 0
            y (int): The row number, starting from 0

        Returns:
            Cell: The Cell at the (x,y) position on the board
            
        Raises:
            ValueError: The cell does not exist
        """
        if x > self.width:
            raise ValueError(f"Cannot get cell with X index {x} when board has a width of {self.width}")
        if y > self.height:
            raise ValueError(f"Cannot get cell with y index {y} when board has a height of {self.height}")
    
        return self.cells[x][y]
    