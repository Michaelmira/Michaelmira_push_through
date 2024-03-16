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
    
    def initialize_cells(self):
        my_cells = []
        for height_idx in range(self.height):
            for width_idx in range(self.width):
                cur_cell = Cell(width_idx, height_idx, self.face)
                my_cells.append(cur_cell)
        return my_cells
        