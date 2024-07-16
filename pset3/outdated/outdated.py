month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if 1 <= d <= 31 and 1 <= m <= 12 and 0 <= y:
            break
        else:
            pass

    except ValueError:
        try:
            md, y = date.split(",")
            m, d = md.split()
            m = int(month.index(m)) + 1
            d = int(d)
            y = int(y)
            if 1 <= d <= 31 and 0 <= y:
                break
            else:
                continue

        except KeyError:
            continue

        except ValueError:
            continue
if d <= 9:
    d = "0" + str(d)
if m <= 9:
    m = "0" + str(m)
print(y, m, d, sep ="-")
