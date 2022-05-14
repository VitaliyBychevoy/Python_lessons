from random import randint

class Die():
    """Класс кубик"""
    def __init__(self):
        self.side = 6

    def roll_die(self):
        print(f"Side {str(randint(1, self.side))}.")
