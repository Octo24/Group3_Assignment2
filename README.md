# Group3_Assignment2

#### Part 1

1. Minimum Down Payment Component

User inputs Purchasing Price and gets Minimum DownPayment percentage

	1. inputs Purchasing Price(P)
	2. Using table 1 values (P) returns a Minimum DownPayment(mdp)
		Calculations to determine (mdp) as a percentage

		2a.(mdp)$ = (P)$ x (md)% 
		2b.(mDp)% = (mdp)$ / (P)$ * 100 


2. Mortage Default Insurance Component

User inputs Downpayment Percentage(dpp) and gets returned a Mortgage Insurance Premium(mip) based off table 2 values
	Calculations for (dp), (ic), and (pa) ensue
	
	1. DownPayment amount(dp)$ = (P)$ * (dpp)as int / 100
	2. Insurance Cost(ic) = [(P)$ - (dp)$] * (mip)% / 100 
	3. Principal Amount(pa) = (P)$ - (dp)$ + (ic)$


3. Mortage Payment Component

Final two user inputs: user inputs Mortgage Term in years(mt) and gets returned Mortgage Interest Rate(mir), then user inputs Amortization Period in years(ap) - the user inputs refer to table 3 and 4 respectively.

	1. 	EMR = ((1 + A/2)2)1/12 - 1
		Where:
			(A) is the Annual mortgage interest rate (as per table 3 above)
			(EMR) is the Effective Monthly Rate

	2.	(M) = P[EMR(1+EMR)^n]/[(1+EMR)^n-1]
		Where:
			(M) is the Monthly payment 
			(P) is the Principal amount
			(EMR) is the Effective Monthly Rate as previously calculated 
			(n) is the number of monthly payments (years * 12)


#### Part 2