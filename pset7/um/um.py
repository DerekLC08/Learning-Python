import re
import sys


def main():
    if 1 < len(sys.argv) < 3:
        print(count(sys.argv[1]))
    else:
        print(count(input("Text: ")))


def count(s):
    uml = re.findall(r"(\W|\b)um(\W|\b)" ,s ,re.IGNORECASE)
    n = 0
    for _ in uml:
        n += 1

    return n

if __name__ == "__main__":
    main()