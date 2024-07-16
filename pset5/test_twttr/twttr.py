def main():
    txt = input("Input: ")
    short = shorten(txt)
    print(short)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for l in range(len(vowels)):
        word = word.replace(vowels[l], "")
    return word


if __name__ == "__main__":
    main()