

class Game():
    def __init__(self, config: dict):
        self.config = self._initialize_config(config)
        self.cube = self._initialize_cube()
        self.players = self._initialize_players()
        self.current_player = 0
        self.current_score = self._initialize_score()
        self.is_game_over = False
        self.move_history = []
        
    def _initialize_config(self, config_parameters: dict):
        pass

    def _initialize_cube(self):
        pass
    
    def _initialize_players(self):
        pass
    
    def _initialize_score(self):
        pass
        