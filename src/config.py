
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