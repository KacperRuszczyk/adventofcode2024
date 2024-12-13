class Lab:
    lab ='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    lab = lab.split('\n')
    width = len(lab) - 1
    height = len(lab[0]) - 1
    for i, k in enumerate(lab):
        lab[i] = list(lab[i])

    def __init__(self):

        self.alt_lab = self.deep_copy(Lab.lab)
        self.width = len(self.alt_lab) - 1
        self.height = len(self.alt_lab[0]) - 1


    def deep_copy(self, lst):
        if isinstance(lst, list):
            return [self.deep_copy(item) for item in lst]

        return lst

    def print_lab(self, message):
        for i, k in enumerate(self.alt_lab):
            self.alt_lab[i] = ''.join(k)
            print(self.alt_lab[i])
            self.alt_lab[i] = list(self.alt_lab[i])
        print(message)
        return

    def print_main_lab(message):
        for i, k in enumerate(Lab.lab):
            Lab.lab[i] = ''.join(k)
            print(Lab.lab[i])
            Lab.lab[i] = list(Lab.lab[i])
        print(message)
        return


class Guard:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.vector = 0
        self.update_direction()

    def update_direction(self):
        self.direction = [
            [self.y - 1, self.x],  # Up (y - 1)
            [self.y, self.x + 1],  # Right (x + 1)
            [self.y + 1, self.x],  # Down (y + 1)
            [self.y, self.x - 1]  # Left (x - 1)
        ]

    def start_pos(self, lab):

        for i, row in enumerate(lab):
            for j, tile in enumerate(row):
                if tile == '^':
                    self.y = i
                    self.x = j
                    self.update_direction()
                    return

    def get_pos(self):
        return [self.y , self.x]

    def y(self):
        return self.y

    def x(self):
        return self.x

    def step(self):
        self.y = self.direction[self.vector % 4][0]
        self.x = self.direction[self.vector % 4][1]
        self.update_direction()
        return

    def look_ahead(self, lab):
        return lab[self.direction[self.vector % 4][0]][self.direction[self.vector % 4][1]]

    def paint(self, lab):
        lab[self.get_pos()[0]][self.get_pos()[1]] = str(self.vector % 4)

    def place(self, lab):
        lab[self.direction[self.vector % 4][0]][self.direction[self.vector % 4][1]] = '@'

    def alt(self,y,x,vector):
        self.y = y
        self.x = x
        self.vector = vector
        self.update_direction()





class PuppetMaster:
    def __init__(self):
        self.guard = Guard()
        self.alt_guard = Guard()
        self.alt_lab = Lab()
        self.out = 0

    def move_thru_lab(self):
        self.guard.start_pos(Lab.lab)

        while Lab.height - 1 >= self.guard.y >= 1 and Lab.width - 1 >= self.guard.x >= 1:
            self.out += self.alt_univers()
            self.guard.paint(Lab.lab)
            # if self.guard.y <= Lab.height - 1 and self.guard.x <= Lab.width - 1 and self.guard.y >= 1 and self.guard.x >= 1:
            if Lab.height - 1 >= self.guard.y >= 1 and Lab.width - 1 >= self.guard.x >= 1:
                self.guard.paint(Lab.lab)
                while self.guard.look_ahead(Lab.lab) == '#' or self.guard.look_ahead(Lab.lab) == '@':
                    self.guard.vector += 1
                if Lab.height - 1 >= self.guard.y >= 1 and Lab.width - 1 >= self.guard.x >= 1:
                    self.guard.step()
            # Lab.print_main_lab('---main---')
        print(self.out,'-------out-------',self.out)
        self.guard.paint(Lab.lab)
        return

    def alt_univers(self):
        self.alt_guard.alt(self.guard.y,self.guard.x,self.guard.vector)
        self.alt_lab = Lab()
        while self.alt_guard.look_ahead(self.alt_lab.alt_lab) == '#' or self.alt_guard.look_ahead(
                self.alt_lab.alt_lab) == '@':
            self.alt_guard.vector += 1
        if self.alt_guard.look_ahead(self.alt_lab.alt_lab) == '.':
            self.alt_guard.place(self.alt_lab.alt_lab)

        while self.alt_lab.height - 1 >= self.alt_guard.y >= 1 and self.alt_lab.width - 1>= self.alt_guard.x >= 1:
            if self.alt_lab.alt_lab[self.alt_guard.y][self.alt_guard.x] == str(self.alt_guard.vector % 4):

                return 1
            self.alt_guard.paint(self.alt_lab.alt_lab)


            if self.alt_lab.height - 1 >= self.alt_guard.y >= 1 and self.alt_lab.width - 1 >= self.alt_guard.x >= 1:
                while self.alt_guard.look_ahead(self.alt_lab.alt_lab) == '#' or self.alt_guard.look_ahead(self.alt_lab.alt_lab) == '@':
                    self.alt_guard.vector += 1
                    if self.alt_guard.vector > 10000:
                        # self.alt_lab.print_lab('---?!?!?!?---')
                        return 1
                self.alt_guard.step()
        # self.alt_lab.print_lab('=================================')
        return 0

master = PuppetMaster()
master.move_thru_lab()
master.alt_lab.print_lab('#####################################################')
master.alt_lab.print_main_lab()
# Lab.print_main_lab(Lab.lab)
