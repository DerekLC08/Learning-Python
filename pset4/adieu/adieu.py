import inflect
p = inflect.engine()
names = []
while True:
    try:
         name = input("Name: ")
         names.append(name)
    except EOFError:
         print()
         break

bid = "Adieu, adieu, to"
adieulist = p.join(names)
print(bid , adieulist)
