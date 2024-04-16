from typing import List
from cell import Cell, CellState
from pprint import pprint

class GameBoard:
    def __init__(self, height: int, width: int, num_boards: int):
        """
            Creates a list of game boards of specified height and width
         Args:
            height (int): The number of cells high the game is (the number of rows).
            width (int): The number of cells wide the game is (the number of columns).
            num_boards (int): Number of game boards to create.
        """
        self.height = height
        self.width = width
        self.num_boards = num_boards
        self.boards = [Board(height, width, face) for face in range(num_boards)]

    def print_ascii_game_boards(self):
        for board_idx, board in enumerate(self.boards):
            print(f"Game Board {board_idx + 1}:")
            board.print_ascii_game_board()


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
    
    def _kth_letter(self, k):
        # Ensure k is within the range of 1 to 26
        if 0 <= k <= 25:
            # Calculate the ASCII code for the K'th letter and convert it to a character
            return chr(65 + k)
        else:
            return "Input must be between 0 and 25"
    
    def print_ascii_game_board(self):
        
        row_letters = [self._kth_letter(row_idx) for row_idx in range(self.height)]
        row_letters = row_letters[::-1]
        print("\n")
        for row_idx in range(self.height):
            row_ascii = f"{row_letters[row_idx]}  | "
            for col_idx in range(self.width):
                cell_state = self.cells[col_idx][row_idx].cell_state
                for data in CellState:
                    if cell_state == data:
                        row_ascii += str(cell_state.value) + " | "
            print(row_ascii)
        print("     " + "   ".join([str(idx) for idx in range(self.width)]) + "  ")
                