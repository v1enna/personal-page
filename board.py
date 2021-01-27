from random import randrange
from snake import Snake

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.blocks = [[False] * self.columns] * self.rows
        self.coin = Coin(randrange(rows), randrange(columns))

        self.starting_position = [randrange(rows), 
                                  randrange(columns)]
        
        self.blocks[self.starting_position[0]][self.starting_position[1]] = True

        self.snake = Snake(self.starting_position)

    def get_snake(self):
        return self.snake

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_starting_position(self):
        return self.starting_position

    def get_coin(self):
        return self.coin

class Coin:
    def __init__(self, x, y):
        self.x = y
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Score:
    def __init__(self):
        self.points = 0

    def get_points(self):
        return self.points

    def set_points(self):
        self.points += 1
        