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


def left_to_right_eval(expr):
    tokens = []
    temp = ""
    for char in expr:
        if char in '0123456789':
            temp += char
        elif char in '+*-:/':
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
        operator = tokens[i]
        number = int(tokens[i + 1])

        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
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
    for j in range(2 ** how_much):
        prop = get_bin(j, how_much)[::-1]
        numbers = str(data_dict[key])[1:-1]
        for k in prop:
            index = numbers.find(',')
            if k == '1':
                numbers = numbers[:index] + '*' + numbers[index + 1:]

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

print(out)


