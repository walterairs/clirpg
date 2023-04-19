import random


class Shield():
    shields = open("entities\\conf\\shieldnames.txt", "r")
    shieldnames = shields.readlines()
    shields.close()

    def __init__(self, maxDefense):
        self.name = random.choice(self.shieldnames)
        self.defense = random.randint(maxDefense * 10 - 3, maxDefense * 10 + 3)
