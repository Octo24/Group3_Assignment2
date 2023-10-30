name = input("Enter your name: ")
address = input("Enter your address: ")
purchPrice = int(input("Enter the purchase price of the property to be mortgaged: "))

if purchPrice < 500000:
    downPaymentLow = 0.05 * purchPrice
    print(downPaymentLow)

elif 500000 <= purchPrice <= 1000000:
    downPaymentFirst = 500000 * 0.10
    downPaymentSecond = (purchPrice - 500000) * 0.05
    downPaymentMid = downPaymentFirst + downPaymentSecond
    print(downPaymentMid)

elif purchPrice > 1000000:
    downPaymentHigh = purchPrice * 0.20
    print(downPaymentHigh)

