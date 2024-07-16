from random import randint
n = 0
while n < 1:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue

x = randint(1, n)

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        continue

    if g == x:
        print("Just right!")
        break
    elif g < x:
        print("Too small!")
    else:
        print("Too large!")
