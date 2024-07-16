def main():
    fraction = input("Fraction: ")
    p = convert(fraction)

    print(gauge(p))


def convert(fraction):
    x, y = fraction.split("/")

    try:
        return (int(x)/int(y)) * 100
    except (ValueError,ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()