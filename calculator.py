print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the biill? "))
x = total_bill * (percentage / 100) 
y = x + total_bill
final = round(y / people, 2)
final = "{:.2f}".format(final)
print(f"Each person should pay ${final}")
