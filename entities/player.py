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
        self._name = ""
        self._intro_done = False
        self._health = 100
        self._maxhp = 100
        self._sword = None
        self._shield = None
        self._enemy = None
        self._experience = 0
        self._level = 1
        self._prompt = ""
        self._flag = 0

    @property
    def name(self):
        """The name of the player.

        Returns:
            str: The name of the player.
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def intro_done(self):
        """Check whether the player has finished the introduction.

        Returns:
            bool: True if the introduction is finished, False otherwise.
        """
        return self._intro_done

    @intro_done.setter
    def intro_done(self, intro_done):
        self._intro_done = intro_done

    @property
    def health(self):
        """Return the current health of the player.

        The health of the player represents the amount of damage they can withstand
        before losing the game. It is calculated as the difference between the maximum
        health (determined by the player's level) and the damage taken from the enemy
        during battles.
        """
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def maxhp(self):
        """Get the maximum amount of health points (HP) the player can have.

        Returns:
            int: The maximum amount of health points the player can have.
        """
        return self._maxhp

    @maxhp.setter
    def maxhp(self, maxhp):
        self._maxhp = maxhp

    @property
    def sword(self):
        """Get the sword object currently equipped by the player.

        Returns:
            Sword: The sword object equipped by the player.
        """
        return self._sword

    @sword.setter
    def sword(self, sword):
        self._sword = sword

    @property
    def shield(self):
        """Return the current shield level.

        Returns:
            int: The current shield level.
        """
        return self._shield

    @shield.setter
    def shield(self, shield):
        self._shield = shield

    @property
    def enemy(self):
        """
        Get the current enemy of the player.

        Returns:
            Enemy: The current enemy object that the player is facing.
        """
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy

    @property
    def experience(self):
        """
        Get the amount of experience points the player has.

        Returns:
        int: The amount of experience points the player has.
        """
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience

    @property
    def level(self):
        """
        Getter method for the `_level` attribute.

        Returns:
            int: The value of the `_level` attribute.
        """
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def prompt(self):
        """The prompt for the current player to make a move.

        Returns:
            str: The prompt for the current player to make a move.
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        self._prompt = prompt

    @property
    def flag(self):
        """
        Getter method for the flag attribute.

        Returns:
            The current value of the flag attribute.
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        self._flag = flag

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
        if enemy.health - self.sword.damage <= 0:
            enemy.health = 0
        else:
            enemy.health -= self.sword.damage

    def defend(self):
        '''Method to heal the player during combat'''
        self.health += self.shield.defense
        if self.health > self.maxhp:
            self.health = self.maxhp

    def is_dead(self):
        '''To find out if player dead or not'''
        return True if self.health <= 0 else False

    def level_up(self):
        '''Level up handler'''
        self.level += 1
        self.experience = 0
        self.maxhp = self.maxhp + 10
        self.health = self.maxhp
        self.prompt = random.choice(self.promptslist)

    def to_json(self):
        '''Saving object to json'''
        data = {
            'name': self.name,
            'introDone': self.intro_done,
            'health': self.health,
            'maxhp': self.maxhp,
            'experience': self.experience,
            'level': self.level,
            'prompt': self.prompt
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
            self.health = data['health']
            self.maxhp = data['maxhp']
            self.experience = data ['experience']
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
