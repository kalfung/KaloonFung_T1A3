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
        print(f'You swing your sword at the {enemy.name}!')
        print(f'You deal {damage} damage!')
        enemy.health -= damage
        enemy.health = max(0, enemy.health)
        print(f'The {enemy.name} now has {enemy.health} health.')

    def take_damage(self, enemy):
        damage_variance = random.randint(-5, 5)
        damage = enemy.strength + damage_variance
        self.health -= damage
        self.health = max(0, self.health)  # makes sure health >= 0
        print(f'The {enemy.name} attacks you and deals {damage} damage.')
        print(f'You now have {player.health} health.')

    def heal(self):
        heal_variance = random.randint(-5, 5)
        heal_amount = self.cure + heal_variance
        self.health += heal_amount
        self.health = min(self.health, self.max_health)  # caps health at max
        print(f'You cast a healing spell and recover {heal_amount} health!')
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

def spawn_mimic():
    enemy = Character('mimic', 100, 30, None)
    with open('coffer.txt') as f:
        contents = f.read()
        print(contents)
    print(f'Do you want to [loot] the coffer, or [ignore] it and continue?')
    while True:
        decision = input().lower()
        if decision == 'ignore':
            break
        elif decision == 'loot':
            print(f'The {enemy.name} reveals itself, shedding its glittering disguise and attacks!')
            player.take_damage(enemy)
            print('What do you do?')
        else:
            print('Can\'t do that. Try again!')
    global enemies_defeated
    players_turn = True

    while player.health > 0 and enemy.health > 0:
        if players_turn:
            print(f'Do you [attack] the {enemy.name} or cast a [heal] spell?')
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
        print(f'You have been defeated by the {enemy.name}.')
        print(f'You encountered {enemies_encountered} enemies and encountered {coffers_encountered} coffers.')
        print(f'You defeated {enemies_defeated} enemies and looted {coffers_looted} coffers.')
        quit()
    else:
        print(f'You have successfully defeated the {enemy.name}!')
        enemies_defeated += 1

def spawn_monster():
    enemy = Character('monster', 100, 30, None)
    print(f'You have {player.health} health.')
    # everything after this line in the function is the battle function
    print('What do you do?')
    global enemies_defeated
    players_turn = True

    while player.health > 0 and enemy.health > 0:
        if players_turn:
            print(f'Do you [attack] the {enemy.name} or cast a [heal] spell?')
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
        print(f'You have been defeated by the {enemy.name}.')
        print(f'You encountered {enemies_encountered} enemies and encountered {coffers_encountered} coffers.')
        print(f'You defeated {enemies_defeated} enemies and looted {coffers_looted} coffers.')
        quit()
    else:
        print(f'You have successfully defeated the {enemy.name}!')
        enemies_defeated += 1



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
        #     print(f'{encounter} You run into a monster!')
        #     enemies_encountered += 1
        #     spawn_monster()
        # else:
            print(f'{encounter} You discover a suspicious looking treasure coffer.')
            enemies_encountered += 1
            spawn_mimic()
    else:
        print('Can\'t do that. Try again!')