import re
import sys


def main():
    if 1 < len(sys.argv) < 3:
        print(parse(sys.argv[1]))
    else:
        print(parse(input("HTML: ")))


def parse(s):

    if code := re.search(r".*src=\"https?\://(?:www\.)?youtube\.com/.+/(\w+)\"" , s):
        short = "https://youtu.be/" + code.group(1)
        return short
    else:
        return None


if __name__ == "__main__":
    main()