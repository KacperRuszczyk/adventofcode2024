data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''


lines = data.split('\n')
data_dict = {}
duplicate_dict = {}

for line in lines:
    key, values = line.split(':')
    key = int(key)
    values = list(map(int, values.split()))
    if key in data_dict:
        duplicate_dict[key] = values
    else:
        data_dict[key] = values


print("Main Dictionary:", data_dict)
print("Duplicate Dictionary:", duplicate_dict)

get_bin = lambda x, n: format(x, 'b').zfill(n)

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))

    return ''.join(reversed(nums))

def left_to_right_eval(expr):
    tokens = []
    temp = ""
    for char in expr:
        if char in '0123456789':
            temp += char
        elif char in '+*-:/|':
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(char)
        elif char == ' ':
            if temp:
                tokens.append(temp)
                temp = ""

    if temp:
        tokens.append(temp)
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if i + 1 >= len(tokens):
            break

        operator = tokens[i]
        number = int(tokens[i + 1])

        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        elif operator == '|':
            result = int(str(result) + str(number))
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    return result


def i_love_elf_math(data_dict):
    numbers = str(data_dict[key])[1:-1]
    how_much = numbers.count(',')

    if how_much == 0:
        g = data_dict[key][0]
        if int(key) == g:

            return int(key)

    for j in range(3 ** how_much):
        prop = ternary(j)[::-1]

        if len(prop) != how_much:
            dif = how_much - len(prop)
            for g in range(dif):
                prop += '0'

        numbers = str(data_dict[key])[1:-1]

        for k in prop:
            index = numbers.find(',')
            if index < 0:
                break

            if k == '1':
                numbers = numbers[:index] + '*' + numbers[index + 1:]
            elif k == '2':
                numbers = numbers[:index] + '|' + numbers[index + 1:]
            else:
                numbers = numbers[:index] + '+' + numbers[index + 1:]


        if left_to_right_eval(numbers) == int(key):

            return int(key)

    return 0


out = 0
for i, key in enumerate(data_dict):

    out += i_love_elf_math(data_dict)

for i, key in enumerate(duplicate_dict):

    out += i_love_elf_math(duplicate_dict)

print(out,'<--------')


