## TODO: Make a class for robots

# *** Import:
from weapon import Weapon

robot_weapon = Weapon

class Robot:
    #~~~~~ CONSTRUCTOR ~~~~~
    def __init__(self, name):
        self.robo_one_name = name
        self.robot_weapon = Weapon

    #~~~~~ METHODS ~~~~~
    def robos_health(self):
        self.robo_health = 0

    def robo_weap(self):
        self.robot_weapon = Weapon

    def attack(self, dinosaur):
        pass