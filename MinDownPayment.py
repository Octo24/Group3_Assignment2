# PART 1  
# Enter inputs for variables name, address and purchase price of home
name = input("Enter your name: ")
address = input("Enter your address: ")
purchasePrice = int(input("Enter the purchase price of the property to be mortgaged: ").replace(" ", ""))

# purchase price under 500000 
if purchasePrice < 500000:
    minimumDownPayment = 0.05 * purchasePrice

    print(f"Your minimum down payment is: ${minimumDownPayment}")


# purchase price between 500000 and 1000000
elif purchasePrice >= 500000 and purchasePrice <= 1000000:
    minimumDownPayment = ((500000 * 0.05) + ((purchasePrice - 500000) * 0.10))

    print(f"Your minimum down payment is: ${minimumDownPayment}")


# elif statement over 1000000
elif purchasePrice > 1000000:
    minimumDownPayment = purchasePrice * 0.20

    print(f"Your minimum down payment is: ${minimumDownPayment}")

minimumDownPaymentPercent = ((minimumDownPayment / purchasePrice) * 100)

# while true loop to check if down payment percent is above the down payment minimum
while True:
    downPaymentPercent = float(input(f'Enter down payment percentage (minimum {minimumDownPaymentPercent:.4}): '))/100
    if downPaymentPercent >= minimumDownPaymentPercent/100:
        break
    else:
        print("Please enter a value between the minimum and 100.")

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


# PART 1 stage 3
mortgageTermInterestRatesDict = {
    1: 0.0595, 
    2: 0.059, 
    3: 0.056, 
    5: 0.0529, 
    10: 0.06
    }


# list of valid mortgage term options
validMortgageTerm = [1, 2, 3, 5, 10]

# check if mortgage term input is in valid options list
while True:
    mortgageTerm = int(input("Enter mortgage term in years (options: 1, 2, 3, 5, 10): "))
    if mortgageTerm in validMortgageTerm:
        break
    else:
        print("Please enter a valid choice.")

# list of valid amortization period options
validAmortizationPeriod = [5, 10, 15, 20, 25]

# check if amortization input is in valid options list
while True:
    amortizationPeriod = int(input("Enter amortization period in years (options: 5, 10, 15, 20 ,25): "))
    if amortizationPeriod in validAmortizationPeriod: 
        break
    else:
        print("Please enter a valid choice.")


annualMortgageInterestRate = mortgageTermInterestRatesDict.get(mortgageTerm)

# Effective monthly rate (EMR) calculation
EMR = ((1 + annualMortgageInterestRate / 2) ** 2) ** (1/12) - 1
print(f"Effective monthly rate is {EMR:.2f}%")

# Number of monthly payments (n) 
n = amortizationPeriod * 12

# Monthly payments (m) calculations
monthlyPayments = principalAmount * (EMR * (1 + EMR) ** n) / ((1 + EMR) ** n - 1)
print(f"Your monthly payments over {amortizationPeriod} years is ${monthlyPayments:.2f}")