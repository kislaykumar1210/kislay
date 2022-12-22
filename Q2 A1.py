GrossIncome = int(input("Enter Your Gross Income  "))
Dependents = int( input("Enter the number of Dependemts-  "))

Tax_1 = GrossIncome-10000-(Dependents*3000)
Final_Tax = Tax_1*0.2

print("Your tax is $ ",Final_Tax)
