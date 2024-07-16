def main():
    phrase = input("please enter a phrase: ")
    print(convert(phrase))

def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

main()