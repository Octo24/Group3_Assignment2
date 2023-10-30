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
