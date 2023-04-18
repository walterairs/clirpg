'''
CLI based RPG turn based game where character fights random generated
monsters and gains xp and itmes.
'''

import time
import os
from loadhandler import Persistent
from entities.player import Player

def game_loop(game):
    while game.name == '':
        clear()
        print("Greetings,")
        print("Tell me your name, adventurer!")
        name = input('Enter your name: ')
        game.name = name
        print('Hello, {}!'.format(game.name))
        time.sleep(1)

    while game.introDone == False:
        clear()
        print('Year 20B.c. in the kingdom of Aria')
        print('''
        You are an adventurer in a world full of monsters.
        You have been tasked by the king to slay the endless hoarding monsters
        that have been terrorizing the kingdom.
        You have been given a sword and a shield to help you
        on your quest.
        ''')
        input('Press enter to continue...')
        clear()
        game.generate_sword(game.level)
        game.generate_shield(game.level)
        print('You have been given a sword {}!, it does {} damage!'.format(game.sword.name, game.sword.damage))
        print('You have been given a shield {}!, it has {} defense!'.format(game.shield.name, game.shield.defense))
        input('Press enter to continue...')
        game.introDone = True

    while True:
        clear()
        print('What do you want to do?, {}!'.format(game.name))
        print('''
        1. Fight
        2. Rest
        3. Exit
        ''')
        print('items:')
        print('{} dmg[{}]' .format(game.sword.name, game.sword.damage))
        print('{} def[{}]' .format(game.shield.name, game.shield.defense))
        print('hp: {}'.format(game.hp))
        print('xp: {}'.format(game.xp))
        print('level: {}'.format(game.level))
        choice = input('Enter your choice: ')
        if choice == '1':
            clear()
            game.generate_enemy(game.level)
            print('You have encountered a {}!'.format(game.enemy.name))
            print('stats:')
            print('hp: {}'.format(game.enemy.hp))
            print('damage: {}'.format(game.enemy.dmg))
            input('Press enter to continue...')
            while True:
                clear()
                print('What do you want to do?, {}!'.format(game.name))
                print('''
                1. Attack
                2. Defend
                3. Run
                ''')
                choice = input('Enter your choice: ')
                if choice == '1':
                    game.attack(game.enemy)
                    print('You attacked the {}!'.format(game.enemy.name))
                    print('The {} has {} hp left!'.format(game.enemy.name, game.enemy.hp))
                    time.sleep(1)
                    if game.enemy.hp <= 0:
                        print('You killed the {}!'.format(game.enemy.name))
                        game.xp += 10
                        if game.xp >= 100:
                            game.level += 1
                            game.xp = 0
                            game.maxHp = game.level * 100
                            game.hp = game.maxHp
                            print('You leveled up! You are now level {}!'.format(game.level))
                            print('You gained 10 hp! You now have {} hp!'.format(game.hp))
                        time.sleep(1)
                        game.generate_sword(game.level)
                        game.generate_shield(game.level)
                        print('You found a {}! It does {} damage!'.format(game.sword.name, game.sword.damage))
                        print('You found a {}! It has {} defense!'.format(game.shield.name, game.shield.defense))
                        time.sleep(4)
                        break
                    else:
                        game.enemy.attack(game)
                        print('The {} attacked you!'.format(game.enemy.name))
                        print('You have {} hp left!'.format(game.hp))
                        time.sleep(1)
                        if game.hp <= 0:
                            print('You died!')
                            time.sleep(1)
                            exit()
                elif choice == '2':
                    game.defend()
                    print('You defended against the {}!'.format(game.enemy.name))
                    print('You have {} hp left!'.format(game.hp))
                    time.sleep(1)
                    game.enemy.attack(game)
                    print('The {} attacked you!'.format(game.enemy.name))
                    print('You have {} hp left!'.format(game.hp))
                    time.sleep(1)
                    if game.hp <= 0:
                        print('You died!')
                        time.sleep(1)
                        exit()
                elif choice == '3':
                    print('You ran away!')
                    time.sleep(1)
                    break
                else:
                    print('Invalid choice!')
                    continue
        elif choice == '2':
            print('You rested!')
            time.sleep(1)
            game.hp += 10
            if game.hp > game.maxHp:
                game.hp = game.maxHp
        elif choice == '3':
            data = game.toJSON()
            ##print(data)
            exit()
        else:
            print('Invalid choice!')
            continue

def menu():
    game = None
    
    while True:
        clear()
        print('Welcome to the CLIRPG!')
        print('''
        1. Start Game
        2. Load Game
        3. Exit
        ''')
        choice = input('Enter your choice: ')
        if choice == '1':
            print('Starting game...')
            time.sleep(1)
            game = Player()
        elif choice == '2':
            print('Loading game...')
            time.sleep(1)
        elif choice == '3':
            exit()
        else:
            print('Invalid choice!')
            continue

        if game:
            game_loop(game)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    menu()