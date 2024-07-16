while True:
    try:
        n, d = (input("Fraction: ").split("/"))
        x = int(n)
        y = int(d)
        p = 100 * x / y

    except ValueError:
        continue
    except ZeroDivisionError:
        continue

    if x < 0 or y < 0 or x > y:
        continue
    else:
        break

if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p:.0f}%")
