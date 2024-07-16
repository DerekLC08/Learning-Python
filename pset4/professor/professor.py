import random


def main():
    l = get_level()

    score = 0

    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        t = x + y

        tries = 0
        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries += 1
                continue

            if answer == t:
                score += 1
                break
            else:
                print("EEE")
                tries += 1
        if tries == 3:
            print(t)

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if 1 <= level <= 3:
            return level
        else:
            continue


def generate_integer(level):
    if level == 1:
        i = random.randint(0, 9)
        return i
    elif level == 2:
        i = random.randint(10, 99)
        return i
    else:
        i = random.randint(100, 999)
        return i


if __name__ == "__main__":
    main()