## TODO: Make a class for fleet

# ** Import:
from robot import Robot



class Fleet:
    #~~~~~ CONSTRUCTOR ~~~~~~
    def __init__(self):
        self.robots = []


    #~~~~~ METHODS ~~~~~
    def create_fleet(self):
        robot_one = Robot("WALL-E")
        robot_two = Robot("EVA")
        robot_three = Robot("Bender")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
        