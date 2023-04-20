"""Module for player functionalities"""
from types import SimpleNamespace
import random
import json
from entities.enemy import Enemy
from entities.sword import Sword
from entities.shield import Shield
import loadhandler

class Player():
    '''Player class'''
    prompts = open("entities\\conf\\prompts.txt", "r", encoding='UTF-8')
    promptslist = prompts.readlines()
    prompts.close()

    def __init__(self):
        self.name = ""
        self.intro_done = False
        self.hp = 100
        self.max_hp = 100
        self.sword = None
        self.shield = None
        self.enemy = None
        self.xp = 0
        self.level = 1
        self.prompt = ""
        self.flag = 0

    def generate_sword(self, max_damage):
        '''Method to create sword'''
        self.sword = Sword(max_damage)
        self.flag = 1

    def generate_shield(self, max_defense):
        '''Method to create shield'''
        self.shield = Shield(max_defense)
        self.flag = 1

    def generate_enemy(self, stat_base):
        '''Method to create enemy'''
        self.enemy = Enemy(stat_base)

    def attack(self, enemy):
        '''Method to attack'''
        if enemy.hp - self.sword.damage <= 0:
            enemy.hp = 0
        else:
            enemy.hp -= self.sword.damage

    def defend(self):
        '''Method to heal the player during combat'''
        self.hp += self.shield.defense
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_dead(self):
        '''To find out if player dead or not'''
        if self.hp <= 0:
            return True
        else:
            return False

    def level_up(self):
        '''Level up handler'''
        self.level += 1
        self.xp = 0
        self.max_hp = self.level * 10
        self.hp = self.max_hp
        self.prompt = random.choice(self.promptslist)

    def to_json(self):
        '''Saving object to json'''
        data = {
            'name':self.name,
            'introDone':self.intro_done,
            'hp':self.hp,
            'max_hp':self.max_hp,
            'xp':self.xp,
            'level':self.level,
            'prompt':self.prompt
        }
        loadhandler.Persistent.serjson('entities/player.json', data)
        if self.flag == 1:
            loadhandler.Persistent.serjson('entities/sword.json', self.sword.serialize())
            loadhandler.Persistent.serjson('entities/shield.json', self.shield.serialize())
        loadhandler.Persistent.serjson('entities/enemy.json', self.enemy.serialize())

    def from_json(self):
        '''Loading object from json'''
        data = loadhandler.Persistent.resjson('entities/player.json')
        if 'name' in data:
            self.name = data['name']
            self.intro_done = data['introDone']
            self.hp = data['hp']
            self.max_hp = data['max_hp']
            self.xp = data ['xp']
            self.level = data ['level']
            self.prompt = data ['prompt']

        sword_data_path = 'entities/sword.json'
        with open(sword_data_path, 'r', encoding='UTF-8') as j:
            swordcontent = json.load(j, object_hook=lambda d: SimpleNamespace(**d))
        self.sword = swordcontent

        shield_data_path = 'entities/shield.json'
        with open(shield_data_path, 'r', encoding='UTF-8') as k:
            shieldcontent = json.load(k, object_hook=lambda d: SimpleNamespace(**d))
        self.shield = shieldcontent

        enemy_data_path = 'entities/enemy.json'
        with open(enemy_data_path, 'r', encoding='UTF-8') as edp:
            enemycontent = json.load(edp, object_hook=lambda d: SimpleNamespace(**d))
        self.enemy = enemycontent
