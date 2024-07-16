# a e i o u
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
txt = input("Input: ")
for l in range(len(vowels)):
    txt = txt.replace(vowels[l], "")
print(txt)
