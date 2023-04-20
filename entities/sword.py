"""Module for creating and updating sword"""
import random

class Sword():
    '''Method to create and update the sword'''
    with open("entities\\conf\\swordnames.txt", "r", encoding='UTF-8') as swords:
        swordnames = swords.readlines()
    swords.close()

    def __init__(self,max_damage):
        self.name = random.choice(self.swordnames)
        self.damage = random.randint(max_damage * 10 - 3, max_damage * 10 + 3)

    def serialize(self):
        '''Method to serialize object data for json'''
        return {
            "name":self.name,
            "damage":self.damage
        }
    