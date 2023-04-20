"""Module for creating and updating shield"""
import random

class Shield():
    '''Method to create and update the shield'''
    shields = open("entities\\conf\\shieldnames.txt", "r", encoding='UTF-8')
    shieldnames = shields.readlines()
    shields.close()

    def __init__(self, max_defense):
        self.name = random.choice(self.shieldnames)
        self.defense = random.randint(max_defense * 10 - 3, max_defense * 10 + 3)

    def serialize(self):
        '''Method to serialize object data for json'''
        return {
            "name":self.name,
            "defense":self.defense
        }
