x = input("Greet someone: ")
y = x.lower().split()

if y[0] == "hello":
    print("$0")
elif y[0] == "hey":
    print("$20")
else:
    print("$100")