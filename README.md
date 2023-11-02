# Group3_Assignment2

#### Part 1

0. Introduction
Asks for 3 user inputs: a name, address, and Purchasing price(P).

1. Minimum Down Payment Component

User inputs Purchasing Price and recieves the Minimum DownPayment as a dollar amount(mdp) and as a percentage(mDp)

	1. inputs Purchasing Price(P)
	2. Using table 1 values (P) returns a Minimum DownPayment(mdp)
		Calculations to determine (mdp) as a percentage

		2a.(mdp)$ = (P)$ x (md)% 
		2b.(mDp)% = (mdp)$ / (P)$ * 100 
	

2. Mortage Default Insurance Component

User inputs a Downpayment Percentage(dpp) **larger** than their Minimum DownPayment percentag  and gets returned a Mortgage Insurance Premium(mip) based off table 2 values

**-If (dpp)% is smaller than (mdp)%** return invalid input and prompt user for an appropriate value range.

**-If (dpp)%

	Calculations for (dp), (ic), and (pa) ensue:
	
	1. DownPayment amount(dp)$ = (P)$ * (dpp) / 100
	2. Insurance Cost(ic) = [(P)$ - (dp)$] * (mip)% / 100 
	3. Principal Amount(pa) = (P)$ - (dp)$ + (ic)$


3. Mortage Payment Component

Final two user inputs: user inputs Mortgage Term in years(mt) and gets returned an Annual Mortgage Interest Rate(A), then user inputs Amortization Period in years(ap) - the user inputs refer to table 3 and 4 respectively.

-**If (mt) and (ap) inputs are NOT from the table** return invalid input and prompt the user for an appropriate value

The program uses the value (A) to return the Effective Monthly Rate(EMR)

	1. 	(EMR)% = ((1 + A/2)^2)^1/12 - 1
		Where:
			(A) is the Annual mortgage interest rate (refer to table 3)
			(EMR) is the Effective Monthly Rate

Then the program uses both (A) and (EMR) values to calculate the Monthly payments(M)

	2.	(M)% = P[EMR(1+EMR)^n]/[(1+EMR)^n-1]
		Where:
			(n) is the number of monthly payments (ap * 12)


#### Part 2

1. Prompts user to input "Yes/No" (Y/N) for whether they want to see the amortization schedule/table or not.

2. If they pick (Y) they will see a CSV table outlining their mortgage stats organized in columns as month, Opening balance(OB) at the start of the month, Monthly payments(M), Monthly principle(MP), Monthly interest(MI), and Closing balance(CB) at the end of the month. 

	(OB)$ = (P)$
	(MI)$ = (OB)$ * (EMR)%
	(MP)$ = (M)$ - (MI)$
	(CB)$ = (OB) - (MP)



