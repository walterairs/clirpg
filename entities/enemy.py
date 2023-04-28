"""Module for creating and updating enemy"""
import random

class Enemy():
    '''Enemy class'''
    with open("entities\\conf\\enemynames.txt", "r", encoding='UTF-8') as names:
        enemynames = names.readlines()
    names.close()

    def __init__(self, stat_base):
        '''Initializes a new enemy object with random stats'''
        self.name = ""
        self.name = ""
        self.health = 0
        self.maxhp = 0
        self.dmg = 0
        self.generate_random_enemy(stat_base)

    def generate_random_enemy(self, stat_base):
        '''Generating new enemy'''
        self.name = random.choice(self.enemynames)
        self.health = random.randint(stat_base*10, stat_base*100)
        self.maxhp = self.health
        self.dmg = random.randint(stat_base*10 - 4, stat_base*10 + 2)

    def attack(self, player):
        '''Attack functionality'''
        player.health -= self.dmg
        if player.health <= 0:
            player.health = 0

    def is_dead(self):
        '''Method to check if player is alive'''
        if self.health <= 0:
            self.health = 0
            return True

        return False

    def serialize(self):
        '''Method to serialize object data for json'''
        return {
            "name":self.name,
            'health':self.health,
            'maxhp':self.maxhp,
            'dmg':self.dmg
        }
    