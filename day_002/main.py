
#! Day 2 - Tip Calculator
print("Welcome to tip calculator.")
initial_bill = float(input("What was the total bill - \n"))
percent_tip = float(input("What percentage tip would you like to give - \n"))
total_people = float(input("How many people to split the bill - \n"))
new_percent = 1 + percent_tip / 100

bill_per_person = (initial_bill / total_people) * new_percent
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay - {bill_per_person}")
