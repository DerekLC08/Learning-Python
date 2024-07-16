def main():
    x = input("Greet someone: ")
    print(f"${value(x)}")


def value(greeting):
    gword = greeting.lower().split()
    if gword == "hello":
        return 0
    elif gword[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()