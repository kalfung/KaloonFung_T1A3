import random
import sys

class Gold:
    def __init__(self, gold):
        self.gold = gold

    def set(self, gold):
        self.gold = gold

    def add(self, gold):
        self.gold += gold

    def add_gold(self, gold):
        self.add(gold)

class Coffer:
    def __init__(self, gold):
        self.gold = gold

    def loot(self, character):
        character.gold.add(self.gold)
        self.gold.set(0)
        print(f'You now have {player.gold} gold')

# object for combat characters (player and enemy monsters)
class Character:
    def __init__(self, name, maxhealth, attack, cure, gold):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.attack = attack
        self.cure = cure
        self.gold = gold

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

while True:
    decision = input('COntinue to the next area? (y/n): ').lower()
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