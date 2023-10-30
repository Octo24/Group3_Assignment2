# Enter inputs for variables name, address and purchase price of home
name = input("Enter your name: ")
address = input("Enter your address: ")
purchPrice = int(input("Enter the purchase price of the property to be mortgaged: "))

# purchase price under 500000 
if purchPrice < 500000:
    downPaymentLow = 0.05 * purchPrice
    print(downPaymentLow)

# purchase price between 500000 and 1000000
elif 500000 <= purchPrice <= 1000000:
    # first part of calculation for value = 500000
    downPaymentFirst = 500000 * 0.10
    # second part of calculation for value > 500000
    downPaymentSecond = (purchPrice - 500000) * 0.05
    downPaymentMid = downPaymentFirst + downPaymentSecond
    print(downPaymentMid)

# elif statement over 1000000
elif purchPrice > 1000000:
    downPaymentHigh = purchPrice * 0.20
    print(downPaymentHigh)

