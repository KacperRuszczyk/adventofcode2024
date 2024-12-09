a = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''

b = '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

rules = a.split('\n')
pages = b.split('\n')
pages = [page.split(',') for page in pages]
before = {}  # Key | Before
after = {}  # After | Key
for rule in rules:
    key, value = rule.split('|')
    if key not in before:
        before[key] = []
    before[key].append(value)

for i in before:
    if i not in after:
        after[i] = []
    for j in before:
        if i in before[j]:
            after[i].append(j)


def after_check(arr):
    n = len(arr)
    if n <= 1:
        return True
    for i, key in enumerate(arr):
        j = i - 1
        while j >= 0:
            if arr[j] in after.keys():
                if key in after[arr[j]]:
                    return False
                else:
                    j -= 1
            else:
                j -= 1
    return True


def after_insert(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i, key in enumerate(arr):
        j = i - 1
        if key not in after.keys():
            after[key] = ['idk']
        while j >= 0 and key in after[arr[j]]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


def before_check(arr):
    n = len(arr)
    if n <= 1:
        return True
    for i, key in enumerate(arr):
        n = len(arr) - 1
        j = i + 1
        while j <= n:
            if arr[j] in before.keys():
                if key in before[arr[j]]:
                    return False
                else:
                    j += 1
            else:
                j += 1
    return True


def before_insert(arr):
    n = len(arr) - 1
    if n <= 1:
        return arr
    for i, key in enumerate(arr):
        j = i + 1
        if j <= n:
            if arr[j] not in before.keys():
                before[arr[j]] = ['idk']
        while j <= n and key in before[arr[j]]:
            arr[j - 1] = arr[j]
            j += 1

        arr[j - 1] = key
    return arr


after_pages = []
for page in pages:
    if not after_check(page):
        after_pages.append(page)
# print(after_pages)
before_pages = []
for page in pages:
    if not before_check(page):
        before_pages.append(page)

for page in before_pages:
    if page not in after_pages:
        after_pages.append(page)

for page in after_pages:
    after_insert(page)
    before_insert(page)


out = 0
print(after_pages)
for page in after_pages:
    n = len(page) // 2
    print(page[n])
    out += int(page[n])

print(out)