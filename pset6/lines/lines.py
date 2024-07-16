import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

ext = sys.argv[1].split(".")
if ext[1] != "py":
    print("Not a python file")
    sys.exit(1)

n = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            l = line.rstrip().strip()
            if l == "" or l[0] == "#":
                pass
            else:
                n += 1

except FileNotFoundError:
    print("File does not exist")
    sys.exit()

print(n)