import sys
from PIL import Image, ImageOps

#Check if the correct amount of command-line arguments has been entered
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

#Check if input and output has the correct image format and are the same
try:
    fi = sys.argv[1].split(".")

except FileNotFoundError:
     sys.exit("File does not exist")

fo = sys.argv[2].split(".")

if fi[1] == "jpg" or fi[1] == "jpeg" or fi[1] == "png":
    pass
else:
    sys.exit("Invalid extension")
if fi[1] != fo[1]:
    sys.exit("Incompatible extension")

try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

#Opens shirt image
shirt = Image.open("shirt.png")
#Gets the size of the shirt
size = shirt.size
#Resize muppet to fit the shirt
muppet = ImageOps.fit(image, size)
#Paste shirt on muppet
muppet.paste(shirt, shirt)
#Save the image
muppet.save(sys.argv[2])