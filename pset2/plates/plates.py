def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#Check length
    if len(s) < 2 or len(s) > 6:
        return False

#Check alphanumeric(No symbols)
    if s.isalnum() == False:
        return False

#Check number of letters
    i = 0 #letters
    n = 0 #numbers
    for c in s:

        #check if char is a number
        if c.isnumeric() == False:
            if n > 0:
                return False
            else:
                i += 1
        else:
            #check if first numbered char is 0
            if n == 0 and c == "0":
                return False
            else:
                n += 1

#check if starts with 2 letters
    if i < 2:
        return False

    return True


main()