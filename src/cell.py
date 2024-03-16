class Cell:
    def __init__(self,
            x: int,
            y: int,
            board: int,
            locked: bool=False,
            cell_state: int=0):
        """Cells are the individual blocks that make up a board on the game face.
        Args:
            x (int): The row coordinate from 0 to the length of the board
            y (int): The column coordinate from 0 to the height of the board
            board (int): An integer reference to which board the cell belongs to in the game
            locked (bool, optional): If true, means the cell cannot be modified in the game. Defaults to False.
            cell_state (int, optional): One of a possible number of states of the cell that specifies which player controls it, if any. Defaults to None.
        """
        self.x = x
        self.y = y
        self.board = board
        self.locked = locked
        self.cell_state = cell_state

    def __repr__(self):
        return f'Cell (X={self.x}, Y={self.y}, board={self.board}, locked={self.locked}, cell_state={self.cell_state})'
