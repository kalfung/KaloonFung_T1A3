import random
import sys
import objects



while True:
    decision = input('COntinue to the next area? (y/n): ').lower()
    if decision == 'n':
        print('Until next time!')
        sys.exit()
    elif decision == 'y':
        encounter = random.randint(1,10)
        if encounter >= 9:
            print(f'{encounter} You discover a treasure coffer!')
        elif encounter >= 3:
            print(f'{encounter} You run into a monster!')
        else:
            print(f'{encounter} You encounter a treasure trap!')
    else:
        print('Can\'t do that. Try again!')