# Enter inputs for variables name, address and purchase price of home
name = input("Enter your name: ")
address = input("Enter your address: ")
purchasePrice = int(input("Enter the purchase price of the property to be mortgaged: "))

# purchase price under 500000 
if purchasePrice < 500000:
    minimumDownPayment = 0.05 * purchasePrice
    print(minimumDownPayment)

# purchase price between 500000 and 1000000
elif purchasePrice >= 500000 and purchasePrice <= 1000000:
    minimumDownPayment = ((500000 * 0.05) + ((purchasePrice - 500000) * 0.10))
    print(minimumDownPayment)

# elif statement over 1000000
elif purchasePrice > 1000000:
    minimumDownPayment = purchasePrice * 0.20
    print(minimumDownPayment)

minimumDownPaymentPercent = ((minimumDownPayment / purchasePrice) * 100)

downPaymentPercent = float(input(f'Enter down payment percentage (minimum {minimumDownPaymentPercent:.4}): '))/100

# PART 1 stage 2
if downPaymentPercent >= 0.05 and downPaymentPercent < 0.10:
    mortgage = 0.04
elif downPaymentPercent >= 0.10 and downPaymentPercent < 0.15:
    mortgage = 0.031
elif downPaymentPercent >= 0.15 and downPaymentPercent < 0.20:
    mortgage = 0.028
elif downPaymentPercent >= 0.20:
    mortgage = 0


downPayment = (purchasePrice * downPaymentPercent)
insuranceCost = (((purchasePrice - downPayment) * mortgage))
principalAmount = (purchasePrice - downPayment + insuranceCost)

print(f'Down payment amount is ${downPayment:.0f}')
print(f'Mortgage insurance price is ${insuranceCost:.0f}')
print(f'Total mortgage amount is ${principalAmount:.0f}')