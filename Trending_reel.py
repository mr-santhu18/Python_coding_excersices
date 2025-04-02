# bill payment program inspired by instagram reels
import random

names = input("enter everybody's names saparated by camma :")
names_list = names.split(",")
lenght = len(names_list)
random_choice = random.randint(0,lenght-1)
print(f"{names_list[random_choice]} will pay the bill")


# OR 

import random
names = input("enter everybody's names saparated by camma :")
names_list = names.split(",")
person_selected = random.choice(names_list)
print(f"{person_selected} will pay the bill")