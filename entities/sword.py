"""Needed for randomization"""
import random

class Sword():
    '''Method to create and update the sword'''
    swords = open("entities\\conf\\swordnames.txt", "r", encoding='UTF-8')
    swordnames = swords.readlines()
    swords.close()

    def __init__(self,maxDamage):
        self.name = random.choice(self.swordnames)
        self.damage = random.randint(maxDamage * 10 - 3, maxDamage * 10 + 3)

    def serialize(self):
        '''Method to serialize object data for json'''
        return {
            "name":self.name,
            "damage":self.damage
        }
    