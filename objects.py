class Player:
    def __init__(self, name, maxhealth, attack, cure, gold):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.attack = attack
        self.cure = cure
        self.gold = gold
        self.alive = True