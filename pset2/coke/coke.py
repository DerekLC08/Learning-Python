ad = 50

while ad > 0:
    print("Amount Due: "+ str(ad))
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        ad = ad - coin
    else:
        continue
co = abs(ad)
print("Change Owed: "+ str(co))