"""Module for creating and updating shield"""
import random

class Shield():
    '''Class for creating and updating a shield.'''
    with open("entities\\conf\\shieldnames.txt", "r", encoding='UTF-8') as shields:
        shieldnames = shields.readlines()
    shields.close()

    def __init__(self, max_defense):
        '''Initializes a new shield object with a random name and defense value.'''
        self.name = random.choice(self.shieldnames)
        self.defense = random.randint(max_defense * 10 - 3, max_defense * 10 + 3)

    def serialize(self):
        '''Returns a dictionary with the shield's data for JSON serialization.'''
        return {
            "name":self.name,
            "defense":self.defense
        }
