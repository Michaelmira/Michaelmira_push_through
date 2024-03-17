from defines import *

class Player:
    TOTAL_LIVES = 3
    TOTAL_PUSHES = 3

    def __init__(self, name, color, account_id):
        self.name = name
        self.color = color
        self.account_id = account_id
        self.pushes_left = TOTAL_PUSHES  
        self.lives_left = TOTAL_LIVES   
    
    def use_push(self):
        if self.pushes_left > 0:
            self.pushes_left -= 1
            return True
        else:
            return False

    def lose_life(self, amount):
        self.lives_left -= 1
        print(f"{self.name} lost {amount} Lives!")

    def add_pushes(self,amount):
        self.pushes_left += amount

    def push(self, amount):
    # Implement the action when a player pushes here
        self.pushes_left -= amount
        print(f"{self.name} pushed {amount} times!")

    def __str__(self):
        return f"""Player: {self.name}, 
            Color:{self.color}, 
            ID: {self.account_id}, 
            Pushes Left : {self.pushes_left}, 
            Lives Left : {self.lives_left}"""

player1 = Player("Player 1", "Yellow", "playerid0")
player2 = Player("Player 2", "Red", "playerid1")

print(player1)
print(player2)

print("\n","\n")

player1.push(1)
player2.lose_life(1)

print(player1)
print(player2)

player2.push(1)
player2.push(1)

print("\n","\n")

print(player1)
print(player2)


# CD int o SRC and python3 player.py to test logic

