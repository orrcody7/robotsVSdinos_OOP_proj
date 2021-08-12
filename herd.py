## TODO: Make a class for herd


# ** Import:
from dinosaur import Dinosaur


class Herd:
    #~~~~~ CONSTRUCTOR ~~~~~
    def __init__(self):
        self.dinosaurs = []


    #~~~~~ METHODS ~~~~~
    def create_herd(self):
        dino_one = Dinosaur("T Rex")
        dino_two = Dinosaur("Velociraptor")
        dino_three = Dinosaur("Triceratops")
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
