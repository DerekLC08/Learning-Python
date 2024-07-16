import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

if len(sys.argv) == 1:
    phrase = input("Input: ")
    f = choice(figlet.getFonts())
    figlet.setFont(font = f)

else:
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = sys.argv[2]
            try:
                figlet.setFont(font = f)

            except KeyError:
                print("Invalid Usage")
                sys.exit()

        else:
            print(figlet.renderText(phrase))

        phrase = input("Input: ")
print(figlet.renderText(phrase))