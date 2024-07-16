import validators

def main():
#prompt user for email and call the function validate
    print(validate(input("Email: ")))


def validate(e):
#check if email is valid and return valid or invalid
    if validators.email(e) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()