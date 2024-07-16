import sys
import re
import inflect

p = inflect.engine()
from datetime import date
from datetime import timedelta

def main():

    dob = check(input("Date of Birth: "))
    year, month, day = dob.split("-")
    try:
        dobtd = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    tdr = date.today() - dobtd
    print(convert(tdr))


def check(s):
    if re.search(r"\d{4}-\d{2}-\d{2}", s):
        return s
    else:
        sys.exit("Invalid date")

def convert(t):
    minutes = round(timedelta.total_seconds(t) / 60)
    return (p.number_to_words(minutes)).replace("and ", "").capitalize() + " minutes"


if __name__ == "__main__":
    main()