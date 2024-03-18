from defines import *

class Player:

    def __init__(self, name, color, account_id):
        self.name = name
        self.color = color
        self.account_id = account_id
        self.pushes_left = TOTAL_PUSHES  
        self.lives_left = TOTAL_LIVES   
        self.turns_left = TOTAL_TURNS   

    def player_place_piece(self):
        if self.turns_left > 0:
            self.player_use_turn()
            print(f"{self.name} Placed a Piece!")
            
        
        else:
            return print("it is not your turn")


    def lose_life(self, amount):
        self.lives_left -= 1
        print(f"{self.name} lost {amount} Lives!")

    def add_pushes(self,amount):
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
        print(f" It is now {self.name} turn")
        self.turns_left = TOTAL_TURNS

    def __str__(self):
        return f"""Player: {self.name}, 
            Color:{self.color}, 
            ID: {self.account_id},
            turns_left : {self.turns_left}, 
            Pushes Left : {self.pushes_left}, 
            Lives Left : {self.lives_left}"""

player1 = Player("Player 1", "Yellow", "playerid0")
player2 = Player("Player 2", "Red", "playerid1")

print(player1)
print(player2)

print("\n","\n")

player1.player_place_piece()
player1.push(1)
player2.lose_life(1)

print(player1)
print(player2)

player2.push(1)
player2.push(1)

print("\n","\n")

print(player1)
print(player2)

player1.player_turn_start()

print(player1)
print(player2)

# CMD cd src = CD into SRC
#  and python3 player.py to test logic
