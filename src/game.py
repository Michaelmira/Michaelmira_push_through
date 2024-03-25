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

    def new_game(self)
    """
    Method to start a new game.
    """
    #TODO logic to initialize a new game
    print("Starting a new game...")
        
            
    def surrender_game(self)
        self.game_over()

    def game_over(self)
        """
        Method to handle actions when the game is over.
        """
        self.save_move_history() # Save move history to Data Storage
        self.save_score_to_leaderboard() # Save total score history to Data Storage
        self.save_win_to_profile() # Save win or loss user to profile history
        self.play_again_questionnaire() # Prompt user whether to play again
        self.terminate_game() #go to home
        self.restart_game() #quickstart new game with same/current settings.

    def play_again_questionnaire():
    """
    Function to prompt the user whether they want to play again.
    """
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == "yes":  # User wants to play again
            self.restart_game()
            return True
        elif response == "no": # User does not want to play again
            self.terminate_game()
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    def restart_game(self):
        for player in self.players:
            player.score = 0
            player.lives_left = TOTAL_LIVES
            player.pushes_left = TOTAL_PUSHES
        self.cube = self._initialize_cube()

    def terminate_game(self)
        """
        Method to terminate the current game.
        """
        self.navigate_to_home()
            #TODO Logic # 
        print("Terminating the current game... Going to home ")

    def navigate_to_home()
        #TODO Direct to homepage.