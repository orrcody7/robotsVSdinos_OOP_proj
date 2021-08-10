## TODO: Make a class for robots

# *** Import:
from weapon import Weapon



class Robot:
    #~~~~~ CONSTRUCTOR ~~~~~
    def __init__(self, name):
        self.robo_one_name = name
        self.robot_weapon = Weapon
        self.health = 200

    #~~~~~ METHODS ~~~~~
    def attack(self, dinosaur):
        pass