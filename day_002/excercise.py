'''
initial_num = input("Enter a number - ")
first_digit = int(initial_num[0])
second_digit = int(initial_num[1])
final_sum = first_digit + second_digit
print(final_sum)
'''

age = int(input("What is your current age - \n"))
years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"Years left - {str(years_left)}")
print(f"Months left - {str(months_left)}")
print(f"Weeks left - {str(weeks_left)}")
print(f"Days left - {str(days_left)}")