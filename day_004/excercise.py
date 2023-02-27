import random

# name_string = input("Enter your names: ")
# names = name_string.split(", ")
# random_num = random.randint(0, len(names)-1)
# # Alternative - random.choice(list_name) can be used to generate random choice from a list
# print(f"{names[random_num]} will pay the bill")

row1 = ['◻️', '◻️', '◻️']
row2 = ['◻️', '◻️', '◻️']
row3 = ['◻️', '◻️', '◻️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure: ")
row = int(position[0])-1
col = int(position[1])-1
map[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}")
