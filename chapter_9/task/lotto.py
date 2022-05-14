from random import choice

class Lotto():
    """Класс игры лото"""
    def __init__(self):
        self.set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
        self.win = ""
        self.ticket = ""

    def get_win_numbers(self):
        """Выиграшная комбинация!"""
        while True:
            self.win += choice(self.set)
            if len(self.win) > 3:
                break
        print(f"Win number: {self.win} ({len(self.win)})")


    def get_my_ticket(self, my_set):
        """Генирация билета!"""
        self.my_set = my_set
        for letter in my_set:
            self.ticket += letter
        print (f"My ticket : {self.ticket}")




game_1 = Lotto()


my_ticket = ['1', 'A', '2', 'B']
game_1.get_my_ticket(my_ticket)



#game_1.get_win_numbers()

attempts = 0

while True:
    attempts += 1
    game_1.get_win_numbers()
    if game_1.win == game_1.ticket:
        game_1.win = ''
        break
    else:
        print(f"{game_1.win}  is not {game_1.ticket}")
        game_1.win = ''
    print("\n")
    
print(f"Attempts = {attempts}.")
