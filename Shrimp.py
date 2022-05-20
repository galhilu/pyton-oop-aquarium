import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        if self.directionH == 0:
            animal = [['*',' ','*',' ',' ',' ',' '], [' ','*','*','*','*','*','*',], [' ',' ','*',' ','*',' ',' ']]
        if self.directionH == 1:
            animal = [[' ',' ',' ',' ','*',' ','*'], ['*','*','*','*','*','*',' '], [' ',' ','*',' ','*',' ',' ']]
        return animal

    def get_blank_animal(self):
        animal = [[' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',], [' ',' ',' ',' ',' ',' ',' ']]
        return animal