principle=int(input("Base capital "))
compoundingRate=float(input("Rate of compounding (ex. 1.3% would be entered as 1.013, 2% as 1.02, etc.) "))
periods=int(input("No. of compounding periods overall "))
addendum=int(input("Value of routine additional deposits "))
addendumFrequency=int(input("Number of periods per addendum interval "))
dividend=float(input("Dividend yield per distribution (ex. 2% would be entered as 1.02) "))
dividendFrequency=int(input("No. of periods per dividend interval "))
payments=(periods/addendumFrequency)
i=0
n=0
while i<payments:
    principle*=(compoundingRate**addendumFrequency)
    principle+=addendum
    i+=1
    while n<i*addendumFrequency//dividendFrequency:
        principle*=dividend
        n+=1
    print(i*addendumFrequency, n*addendumFrequency, principle)