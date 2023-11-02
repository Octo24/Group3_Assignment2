# PART 1  
# Enter inputs for variables name, address and purchase price of home
name = input("Enter client name: ")
address = input("Enter address of property: ")
purchasePrice = int(input("Enter purchase price: ").replace(" ", ""))

# purchase price under 500000 
if purchasePrice < 500000:
    minimumDownPayment = 0.05 * purchasePrice

# purchase price between 500000 and 1000000
elif purchasePrice >= 500000 and purchasePrice <= 1000000:
    minimumDownPayment = ((500000 * 0.05) + ((purchasePrice - 500000) * 0.10))
    
# elif statement over 1000000
elif purchasePrice > 1000000:
    minimumDownPayment = purchasePrice * 0.20
minimumDownPaymentPercent = ((minimumDownPayment / purchasePrice) * 100)

# while true loop to check if down payment percent is above the down payment minimum
while True:
    downPaymentPercent = float(input(f'Enter down payment percentage (minimum {minimumDownPaymentPercent:.4}): '))/100
    if downPaymentPercent >= minimumDownPaymentPercent/100 and downPaymentPercent <= 1.0:
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
effectiveMonthlyRate = ((1 + annualMortgageInterestRate / 2) ** 2) ** (1/12) - 1
intrestRate = (annualMortgageInterestRate*100)
print(f'Interest rate for the term will be {intrestRate:.2f}%')

# Number of monthly payments (n) 
n = amortizationPeriod * 12


# Monthly payments (m) calculations
monthlyPayments = round(principalAmount * (effectiveMonthlyRate * (1 + effectiveMonthlyRate) ** n) / ((1 + effectiveMonthlyRate) ** n - 1),2)
print(f"Monthly payment amount is: ${monthlyPayments:.0f}")

# Part 2 begins for the table here

table = input("Would you like to see the amortization schedule? (Y/N): " ).upper()


# Opening balance
openingBalance = (principalAmount)

# Monthly Interest amount
monthlyInterest = round((openingBalance * effectiveMonthlyRate),2)

# Monthly Payments
monthly = round((monthlyPayments),2)

# Monthly priciple
monthlyPrinciple = round((monthly - monthlyInterest),2)

# Closing Balance
closingBalance = round((openingBalance - monthlyPrinciple),2)

# Years to months
yearsToMonths = (mortgageTerm*12)


if table.upper() == ('Y'):
    # Creates a csv file to read data from and create a table to print
    import csv
    with open('amortization_schedule.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Month", "Opening Bal.", "Payments", "Principal", "Interest", "Closing Bal."])
        for month in range(1, yearsToMonths+1):
            writer.writerow([month, openingBalance, monthlyPayments, monthlyPrinciple, monthlyInterest, closingBalance])

            # Calculations for each month in a loop
            closingBalance = round((openingBalance - monthlyPrinciple*2),2)
            openingBalance = round((openingBalance - monthlyPrinciple),2) 
            monthlyPrinciple = round(monthlyPrinciple + (monthlyPrinciple*(effectiveMonthlyRate*mortgageTerm)),2)
            monthlyInterest = round((openingBalance*effectiveMonthlyRate),2)
            
    # Formats each row into a table that is readable
    with open('amortization_schedule.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*row))

    totalMonthlyPrinciple = 0
    with open('amortization_schedule.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            totalMonthlyPrinciple += float(row[3])

    totalMonthlyIncome = 0
    with open('amortization_schedule.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            totalMonthlyIncome += float(row[4])
    
    print("==========================================================================================================")
    print("{:<52} {:<20} {:<10}".format(f'Total ',totalMonthlyPrinciple, totalMonthlyIncome))

elif table.upper() == ('N'):
    print("Goodbye")