a = '''.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........'''
words = a.split('\n')
d = len(words[0])


class DataHolder:
    Counter = 0
    l = words

    def __init__(self):
        self.data = 'MAS'
        self.data2 = 'SAM'
        self.check = ''
        self.check2 = ''

    def anotherOne(self, letter, y, x):

        self.check += letter

        if self.check[len(self.check) - 1] != self.data[len(self.check) - 1]:
            self.check = ''
            if letter == 'M':
                self.check = 'M'

        if self.check == self.data:
            self.check = ''
            if words[y - 2][x] == 'M' and words[y][x + 2] == 'S':
                DataHolder.Counter += 1
            elif words[y - 2][x] == 'S' and words[y][x + 2] == 'M':
                DataHolder.Counter += 1

        self.check2 += letter

        if self.check2[len(self.check2) - 1] != self.data2[len(self.check2) - 1]:
            self.check2 = ''
            if letter == 'S':
                self.check2 = 'S'

        if self.check2 == self.data2:
            self.check2 = ''
            if words[y - 2][x] == 'M' and words[y][x + 2] == 'S':
                DataHolder.Counter += 1
            elif words[y - 2][x] == 'S' and words[y][x + 2] == 'M':
                DataHolder.Counter += 1


direction_6 = DataHolder()

for i in range(d):

    for j in range(2, d):

        direction_6.anotherOne('@', 0, 0)

        for k in range(d):
            if i > 1:
                break
            if k > j:
                break

            if i == 1:
                if j == d - 1:
                    break
                direction_6.anotherOne(words[-j + k - i][-k - i], -j + k - i, -k - i)

            else:
                direction_6.anotherOne(words[k][j - k], k, j - k)

print('----------------')
print(DataHolder.Counter)
print('----------------')
