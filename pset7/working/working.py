import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #Breaking down the string
    if matches := re.search(r"^(1[0-2]|\d)(:[0-5]\d)? (AM|PM) to (1[0-2]|\d)(:[0-5]\d)? (AM|PM)$" , s, re.IGNORECASE):
        hs = matches.group(1)
        ms = matches.group(2)
        fs = matches.group(3)
        he = matches.group(4)
        me = matches.group(5)
        fe = matches.group(6)
    else:
        #Raising value error if the format is wrongly input
        raise ValueError

    if fs == "PM":
        hs = int(hs) + 12
        if hs > 24:
            hs = hs - 24
        elif hs == 24:
            hs = "12"
    else:
        if int(hs) == 12:
            hs = "0"

    if int(hs) < 10:
        hs = f"0{hs}"

    if fe == "PM":
        he = int(he) + 12
        if he > 24:
            he = he - 24
        elif he == 24:
            he = "12"
    else:
        if int(he) == 12:
            he = "0"

    if int(he) < 10:
        he = f"0{he}"

    if ms == None:
        ms = ":00"

    if me == None:
        me = ":00"

    time = f"{hs}{ms} to {he}{me}"
    return time


if __name__ == "__main__":
    main()