from random import choice, randint

players = ['jack', 'mark', 'michel', 'ali', 'tyson']

print(choice(players))


class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        roll_side = randint(1, self.side)
        print(f"your die roll to {roll_side}")


my_die = Die(5)

my_die.roll_die()
