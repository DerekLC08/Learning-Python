import sys
import csv

#Check if the correct amount of command-line arguments has been entered
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

#Creates the dictionary of students
students = []

#Exception handling, if file is entered is wrong, the program will exit
try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first" : first.lstrip(), "last" : last, "house": row["house"]})

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

#Writing new csv file
with open(sys.argv[2], "w", newline="") as csvfile:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in students:
        writer.writerow({"first" : row["first"],"last": row["last"], "house": row["house"]})