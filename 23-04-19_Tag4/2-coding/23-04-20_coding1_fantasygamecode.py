import random

print("Welcome to the charactor gen!")
print(" Lets name:")



# 5 character names
name1 = input ("name1: ")
name2 = input ("name2: ")
name3 = input ("name3: ")
name4 = input ("name4: ")
name5 = input ("name5: ")

luck = random.randint(1,3)

character_type = "Warrior"
if luck == 1:
    character_type = "Warrior"
elif luck == 2:
    character_type = "Wizard"
else:
    character_type = "Potato"

print