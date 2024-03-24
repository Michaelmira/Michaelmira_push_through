from random import random
from defines import *
from cube import Cube
from player import Player
class Game():
    def __init__(self, config: dict):
        self.config = self._initialize_config(config)
        self.cube = self._initialize_cube()
        self.players = self._initialize_players()
        self.game_turn = 0
        self.current_player = 0
        self.is_game_over = False
        self.move_history = []
        
    def _initialize_config(self, config_parameters: dict):
        #TODO - use config_parameters object if we want
        return {}

    def _initialize_cube(self):
        cube = Cube(GAME_HEIGHT, GAME_WIDTH, NUM_BOARDS)
        return cube
    
    def _initialize_players(self):
        players = [
            Player("Rob", "Yellow", "playerid0"),
            Player("Mike", "Red", "playerid1")
        ]
        return players
    
    def play_game(self):
        while not self.is_game_over:
            self.play_next_turn()
        print("Game is over. Hope you had fun!")

    def play_next_turn(self):
        self.execute_turn()
        self.check_game_over()
        self.advance_player_turn()
    
    def execute_turn(self):
        move = self.get_move() #get player input
        self.play_move(move) #update the game state
    
    def get_move(self):
        return {
            "player": self.current_player,
            "cell": None
        }
    
    def play_move(self, move: dict):
        if random() < 0.2:
            self.players[self.current_player].lose_life()
            print(f"Player {self.current_player} lost a life and now has {self.players[self.current_player].lives_left} lives left")
        else:
            print("Some other move happened")
        self._update_history(move) #add move to history
        pass
    
    def _update_history(self, move: dict):
        pass
    
    def check_game_over(self):
        for player in self.players:
            if player.lives_left <= 0:
                self.is_game_over = True
                print(f"Game is over, player {player.name} lost")
                return
    
    def advance_player_turn(self):
        self.game_turn += 1
        self.current_player = self.game_turn % len(self.players)
    
    #TODO - might not need this
    # def _reset_game(self):
    #     for player in self.players:
    #         player.score = 0
    #         player.lives_left = TOTAL_LIVES
    #         player.pushes_left = TOTAL_PUSHES
    #     self.cube = self._initialize_cube()
        
    
        
        