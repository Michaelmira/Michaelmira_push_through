
class config():
    def __init__(self):
        self.boards = None
        self.win_condition = None
        self.player_colors = None
        self.game_width = None
        self.game_height = None
        self.total_pushes = None
        self.total_turns_per_player = None
        self.turn_time_limit = None

    def set_boards(self, boards):
        self.boards = boards

    def set_win_condition(self, win_condition):
        self.win_condition = win_condition

    def set_player_colors(self, player_colors):
        self.player_colors = player_colors

    def set_game_width(self, game_width):
        self.game_width = game_width

    def set_game_height(self, game_height):
        self.game_height = game_height

    def set_total_pushes(self, total_pushes):
        self.total_pushes = total_pushes

    def set_total_turns_per_player(self, total_turns_per_player):
        self.total_turns_per_player = total_turns_per_player

    def set_turn_time_limit(self, turn_time_limit):
        self.turn_time_limit = turn_time_limit

    def get_boards(self):
        return self.boards

    def get_win_condition(self):
        return self.win_condition

    def get_player_colors(self):
        return self.player_colors

    def get_game_width(self):
        return self.game_width

    def get_game_height(self):
        return self.game_height

    def get_total_pushes(self):
        return self.total_pushes

    def get_total_turns_per_player(self):
        return self.total_turns_per_player

    def get_turn_time_limit(self):
        return self.turn_time_limit

game_config = Config()
game_config.set_boards(4)
game_config.set_win_condition(2)
game_config.set_player_colors(["red", "yellow", "green", "blue"])
game_config.set_game_width(8)
game_config.set_game_height(8)
game_config.set_total_pushes(10)
game_config.set_total_turns_per_player(5)
game_config.set_turn_time_limit(60)

print("Number of boards:", game_config.get_boards())
print("Win condition:", game_config.get_win_condition())
print("Player colors:", game_config.get_player_colors())
print("Game width:", game_config.get_game_width())
print("Game height:", game_config.get_game_height())
print("Total pushes:", game_config.get_total_pushes())
print("Total turns per player:", game_config.get_total_turns_per_player())
print("Turn time limit:", game_config.get_turn_time_limit())