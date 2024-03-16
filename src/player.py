

class Player:
    def __init__(self, name, color, account_id):
        self.name = name
        self.color = color
        self.account_id = account_id
        self.pushes_left = 0   # TODO DEFINE THIS AS VARIABLE
        self.lives_left = 3    # TODO DEFINE THIS AS VARIABLE
    
    def use_push(self):
        if self.pushes_left > 0:
            self.pushes_left -= 1
            return True
        else:
            return False