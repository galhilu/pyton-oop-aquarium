MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_WIDTH
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        pass

    def get_food(self):
        return self.food

    def get_age(self):
        return self.age

    def dec_food(self):
        self.food = self.food-1
        return None

    def inc_age(self):
        self.age = self.age+1
        return None

    def right(self):
        self.x =  self.x+1
        return None

    def left(self):
        self.x = self.x - 1
        return None

    def get_position(self):
        return (self.y,self.x)

    def set_x(self, x):
        self.x = x
        return None

    def set_y(self, y):
        self.y = y
        return None

    def starvation(self):
        print("The fish %Name died at the age of %Age years Because he ran out of food!")
        return None

    def die(self):
        print("%AnimalName died in good health")
        return None

    def get_directionH(self):
        return self.directionH

    def set_directionH(self, directionH):
        self.directionH = directionH
        return None

    def get_alive(self):
       return self.alive

    def get_size(self):
        return (self.width,self.height)

    def get_food_amount(self):
        return self.food

    def add_food(self, amount):
        self.food = self.food + amount
        return None

    def get_animal(self):
        pass