from random import choice

class RandomWalk():
    """Класс геннирации случайных блужданий"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        """Все блуждания совершаются с точки (0, 0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
