from entities.enemy import Enemy
from entities.sword import Sword
from entities.shield import Shield
from types import SimpleNamespace
import random
import json
import loadhandler

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
        self.flag = 0

    def generate_sword(self, maxDamage):
        self.sword = Sword(maxDamage)
        self.flag = 1

    def generate_shield(self, maxDefense):
        self.shield = Shield(maxDefense)
        self.flag = 1

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
        self.maxHp = self.level * 10
        self.hp = self.maxHp
        self.prompt = random.choice(self.promptslist)

    def toJSON(self):
        data = {
            'name':self.name,
            'introDone':self.introDone,
            'hp':self.hp,
            'maxhp':self.maxHp,
            'xp':self.xp,
            'level':self.level,
            'prompt':self.prompt
        }
        loadhandler.Persistent.serjson('entities/player.json', data)
        if self.flag == 1:
            loadhandler.Persistent.serjson('entities/sword.json', self.sword.serialize())
            loadhandler.Persistent.serjson('entities/shield.json', self.shield.serialize())
        loadhandler.Persistent.serjson('entities/enemy.json', self.enemy.serialize())

    def fromJSON(self):
        data = loadhandler.Persistent.resjson('entities/player.json')
        if 'name' in data:
                self.name = data['name']
                self.introDone = data['introDone']
                self.hp = data['hp']
                self.maxHp = data['maxhp']
                self.xp = data ['xp']
                self.level = data ['level']
                self.prompt = data ['prompt']

        swordDataPath = 'entities/sword.json'
        with open(swordDataPath, 'r') as j:
            swordcontent = json.load(j, object_hook=lambda d: SimpleNamespace(**d))
        self.sword = swordcontent

        shieldDataPath = 'entities/shield.json'
        with open(shieldDataPath, 'r') as k:
            shieldcontent = json.load(k, object_hook=lambda d: SimpleNamespace(**d))
        self.shield = shieldcontent

        enemyDataPath = 'entities/enemy.json'
        with open(enemyDataPath, 'r') as n:
            enemycontent = json.load(n, object_hook=lambda d: SimpleNamespace(**d))
        self.enemy = enemycontent