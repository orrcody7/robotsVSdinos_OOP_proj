## TODO: Make a class for Weapons


class Dinosaur:
    #~~~~~ CONSTRUCTOR ~~~~~
    def __init__(self, name, attack_power):
        self.dino_name = name
        self.atk_power = attack_power
        self.health = 0

    def attack_power(self):
        self.atk_power = 25

    def dino_attack(self, robot):
        pass