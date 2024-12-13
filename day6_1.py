a = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

lab = a.split('\n')
for i,k in enumerate(lab):
    lab[i] = list(lab[i])


def find_guard(lab):
    for i, row in enumerate(lab):
        for j, tile in enumerate(row):
            if tile == '^':
                return ([i, j])


def move_guard(position, lab):
    out= 0
    position = position
    vector = 0
    y = position[0]
    x = position[1]
    width = len(lab) - 1
    height = len(lab[0]) - 1

    while y <= height and x <= width and y >= 0 and x >= 0:
        lab[y][x] = 'X'

        if y <= height - 1 and x <= width - 1 and y >= 1 and x >= 1:
            if vector % 4 == 0:
                look = y - 1
            elif vector % 4 == 1:
                look = x + 1
            elif vector % 4 == 2:
                look = y + 1
            else:
                look = x - 1
            if vector % 2 == 0:
                if lab[look][x] == '#':
                    vector += 1
            else:
                if lab[y][look] == '#':
                    vector += 1

        if vector % 4 == 0:
            y -= 1
        elif vector % 4 == 1:
            x += 1
        elif vector % 4 == 2:
            y += 1
        else:
            x -= 1






    for i, k in enumerate(lab):
        out += k.count('X')
        lab[i] = ''.join(k)
    for i in lab:
        print(i)

    return out


print(move_guard(find_guard(lab), lab))

