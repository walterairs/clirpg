from entities.enemy import Enemy
from entities.sword import Sword
from entities.shield import Shield
import random
import json


class Player():
    prompts = open("entities\\conf\\prompts.txt", "r")
    promptslist = prompts.readlines()
    prompts.close()

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
        self.prompt = ""

    def generate_sword(self, maxDamage):
        self.sword = Sword(maxDamage)

    def generate_shield(self, maxDefense):
        self.shield = Shield(maxDefense)

    def generate_enemy(self, statBase):
        self.enemy = Enemy(statBase)

    def attack(self, enemy):
        if enemy.hp - self.sword.damage <= 0:
            enemy.hp = 0
        else:
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

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.maxHp = self.level * 100
        self.hp = self.maxHp
        self.prompt = random.choice(self.promptslist)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
