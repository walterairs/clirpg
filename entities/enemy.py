import random

class Enemy():
    names = open("entities/enemynames.txt", "r")
    enemynames = names.readlines()
    names.close()

    def __init__(self):
        self.name = ""
        self.hp = 0
        self.maxHp = 0
        self.dmg = 0
        self.generate_random_enemy()

    def generate_random_enemy(self):
        self.name = random.choice(self.enemynames)
        self.hp = random.randint(10, 100)
        self.maxHp = self.hp
        self.dmg = random.randint(1, 10)

    def attack(self, player):
        player.hp -= self.dmg
        if player.hp <= 0:
            player.hp = 0

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False