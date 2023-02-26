
# #! Rollercoaster ride
# height = int(input("Enter your height - "))

# if height > 120:
#     # Can ride
#     age = int(input("Enter your age - "))
#     wantPhotos = input("Do you want photos [Y/N] - ").lower()
#     bill = 0

#     if (wantPhotos == 'y' or wantPhotos == 'yes'):
#         bill += 3

#     if (age < 12):
#         bill += 5
#         print(f"You can ride, your total cost will be - ${bill}")

#     elif (age <= 18):
#         bill += 7
#         print(f"You can ride, your total cost will be - ${bill}")

#     # Mid-life crisis
#     elif (age >= 45  and age <= 55):
#         print(f"You can ride, your total cost will be - ${bill}")

#     else:
#         bill += 12
#         print(f"You can ride, your total cost will be - ${bill}")

# else:
#     print("Can't ride")

# #! Odd or even
# num = int(input("Enter any number - "))
# if (num % 2 == 0):
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

# #! Leap year checker
# year = int(input("Which year you want to check - "))
# isLeap = False
# if (year % 4 == 0):
#     if (year % 100 == 0):
#         if (year % 400 == 0):
#             isLeap = True
#     else:
#         isLeap = True
# if (isLeap):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is NOT a leap year")

# #! Pizza order practice
# size = input("What size pizza do you want? S,M or L - ").lower()
# addPepperoni = input("Do you want pepperoni? Y or N - ").lower()
# extraCheese = input("Do you want extra cheese? Y or N - ").lower()
# bill = 0

# if (size == 's'):
#     bill += 15
#     if (addPepperoni == 'y'):
#         bill += 2
# elif (size == 'm'):
#     bill += 20
#     if (addPepperoni == 'y'):
#         bill += 3
# elif (size == 'l'):
#     bill += 25
#     if (addPepperoni == 'y'):
#         bill += 3

# if (extraCheese == 'y'):
#     bill += 1

# print(f"Thank you for ordering. Your final bill is - ${bill}")

#! Love calculator

name1 = input("What is your name - ").lower()
name2 = input("What is their's name - ").lower()
concatenated_name = name1 + name2

t_count = concatenated_name.count('t')
r_count = concatenated_name.count('r')
u_count = concatenated_name.count('u')
e_count = concatenated_name.count('e')
l_count = concatenated_name.count('l')
o_count = concatenated_name.count('o')
v_count = concatenated_name.count('v')
e_count = concatenated_name.count('e')

true_total = str(t_count + r_count + u_count + e_count)
love_total = str(l_count + o_count + v_count + e_count)
score = int(true_total + love_total)

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (40 < score < 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")