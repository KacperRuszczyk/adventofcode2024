a = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''




b = a.split('\n')
l = list(map(str.split, b))

print(l)
print(type(l[0]))

out = 0

for i in l:
    len1 = len(i)
    t = 0
    if int(i[0]) > int(i[1]) or int(i[len1-2]) > int(i[len1-1]): #desc
        for j in range(len1-1):
            if int(i[j]) - int(i[j+1]) > 3:
                t += 1
                if t < 1:
                    break
            elif int(i[j]) - int(i[j+1]) < 1:
                t += 1
                if t < 1:
                    break


    elif int(i[0]) < int(i[1]) or int(i[len1-2]) < int(i[len1-1]): #asc
        for j in range(len1-1):

            if int(i[j]) - int(i[j + 1]) < -3:
                t += 1
                if t < 1:
                    break
            elif int(i[j]) - int(i[j + 1]) > -1:
                t += 1
                if t < 1:
                    break


    else:
        t += 1

    if t < 1:
        out += 1
        print('asc', i)

print(out)
