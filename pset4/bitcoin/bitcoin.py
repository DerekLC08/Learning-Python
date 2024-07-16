import requests
import sys
import json

if sys.argv[1] == None:
    print("Missing command-line argument")
    sys.exit()

try:
    n = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin_dict = response.json()
bitcoin_price = float(bitcoin_dict["bpi"]["USD"]["rate_float"])

total = n * bitcoin_price
print(f"${total:,.4f}")