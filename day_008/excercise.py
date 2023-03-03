import math
# # Defining a function (without argument)
# def function_name():
#     print("Inside function (without argument)\n")


# # Calling the function
# print("Calling function (without argument)")
# function_name()

# # Defining a function (with argument)
# def function_name(para1, para2):
#     print(f"Parameter 1 - {para1}")
#     print(f"Parameter 2 - {para2}\n")


# print("Calling function (with argument)")
# function_name(10, 20)

# # Defining a function (with position of the arguments being changed)
# def function_name(para2, para1):
#     print(f"Parameter 1 - {para1}")
#     print(f"Parameter 2 - {para2}")


# print("Calling function (with position of the arguments being changed)")
# function_name(para1=10, para2=20)

# * Wall paint coverage calculator
# def calc_paint(width, height, coverage):
#     area = width * height
#     no_of_cans = area / coverage
#     print(f"{math.ceil(no_of_cans)} cans needed")

# height = int(input("Height of wall - "))
# width = int(input("Width of wall - "))
# coverage = 5
# calc_paint(height=height, width=width, coverage=coverage)
# round(10, 2)

# * Prime number checker
def prime_checker(n):
    isPrime = True
    for i in range(2, n):
        if (n % i == 0):
            isPrime = False
    if isPrime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is NOT a prime number")


n = int(input("Enter a number - "))
prime_checker(n)
