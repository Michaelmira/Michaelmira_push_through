

class Cell:
    def __init__(self, x_position, y_position, board, locked=False, cell_state=None):
        self.x_position = x_position
        self.y_position = y_position
        self.board = board
        self.locked = locked
        self.cell_state = cell_state

    def __repr__(self):
        return f'Cell(x_position={self.x_position}, y_position={self.y_position}, board={self.board}, locked={self.locked}, cell_state={self.cell_state})'

cell = Cell(x_position=1, y_position=2, board='main_board', locked=True, cell_state='X')

# Printing the cell representation
print(cell)