a ='''3   4
4   3
2   5
1   3
3   9
3   3'''

b = a.split('\n')
l = list(map(str.split, b))
print(type(l[0]))
print(l[0][0])

out = 0
l1 = []
l2 = []

for j in l:
    l1.append(int(j[0]))
    l2.append(int(j[1]))


l11 = sorted(l1)
l22 = sorted(l2)

print(l11)
print(l22)

for i in range(len(l11)):
    if l11[i] > l22[i]:
        out += l11[i] - l22[i]
    else:
        out += l22[i] - l11[i]

print(out)
