"""Module for creating and updating enemy"""
import random

class Enemy():
    '''Enemy class'''
    with open("entities\\conf\\enemynames.txt", "r", encoding='UTF-8') as names:
        enemynames = names.readlines()
    names.close()

    def __init__(self, stat_base):
        self.name = ""
        self.hp = 0
        self.max_hp = 0
        self.dmg = 0
        self.generate_random_enemy(stat_base)

    def generate_random_enemy(self, stat_base):
        '''Generating new enemy'''
        self.name = random.choice(self.enemynames)
        self.hp = random.randint(stat_base*10, stat_base*100)
        self.max_hp = self.hp
        self.dmg = random.randint(stat_base*10 - 4, stat_base*10 + 2)

    def attack(self, player):
        '''Attack functionality'''
        player.hp -= self.dmg
        if player.hp <= 0:
            player.hp = 0

    def is_dead(self):
        '''Method to check if player is alive'''
        if self.hp <= 0:
            self.hp = 0
            return True

        return False

    def serialize(self):
        '''Method to serialize object data for json'''
        return {
            "name":self.name,
            'hp':self.hp,
            'max_hp':self.max_hp,
            'dmg':self.dmg
        }
    