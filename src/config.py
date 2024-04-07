from __future__ import annotations
from defines import *
from typing import Any
from pprint import pprint
class Config():
    def __init__(self, parameters=dict):
        parameters["num_boards"] = parameters.get("num_boards", DEFAULT_NUM_BOARDS)
        parameters["win_condition"] = parameters.get("win_condition", DEFAULT_WIN_CONDITION)
        parameters["num_players"] = parameters.get("num_players", DEFAULT_NUM_PLAYERS)
        parameters["player_colors"] = parameters.get("player_colors", DEFAULT_PLAYER_COLORS)
        parameters["game_width"] = parameters.get("game_width", DEFAULT_GAME_WIDTH)
        parameters["game_height"] = parameters.get("game_height", DEFAULT_GAME_HEIGHT)
        parameters["total_pushes"] = parameters.get("total_pushes", DEFAULT_NUM_TOTAL_PUSHES)
        parameters["turns_per_move"] = parameters.get("total_turns_per_player", DEFAULT_TURNS_PER_MOVE)
        parameters["turn_time_limit"] = parameters.get("turn_time_limit", DEFAULT_TURN_TIME_LIMIT)
        parameters["num_lives"] = parameters.get("num_lives", DEFAULT_NUM_LIVES)
        
        self.validate_parameters(parameters)
        
        self.parameters = parameters
        
    def validate_parameters(self, parameters: dict):
        """Verifies that the parameters are valid

        Args:
            parameters (dict): _description_
        """
        #TODO - if number of players is not the same as the length of the player colors, complain
        #TODO - if a player color is repeated in the array, complain
        pass
    
    def set_parameter_value(self, parameter_name: str, value: Any):
        """_summary_

        Args:
            parameter_name (str): _description_
            value (Any): _description_
        """
        self.parameters[parameter_name] = value
               
    def get_parameter_value(self, parameter_name: str) -> Any | None:
        """_summary_

        Args:
            parameter_name (str): _description_

        Returns:
            Any: _description_
        """
        return self.parameters.get(parameter_name)

if __name__ == "__main__":
    parameters = {
        "boards": 4,
        "turn_time_limit": 30
    }

    game_config = Config(parameters)

    total_players = game_config.get_parameter_value("total_players")
    print(total_players)
    game_config.set_parameter_value("total_players", 10)
    pprint(game_config.parameters)