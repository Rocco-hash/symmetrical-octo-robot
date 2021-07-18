import math
principle = int(input("Base capital "))
compoundingRate = float(input("Rate of compounding (ex. 1.3% would be entered as 1.013, 2% as 1.02, etc. "))
periods = int(input("No. of compounding periods overall "))
addendum = int(input("Value of routine additional deposits "))
addendumFrequency = int(input("Number of periods per addendum interval "))
payments = (periods / addendumFrequency)

i = 0

while i < payments:
    principle *= (compoundingRate ** addendumFrequency)
    principle += addendum
    i += 1
    print(i, principle)
