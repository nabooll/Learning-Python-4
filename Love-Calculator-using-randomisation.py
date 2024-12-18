#FIrst we need to import the module that we're gonna use, which is random
import random

# Love Calculator
print("Let's see how much is your score!")

name1 = input("Your Name: ")
name2 = input("Name of the person you want to match: ")

#Now we use random.randint to print random number in range 1-100
love_score = random.randint(1, 100)
print(f"Your Love Score is {love_score}!")

# Conditional checks based on the concatenated love score
if love_score > 90:
    print("You guys are ready to get married <3")
elif 90 >= love_score >= 75:
    print("You are a good match!")
elif 75 > love_score > 50:
    print("You still need to try harder!")
else:
    print("Sorry, you are not a match.")
