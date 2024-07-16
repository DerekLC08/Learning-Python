def main():
    t = input("What is the time?: ")
    val = convert(t)
    if 7 <= val <= 8:
        print("breakfast time")
    elif 12 <= val <= 13:
        print("lunch time")
    elif 18 <= val <= 19:
        print("dinner time")


def convert(time):
    if " a.m." in time:
        time = time.strip(" a.m.")
        h, m = (time.split(":", 1))
        hours = float(h) + (float(m)/60)
        return hours

    elif " p.m." in time:
        time = time.strip(" p.m.")
        h, m = (time.split(":", 1))
        hours = float(h) + (float(m)/60) + 12
        return hours

    else :
         h, m = (time.split(":", 1))
    hours = float(h) + (float(m)/60)
    return hours

if __name__ == "__main__":
    main()