import random

class Enemy():
    names = open("entities\conf\enemynames.txt", "r")
    enemynames = names.readlines()
    names.close()

    def __init__(self, statBase):
        self.name = ""
        self.hp = 0
        self.maxHp = 0
        self.dmg = 0
        self.generate_random_enemy(statBase)

    def generate_random_enemy(self, statBase):
        self.name = random.choice(self.enemynames)
        self.hp = random.randint(statBase*10, statBase*100)
        self.maxHp = self.hp
        self.dmg = random.randint(statBase*10 - 4, statBase*10 + 2)

    def attack(self, player):
        player.hp -= self.dmg
        if player.hp <= 0:
            player.hp = 0

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0
            return True
        else:
            return False
        
    def serialize(self):
        return {
            "name":self.name,
            'hp':self.hp,
            'maxhp':self.maxHp,
            'dmg':self.dmg
        }