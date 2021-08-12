from fleet import Fleet
from herd import Herd


class Battlefield:

    #~~~~~ CONSTRUCTOR ~~~~~
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    #~~~~~ METHODS ~~~~~
    def run_game(self):
        pass
    # this is what begins the game and pulls everything together

    def display_welcome(self):
        print("welcome to Robots Vs. Dinosaurs!")
        input("press 'ENTER' to start the game")
        pass

    def battle(self):
        pass
    # this will initiate the turns
        #dinosaurs will attack first, then robots
        #and keep going as long as both sides have health left

    def dino_turn(self, dinosaur):
        pass 
    # dinosaur attacks robot
        # dinosaur does 25 damage
        # robot loses 25 health

    def robo_turn(self, robot):
        pass
    # robot attacks dinosaur
        # robot does 25 damage
        # dinosaur loses 25 health

    def show_dino_opponent_options(self):
        pass
    # display all robots that have health above ZERO
        # this shows options for the dinosaurs to attack
        print(Fleet)

    def show_robo_opponent_options(self):
        pass
    # display all the dinosaurs that have health above ZERO
        # this shows options for the robots to attack
        if(Herd >= 1)
        print(Herd)

    def display_winner(self):
        pass
# when all robots OR all dinos have ZERO health, game over
# the team that still has health wins and gets displayed!