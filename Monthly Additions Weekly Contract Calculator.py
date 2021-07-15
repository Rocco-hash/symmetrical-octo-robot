Principle=int(input("Base capital"))
Compounding_Rate=float(input("Rate of compounding (ex. 1.3% would be entered as 1.013, 2% as 1.02, etc."))
Periods=int(input("No. of compounding periods overall"))
Addendum=int(input("Value of routine additional deposits"))
Addendum_Frequency=int(input("Number of periods per addendum interval"))
Payments=(Periods/Addendum_Frequency)-1
Subtotal=Addendum*Compounding_Rate**a
def Subtotal(, Payments):
    result=0
    while a<Periods:
        a+=Addendum_Frequency
        Payments-=1
    return result
#(Principle*Compounding_Rate**Periods)