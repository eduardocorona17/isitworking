from random import randint, choice

class Dice:
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        print(f"{randint(1,6)}")

die = Dice()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()