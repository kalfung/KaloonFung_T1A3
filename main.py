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

class Coffer:
    def __init__(self, gold):
        self.gold = Treasure(gold)

    def loot(self, character):
        character.gold.add_treasure(self.gold)
        self.gold.set(0)
        print(f'You now have {player.gold} gold')

# object for combat characters (player and enemy monsters)
class Character:
    def __init__(self, name, maxhealth, attack, cure):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.attack = attack
        self.cure = cure
        self.gold = Treasure(0)

def spawn_coffer():
    coffer = Coffer(random.randint(10, 30))
    print(f'The coffer contains {coffer.gold} gold inside.')
    print(f'Do you want to [loot] the coffer, or [ignore] it and continue?')
    while True:
        decision = input().lower()
        if decision == 'ignore':
            break
        elif decision == 'loot':
            print(f'The coffer contains {coffer.gold} pieces of gold inside.')
            coffer.loot(player)
            break
        else:
            print('Can\'t do that. Try again!')

player = Character('Adventurer', 100, 40, 40)

while True:
    decision = input('Continue to the next area? (y/n): ').lower()
    if decision == 'n':
        print('Until next time!')
        sys.exit()
    elif decision == 'y':
        encounter = random.randint(1,10)
        if encounter >= 9:
            print(f'{encounter} You discover a treasure coffer!')
            spawn_coffer()
        elif encounter >= 3:
            print(f'{encounter} You run into a monster!')
        else:
            print(f'{encounter} You encounter a treasure trap!')
    else:
        print('Can\'t do that. Try again!')