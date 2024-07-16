grocery = {}

while True:
    n = 0
    try:
        item = input().upper()
    except EOFError:
        break

    if item in grocery:
        n = grocery[item] + 1
        grocery[item] = n
    else:
        grocery[item] = 1

sorted_grocery = dict(sorted(grocery.items()))
for i in sorted_grocery:
    print(grocery[i], i)
