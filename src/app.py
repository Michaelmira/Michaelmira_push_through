from defines import *
from cube import Cube
from game import Game

cube = Cube(GAME_HEIGHT, GAME_WIDTH, num_boards=NUM_BOARDS)

#Grab a cell and make sure it looks good
first_board = cube.boards[0]
some_cell = first_board.get_cell(2, 3)
print(some_cell)

new_game_config = {}
new_game = Game(new_game_config)

new_game.play_game()

