## TODO: Make a class for robots

# *** Import:
from weapon import Weapon



class Robot:
    #~~~~~ CONSTRUCTOR ~~~~~ "the Robot Has..."
    def __init__(self, name, health):
        self.robot_name = name
        self.health = health
        self.robot_weapon = Weapon()


    #~~~~~ METHODS ~~~~~


    def attack(self, dinosaur):
        pass
   
    # ***   figure out if I need to make a loop/ if/elif 
    # ***   statement. not sure what I need to do 
    # ***   for this method
    