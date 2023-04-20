import random

class Sword():
    swords = open("entities\\conf\\swordnames.txt", "r")
    swordnames = swords.readlines()
    swords.close()

    def __init__(self, maxDamage):
        self.name = random.choice(self.swordnames)
        self.damage = random.randint(maxDamage * 10 - 3, maxDamage * 10 + 3)

    def serialize(self):
        return {
            "name":self.name,
            "damage":self.damage
        }