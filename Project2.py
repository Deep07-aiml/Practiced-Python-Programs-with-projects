# TIP CALCULATOR
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to split the bill? 10,12, or 15? "))
new_bill = (bill * (tip/100))
new_totalBill = bill + new_bill
split = float(input("How many people to split the bill? "))
split_bill = round(new_totalBill / split ,2)
print(f"Each person should pay: ${split_bill}")