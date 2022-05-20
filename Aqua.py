import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []

    def build_tank(self):
        y = self.board
        for n in range(self.aqua_height):
            x = ["|"]
            for i in range(self.aqua_width - 2):
                x.append(" ")
            x.append("|")
            y[n] = x.copy()
        y[-1] = "\\" + "_" * (self.aqua_width - 2) + "/"
        y[2] = "|" + "~" * (self.aqua_width - 2) + "|"
        self.board = y
        return None

    def print_board(self):
        board = self.get_board()
        for i in board:
            print(*i)
        return None

    def get_board(self):
        return self.board

    def get_all_animal(self):
        return self.anim

    def is_collision(self, animal):
        board = self.get_board()
        if animal.directionH == 0:
            for i in range(0,3):
                if board[animal.y + i][animal.x-1] == "*":
                    return True
        if animal.directionH == 1:
            for i in range(0, 3):
                if board[animal.y + i][animal.x + 7] == "*":
                    return True
        return False

    def print_animal_on_board(self, animal: Animal):
        board = self.board
        arry = animal.get_animal()
        for i in range(len(arry)):
            board[animal.y+i] = list(board[animal.y+i][:animal.x]) + list(arry[i]) + list(board[animal.y + i][animal.x + len(arry[0]):])
        self.board = board
        return None

    def delete_animal_from_board(self, animal: Animal):
        board = self.board
        arry = animal.get_blank_animal()
        for i in range(animal.height):
            board[animal.y+i] = list(board[animal.y+i][:animal.x]) + list(arry[i]) +list(board[animal.y + i][animal.x + len(arry[0]):])
        self.board = board
        return None

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):

        if fishtype == "mo":
            if x+8 >= self.aqua_width:
                x = self.aqua_width-9
            if y+3 >= self.aqua_height - MAX_CRAB_HEIGHT:
                y = self.aqua_height - MAX_CRAB_HEIGHT-4
            for i in range(0,3):
                for n in range(0,8):
                    if self.check_if_free(x+n, y+i) is False:
                        print("The place is not available! Please try again later.")
                        return False

            nfish = Moly.Moly(name, age, x, y, directionH, directionV)
            self.print_animal_on_board(nfish)
            self.anim.append(nfish)
            return True

        if fishtype == "sc":
            if x+8 >= self.aqua_width:
                x = self.aqua_width-9
            if y+5 >= self.aqua_height-MAX_CRAB_HEIGHT:
                y = self.aqua_height-MAX_CRAB_HEIGHT-6
            for i in range(0,5):
                for n in range(0,8):
                    if self.check_if_free(x+n, y+i) is False:
                        print("The place is not available! Please try again later.")
                        return False

            nfish = Scalar.Scalar(name, age, x, y, directionH, directionV)
            self.print_animal_on_board(nfish)
            self.anim.append(nfish)
            return True

        return False

    def add_crab(self, name, age, x, y, directionH, crabtype):
        if x+7 >= self.aqua_width:
            x = self.aqua_width-8
        if crabtype == "oc":
            y = self.aqua_height - 5
            for i in range(0,4):
                for n in range(0,7):
                    if self.check_if_free(x+n, y+i) is False:
                        print("The place is not available! Please try again later.")
                        return False

            ncrab = Ocypode.Ocypode(name, age, x, y, directionH,)
            self.anim.append(ncrab)
            self.print_animal_on_board(ncrab)
            return True

        if crabtype == "sh":
            y = self.aqua_height - 4
            for i in range(0,3):
                for n in range(0,7):
                    if self.check_if_free(x+n, y+i) is False:
                        print("The place is not available! Please try again later.")
                        return False

            ncrab = Shrimp.Shrimp(name, age, x, y, directionH, )
            self.anim.append(ncrab)
            self.print_animal_on_board(ncrab)
            return True
        return False

    def check_if_free(self, x, y) -> bool:
        board = self.get_board()
        if board[y][x] == " ":
            return True
        else:
            return False

    def left(self, a):
        if a.x -1 == 0:
            self.delete_animal_from_board(a)
            a.directionH = 1
            self.print_animal_on_board(a)
        else:
            self.delete_animal_from_board(a)
            a.x = a.x -1
            self.print_animal_on_board(a)
        return None

    def right(self, a):
        if a.x + a.width +1 == self.aqua_width:
            self.delete_animal_from_board(a)
            a.directionH = 0
            self.print_animal_on_board(a)
        else:
            self.delete_animal_from_board(a)
            a.x = a.x + 1
            self.print_animal_on_board(a)
        return None

    def up(self, a):
        if a.y - 1 == 2:
            self.delete_animal_from_board(a)
            a.directionV = 0
            self.print_animal_on_board(a)
        else:
            self.delete_animal_from_board(a)
            a.y = a.y - 1
            self.print_animal_on_board(a)
        return None

    def down(self, a):
        if a.y + a.height == self.aqua_height - (MAX_CRAB_HEIGHT+1):
            self.delete_animal_from_board(a)
            a.directionV = 1
            self.print_animal_on_board(a)
        else:
            self.delete_animal_from_board(a)
            a.y = a.y + 1
            self.print_animal_on_board(a)
        return None

    def next_turn(self):
        a = self.anim
        if self.turn % 10 == 0:
            indx = 0
            for i in a:
                i.dec_food()
                if i.food == 0:
                    i.starvation()
                    self.delete_animal_from_board(i)
                    del a[indx]
                indx = indx + 1

        if self.turn % 100 == 0:
            indx=0
            for i in a:
                i.inc_age()
                if i.age == 120:
                    i.die()
                    self.delete_animal_from_board(i)
                    del a[indx]
                indx=indx+1

        for i in a:
            if isinstance(i, Scalar.Scalar) or isinstance(i, Moly.Moly):
                if i.directionV == 1:
                    self.up(i)
                else:
                    self.down(i)
                if i.directionH == 0:
                    self.left(i)
                else:
                    self.right(i)

            if isinstance(i, Ocypode.Ocypode) or isinstance(i, Shrimp.Shrimp):
                if i.directionH == 0:
                    if self.is_collision(i) is False:
                        self.left(i)
                    else:
                        i.directionH=1
                        self.right(i)
                else:
                    if i.directionH == 1:
                        if self.is_collision(i) is False:
                            self.right(i)
                        else:
                            i.directionH = 0
                            self.left(i)
        print(self.turn)
        self.print_all()
        self.turn += 1
        return None

    def print_all(self):
        a = self.get_all_animal()
        for i in a:
            print(i.__str__())
        return None

    def feed_all(self):
        a = self.anim
        for i in a:
            i.add_food(FEED_AMOUNT)
        return None

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        n = 0
        while n<1:
            n =  int(input("How many steps do you want to take?"))
        for i in range(n):
            self.next_turn()
        return None



