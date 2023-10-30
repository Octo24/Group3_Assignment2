# Enter inputs for variables name, address and purchase price of home
name = input("Enter your name: ")
address = input("Enter your address: ")
purchasePrice = int(input("Enter the purchase price of the property to be mortgaged: "))

# purchase price under 500000 
if purchasePrice < 500000:
    minimumDownpayment = 0.05 * purchasePrice
    print(minimumDownpayment)

# purchase price between 500000 and 1000000
elif purchasePrice >= 500000 and purchasePrice <= 1000000:
    minimumDownpayment = ((500000 * 0.05) + ((purchasePrice - 500000) * 0.10))
    print(minimumDownpayment)

# elif statement over 1000000
elif purchasePrice > 1000000:
    minimumDownPayment = purchasePrice * 0.20
    print(minimumDownPayment)

