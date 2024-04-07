from config import Config
from defines import *

class Player:

    #TODO - color should be an identifier
    def __init__(self, name: str, color: str, account_id: str, config: Config):
        """Initializes the player class

        Args:
            name (str): The name of the player to appear on screen
            color (str): The color of the player to appear
            account_id (str): A unique account identifier for the player
        """
        self.name = name
        self.color = color
        self.account_id = account_id
        self.score = 0
        self.pushes_left = config.get_parameter_value("total_pushes")
        self.lives_left = config.get_parameter_value("num_lives")
        self.turns_left = config.get_parameter_value("turns_per_move")

    def player_place_piece(self):
        if self.turns_left > 0:
            self.player_use_turn()
            print(f"{self.name} Placed a Piece!")
        else:
            return print("it is not your turn")

    def lose_life(self):
        self.lives_left -= 1

    def add_pushes(self, amount: int=1):
        self.pushes_left += amount

    def player_use_turn(self):
        if self.turns_left > 0:
            self.turns_left -= 1
            return True
        else:
            return False

    def push(self, amount):
    # Implement the action when a player pushes here
        self.pushes_left -= amount
        self.player_use_turn()
        
        print(f"{self.name} pushed {amount} times!")

        
    def player_turn_start(self):
        print(f"It is now {self.name} turn")

    def __str__(self):
        return f"""Player: {self.name}, 
            Color:{self.color}, 
            ID: {self.account_id},
            turns_left : {self.turns_left}, 
            Pushes Left : {self.pushes_left}, 
            Lives Left : {self.lives_left}"""

# player1 = Player("Player 1", "Yellow", "playerid0")
# player2 = Player("Player 2", "Red", "playerid1")

# print(player1)
# print(player2)

# print("\n","\n")

# player1.player_place_piece()
# player1.push(1)
# player2.lose_life()

# print(player1)
# print(player2)

# player2.push(1)
# player2.push(1)

# print("\n","\n")

# print(player1)
# print(player2)

# player1.player_turn_start()

# print(player1)
# print(player2)

# CMD cd src = CD into SRC
#  and python3 player.py to test logic

