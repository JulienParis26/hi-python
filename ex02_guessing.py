# IMPORT THE MODULE
import json
import random

n = random.randint(1, 50)

number = int(input("Enter an integer from 1 to 50: "))
while n != "number":
   
    if number < n:
        print("It is more")
        number = int(input("Enter an number from 1 to 50: "))

    elif number > n:
        print("It is less")
        number = int(input("Enter an number from 1 to 50: "))

    else:
        print("The account is good!")
        break
    