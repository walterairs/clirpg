from entities.enemy import Enemy
import random

class Player():

    def __init__(self):
        self.name = ""
        self.introDone = False
        self.hp = 100
        self.maxHp = 100
        self.sword = None
        self.shield = None
        self.enemy = None
        self.xp = 0
        self.level = 1

    def generate_sword(self, maxDamage):
        self.sword = Sword(maxDamage)

    def generate_shield(self, maxDefense):
        self.shield = Shield(maxDefense)

    def generate_enemy(self):
        self.enemy = Enemy()

    def attack(self, enemy):
        enemy.hp -= self.sword.damage

    def defend(self):
        self.hp += self.shield.defense
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False


class Sword():
    ##Take swordnames from a file swordnames.txt
    swords = open("entities/swordnames.txt", "r")
    swordnames = swords.readlines()
    swords.close()

    def __init__(self, maxDamage):
        self.name = random.choice(self.swordnames)
        self.damage = random.randint(maxDamage*10 - 3, maxDamage*10 + 3)


class Shield():
    shields = open("entities/shieldnames.txt", "r")
    shieldnames = shields.readlines()
    shields.close()

    def __init__(self, maxDefense):
        self.name = random.choice(self.shieldnames)
        self.defense = random.randint(maxDefense*10 - 3, maxDefense*10 + 3)