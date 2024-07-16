camel = input("camelCase: ").strip()

for c in camel:
    if c.isupper() == True:
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()
