'''
CLI based RPG turn based game where character fights random generated
monsters and gains xp and itmes.
'''

import time
import os
from entities.player import Player
from entities.conf.colors import Colors

def game_loop(game):
    '''Intro to the game'''
    while game.name == '':
        clear()
        print(Colors.OKGREEN + "Greetings," + Colors.ENDC)
        print("Tell me your name, adventurer!")
        name = input('Enter your name: ')
        game.name = name
        print(f'Hello, {game.name}!')
        time.sleep(1)

    while game.intro_done is False:
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
        print(f'You have been given a sword {game.sword.name}')
        print(
            Colors.FAIL +
            f'It does {game.sword.damage} damage!'  +
            Colors.ENDC)
        print(f'You have been given a shield {game.shield.name}')
        print(
            Colors.OKBLUE +
            f'It has {game.shield.defense} defense!' +
            Colors.ENDC)
        input('Press enter to continue...')
        game.intro_done = True

    while True:
        clear()
        print(f'What do you want to do?, {game.name}!')
        print('''
        1. Fight
        2. Rest
        3. Exit
        ''')
        print('items:')


        print(f'{game.sword.name} dmg[{game.sword.damage}]')
        print(f'{game.shield.name} def[{game.shield.defense}]')
        print(f'hp: {game.hp}')
        print(f'xp: {game.xp}')
        print(f'level: {game.level}')
        game.generate_enemy(game.level)
        choice = input('Enter your choice: ')
        if choice == '1':
            clear()
            print(f'You have encountered a {game.enemy.name}!')
            print('stats:')
            print(f'hp: {game.enemy.hp}')
            print(f'damage: {game.enemy.dmg}')
            input('Press enter to continue...')
            while True:
                clear()
                print(f'What do you want to do?, {game.name}!')
                print('''
                1. Attack
                2. Defend
                3. Run
                ''')
                choice = input('Enter your choice: ')
                if choice == '1':
                    game.attack(game.enemy)
                    print(f'You attacked the {game.enemy.name}!')
                    print(
                        f'The {game.enemy.name} has {game.enemy.hp} hp left!')
                    time.sleep(1)
                    if game.enemy.hp <= 0:
                        print(f'You killed the {game.enemy.name}!')
                        game.xp += 50
                        if game.xp >= 100:
                            game.level_up()
                            print(f'You leveled up! You are now level {game.level}!')
                            print(f'You gained 10 hp! You now have {game.hp} hp!')
                            input('Press enter to continue...')
                            clear()
                            print(f'{game.prompt}')
                            input('Press enter to continue...')
                            clear()
                        time.sleep(1)
                        game.generate_sword(game.level)
                        game.generate_shield(game.level)
                        print(f'You found a {game.sword.name}! It does {game.sword.damage} damage!')
                        print(
                            f'You found a {game.shield.name}! It has {game.shield.defense} defense!'
                            )
                        time.sleep(4)
                        break
                    else:
                        game.enemy.attack(game)
                        print(f'The {game.enemy.name} attacked you!')
                        print(f'You have {game.hp} hp left!')
                        time.sleep(1)
                        if game.hp <= 0:
                            print('You died!')
                            time.sleep(1)
                            exit()
                elif choice == '2':
                    game.defend()
                    print(f'You defended against the {game.enemy.name}!')
                    print(f'You have {game.hp} hp left!')
                    time.sleep(1)
                    game.enemy.attack(game)
                    print(f'The {game.enemy.name} attacked you!')
                    print(f'You have {game.hp} hp left!')
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
            while True:
                user_input = input("Do you want to save? Y/N ").upper()
                if user_input == 'Y':
                    print("Saving...")
                    game.to_json()
                    exit()
                elif user_input == 'N':
                    print("You did not save")
                    exit()
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")

        else:
            print('Invalid choice!')
            continue


def menu():
    '''Main menu'''
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
            game = Player()
            print('Loading game...')
            game.from_json()
            time.sleep(1)
        elif choice == '3':
            exit()
        else:
            print('Invalid choice!')
            continue

        if game:
            game_loop(game)


def clear():
    '''FOr clearing the terminal window'''
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    menu()
