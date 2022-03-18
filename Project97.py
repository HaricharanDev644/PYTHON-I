import random

num = random.randint(1,9)

chance = int(input("Enter the number you guessed: "))
if chance == num:
    print("You have guessed it right")
elif chance != num:
    print("Your guess is too low")

chance2 = int(input("Enter the number you guessed: "))
if chance2 == num:
    print("You have guessed it right")
elif chance2 != num:
    print("Your guess is too low")

chance3 = int(input("Enter the number you guessed: "))
if chance3 == num:
    print("You have guessed it right")
elif chance3 != num:
    print("Your guess is too low")

chance4 = int(input("Enter the number you guessed: "))
if chance4 == num:
    print("You have guessed it right")
elif chance4 != num:
    print("Your guess is too low")

chance5 = int(input("Enter the number you guessed: "))
if chance5 == num:
    print("You have guessed it right, Game Over")
elif chance5 != num:
    print("You have guessed is too low, Game Over")