import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

ext = sys.argv[1].split(".")
if ext[1] != "csv":
    print("Not a CSV file")
    sys.exit(1)

table = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

print(tabulate(table, headers="keys", tablefmt="grid"))