import re
import sys


def main():
    if 1 < len(sys.argv) < 3:
        print(validate(sys.argv[1]))
    else:
        print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(([2]([5][0-5]|[0-4][0-9])|[1]?[0-9]?[0-9])\.){3}([2]([5][0-5]|[0-4][0-9])|[1]?[0-9]?[0-9]$)", ip)
    if matches:
        return True
    else:
        return False

if __name__ == "__main__":
    main()