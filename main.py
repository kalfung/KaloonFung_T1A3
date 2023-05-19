import random
import sys

class Treasure:
    def __init__(self, gold):
        self.gold = gold

    def set(self, gold):
        self.gold = gold

    def add(self, gold):
        self.gold += gold

    def add_treasure(self, treasure):
        self.add(treasure.gold)

    def __repr__(self):
        return f'Treasure(gold={self.gold})'

    def __str__(self):
        return f'{self.gold}'

class Coffer:
    def __init__(self, gold):
        self.gold = Treasure(gold)

    def loot(self, character):
        character.gold.add_treasure(self.gold)
        self.gold.set(0)
        print(f'You now have {player.gold} pieces of gold.')

# object for combat characters (player and enemy monsters)
class Character:
    def __init__(self, name, maxhealth, attack, cure):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.attack = attack
        self.cure = cure
        self.gold = Treasure(0)

    def attack(self, enemy):
        damage = self.attack
        print(f'You swing your sword at the {enemy.name}!')
        print(f'You deal {damage} damag!')
        enemy.health -= damage
        print(f'The {enemy.name} now has {enemy.health} health.')

    def heal(self):
        self.health += self.cure
        print(f'You cast a healing spell and recover {self.cure} health!')
        print(f'You now have {player.health} health.')

def spawn_coffer():
    coffer = Coffer(random.randint(10, 30))
    with open('coffer.txt') as f:
        contents = f.read()
        print(contents)
    print(f'Do you want to [loot] the coffer, or [ignore] it and continue?')
    while True:
        decision = input().lower()
        if decision == 'ignore':
            print('You ignore the coffer and continue on your way.')
            break
        elif decision == 'loot':
            print(f'The coffer contains {coffer.gold} pieces of gold inside.')
            coffer.loot(player)
            global coffers_looted
            coffers_looted += 1
            break
        else:
            print('Can\'t do that. Try again!')

def spawn_monster():
    enemy = Character('monster', 100, 30, None)
    print('What do you do?')
    while player.health > 0 and enemy.health > 0:
        print(f'Do you [attack] the {enemy.name} or cast a [heal] spell?')
        decision = input().lower()
        if decision == 'heal':
            player.heal()
        elif decision == 'attack':
            player.attack(enemy)
        else:
            print('Can\'t do that. Try again!')
            continue

player = Character('Adventurer', 100, 40, 40)
enemies_encountered = 0
coffers_encountered = 0
coffers_looted = 0
enemies_defeated = 0

while True:
    decision = input('Continue to the next area? (y/n): ').lower()
    if decision == 'n':
        print('Until next time!')
        sys.exit()
    elif decision == 'y':
        encounter = random.randint(1,10)
        if encounter >= 9:
            print(f'{encounter} You discover a treasure coffer!')
            coffers_encountered += 1
            spawn_coffer()
        elif encounter >= 3:
            print(f'{encounter} You run into a monster!')
            enemies_encountered += 1
            spawn_monster()
        else:
            print(f'{encounter} You encounter a treasure trap!')
            enemies_encountered += 1
    else:
        print('Can\'t do that. Try again!')