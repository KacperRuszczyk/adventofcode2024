a = '''....S
...A.
..M..
.X...
.....'''


class DataHolder:
    Counter = 0

    def __init__(self):
        self.data = 'XMAS'
        self.check = ''

    def anotherOne(self, letter):
        self.check += letter
        print(self.check)

        if self.check[len(self.check) - 1] != self.data[len(self.check) - 1]:
            self.check = ''
            if letter == 'X':
                self.check = 'X'

            # print('damp')
        if self.check == self.data:
            self.check = ''
            DataHolder.Counter += 1
            # print('pass', DataHolder.Counter)


words = a.split('\n')
d = len(words[0])
direction_1 = DataHolder()
direction_2 = DataHolder()
direction_3 = DataHolder()
direction_4 = DataHolder()
direction_5 = DataHolder()
direction_6 = DataHolder()
direction_7 = DataHolder()
direction_8 = DataHolder()

for i in range(d):
    direction_1.anotherOne('@')
    direction_2.anotherOne('@')
    direction_3.anotherOne('@')
    direction_4.anotherOne('@')
    for j in range(d):
        direction_1.anotherOne(words[i][j])
        direction_2.anotherOne(words[i][-j-1])
        direction_3.anotherOne(words[j][i])
        direction_4.anotherOne(words[-j - 1][i])
        direction_5.anotherOne('@')
        direction_6.anotherOne('@')
        direction_7.anotherOne('@')
        direction_8.anotherOne('@')
        for k in range(d):
            if i > 1:
                break
            if k > j:
                break

            if i == 1:
                if j == d - 1:
                    break
                # print('2. ', 'i:', i, '| j:', j, '| k:', k, '||', 'y:', -j + k -1 , ' x:', k, words[-j + k - 1][k])
                direction_5.anotherOne(words[-k - i][-j + k - i])
                direction_6.anotherOne(words[-j + k - i][-k - i])
                direction_7.anotherOne(words[j - k][-k - 1])
                direction_8.anotherOne(words[-j + k - 1][k])
            else:
                # print('1. ', 'i:', i, '| j:', j, '| k:', k, '||', 'y:',k, ' x:',-j - 1 + k, words[k][-j - 1 + k])
                direction_5.anotherOne(words[j - k][k])
                direction_6.anotherOne(words[k][j - k])
                direction_7.anotherOne(words[-k - 1][j - k])
                direction_8.anotherOne(words[k][-j - 1 + k])


print('----------------')
print(DataHolder.Counter)
print('----------------')
