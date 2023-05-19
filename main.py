import random
import sys
import art
from colorama import Fore, Style

# object for gold
class Treasure:
    def __init__(self, gold):
        self.gold = gold

    def set(self, gold):
        self.gold = gold

    def add(self, gold):
        self.gold += gold

    def add_treasure(self, treasure):
        self.add(treasure.gold)

# may not need this repr
    # def __repr__(self):
    #     return f'Treasure(gold={self.gold})'

    def __str__(self):
        return f'{self.gold}'

# object for treasure coffers
class Coffer:
    def __init__(self, gold):
        self.gold = Treasure(gold)

    def loot(self, character):
        character.gold.add_treasure(self.gold)
        self.gold.set(0)
        print(f'You now have {player.gold} pieces of gold.' + Style.RESET_ALL)


# object for combat characters (player and enemy monsters)
class Character:
    def __init__(self, name, max_health, strength, cure):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.cure = cure
        self.gold = Treasure(0)

    def attack(self, enemy):
        damage_variance = random.randint(-5, 5)
        damage = self.strength + damage_variance
        print(Fore.MAGENTA + f'You swing your sword at the {enemy.name}!')
        print(f'You deal {damage} damage!' + Style.RESET_ALL)
        enemy.health -= damage
        enemy.health = max(0, enemy.health)
        print(f'The {enemy.name} now has {enemy.health} health.')

    def take_damage(self, enemy):
        damage_variance = random.randint(-5, 5)
        damage = enemy.strength + damage_variance
        self.health -= damage
        self.health = max(0, self.health)  # makes sure health >= 0
        print(Fore.RED + f'The {enemy.name} attacks you and deals {damage} damage.')
        print(f'You now have {player.health} health.' + Style.RESET_ALL)

    def heal(self):
        heal_variance = random.randint(-5, 5)
        heal_amount = self.cure + heal_variance
        self.health += heal_amount
        self.health = min(self.health, self.max_health)  # caps health at max
        print(Fore.GREEN + f'You cast a healing spell and recover {heal_amount} health!')
        print(f'You now have {player.health} health.' + Style.RESET_ALL)


# treasure coffer spawn function
def spawn_coffer():
    coffer = Coffer(random.randint(10, 30))
    with open('coffer.txt') as f:
        contents = f.read()
        print(contents)
    print('Do you want to ' + Fore.YELLOW + 'loot' + Style.RESET_ALL + ' the coffer, or ' + Fore.RED + 'ignore' + Style.RESET_ALL + ' it and continue?')
    while True:
        decision = input().lower()
        if decision == 'ignore':
            print('You ignore the coffer and continue on your way.')
            break
        elif decision == 'loot':
            print(Fore.YELLOW + f'The coffer contains {coffer.gold} pieces of gold inside.')
            coffer.loot(player)
            global coffers_looted
            coffers_looted += 1
            break
        else:
            print('Can\'t do that. Try again!')


# treasure coffer trap/mimic spawn function
def spawn_mimic():
    enemy = Character('mimic', 100, 30, None)
    with open('coffer.txt') as f:
        contents = f.read()
        print(contents)
    print('Do you want to ' + Fore.YELLOW + 'loot' + Style.RESET_ALL + ' the coffer, or ' + Fore.RED + 'ignore' + Style.RESET_ALL + ' it and continue?')
    while True:
        decision = input().lower()
        if decision == 'ignore':
            print(Fore.GREEN + 'Good choice. That was actually a mimic in disguise!')
            print('You get away safely!' + Style.RESET_ALL)
            break
        elif decision == 'loot':
            print(f'The {enemy.name} reveals itself, shedding its glittering disguise and attacks!')
            player.take_damage(enemy)
            # everything after this line in the function is the battle function
            print('What do you do?')
            global enemies_defeated
            players_turn = True

            while player.health > 0 and enemy.health > 0:
                if players_turn:
                    print('Do you ' + Fore.RED + 'attack' + Style.RESET_ALL + f' the {enemy.name} or cast a ' + Fore.GREEN + 'heal' + Style.RESET_ALL + ' spell?')
                    decision = input().lower()
                    if decision == 'heal':
                        player.heal()
                    elif decision == 'attack':
                        player.attack(enemy)
                    else:
                        print('Can\'t do that. Try again!')
                        continue
                else:
                    print(f'It\'s the {enemy.name}\'s turn.')
                    player.take_damage(enemy)

                players_turn = not players_turn

            if player.health <= 0:
                print(Fore.RED + f'You have been defeated by the {enemy.name}.')
                game_recap()
            else:
                print(Fore.YELLOW + f'You have successfully defeated the {enemy.name}!' + Style.RESET_ALL)
                enemies_defeated += 1
            break
        else:
            print('Can\'t do that. Try again!')


# monster spawn function
def spawn_monster():
    enemy = Character('monster', 100, 30, None)
    with open('monster.txt') as f:
        contents = f.read()
        print(contents)
    print(f'You have {player.health} health.')
    # everything after this line in the function is the battle function
    print('What do you do?')
    global enemies_defeated
    players_turn = True

    while player.health > 0 and enemy.health > 0:
        if players_turn:
            print('Do you ' + Fore.RED + 'attack' + Style.RESET_ALL + f' the {enemy.name} or cast a ' + Fore.GREEN + 'heal' + Style.RESET_ALL + ' spell?')
            decision = input().lower()
            if decision == 'heal':
                player.heal()
            elif decision == 'attack':
                player.attack(enemy)
            else:
                print('Can\'t do that. Try again!')
                continue
        else:
            print(f'It\'s the {enemy.name}\'s turn.')
            player.take_damage(enemy)

        players_turn = not players_turn

    if player.health <= 0:
        print(Fore.RED + f'You have been defeated by the {enemy.name}.')
        game_recap()
    else:
        print(Fore.YELLOW + f'You have successfully defeated the {enemy.name}!' + Style.RESET_ALL)
        enemies_defeated += 1

# function to display tally of enemy and coffer encounters
def game_recap():
    print(Fore.CYAN)
    print(f'You encountered {enemies_encountered} enemies and {coffers_encountered} coffers.')
    print(f'You defeated {enemies_defeated} enemies and looted {coffers_looted} coffers.')
    print(Style.RESET_ALL)
    sys.exit()

# declaring global variables
player = Character('Adventurer', 100, 40, 50)
enemies_encountered = 0
enemies_defeated = 0
coffers_encountered = 0
coffers_looted = 0


# main game code
print('You arrive at the entrance of the caverns.')
print('Armed with your trusty sword and handful of spells, you venture into the dark depths before you.')
art.aprint('sword6')
while True:
    decision = input('Continue to the next area? [y/n]: ').lower()
    if decision == 'n':
        print('Until next time!')
        game_recap()
    elif decision == 'y':
        encounter = random.randint(1,10)
        if encounter >= 9:
            print(Fore.YELLOW + 'You discover a glittering treasure coffer!')
            print(Style.RESET_ALL)
            coffers_encountered += 1
            spawn_coffer()
        elif encounter >= 3:
            print(Fore.RED + 'You run into a monster!')
            print(Style.RESET_ALL)
            enemies_encountered += 1
            spawn_monster()
            coffer_drop = random.randint(1, 10)
            if coffer_drop >= 9:
                print(Fore.YELLOW + 'Huzzah! Upon its defeat, the monster drops a bonus treasure coffer!')
                print(Style.RESET_ALL)
                coffers_encountered += 1
                spawn_coffer ()
            else:
                pass
        else:
            print(Fore.YELLOW + 'You discover a suspicious looking treasure coffer.')
            print(Style.RESET_ALL)
            enemies_encountered += 1
            spawn_mimic()
    else:
        print('Can\'t do that. Try again!')