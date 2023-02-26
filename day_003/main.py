
#! Day 3 - Treasure Island

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1 = input(
    "You are at a cross road. Where do you want to go? [LEFT/RIGHT] - ").lower()
if (input1 == 'l' or input1 == 'left'):
    input2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat, or type 'swim' to swim across - ")
    if (input2 == 'w' or input2 == 'wait'):
        input3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose - ")
        if (input3 == 'red' or input3 == 'r'):
            print("It's a room full of fire. Game Over!")
        elif (input3 == 'yellow' or input3 == 'y'):
            print("\nYou found the treasure! You Win!")
        elif (input3 == 'blue' or input3 == 'b'):
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")
