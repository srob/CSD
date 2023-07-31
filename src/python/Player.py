class Player:
    def __init__(self, player_type):
        self.player_type = player_type

    def move(self):
        if self.player_type == "Warrior":
            return "Warrior moves forward"
        elif self.player_type == "Mage":
            return "Mage teleports"
        elif self.player_type == "Rogue":
            return "Rogue sneaks"
        else:
            raise ValueError("Invalid player type")
