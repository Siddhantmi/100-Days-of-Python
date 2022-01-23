# If-else conditions

# #Exercise 1 - find odd or even 
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number%2 == 0:
#   print("This is an even number")
# else:
#   print("This is an odd number")

#-----------------------------------------------------------------------------------------------

# # Exercise 2 - BMI calulator 2.0
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")

#------------------------------------------------------------------------------------------------------

# # Exercise 3 - Leap year calculator

# # 🚨 Don't change the code below 👇
# print("Leap year calculator")
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if year%4 == 0:
#   if year%100 == 0:
#     if year%400==0:
#       print("leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("leap year")
# else:
#   print("Not leap year")

#-----------------------------------------------------------------------------------------------------------

# Exercise - 4 - Pizza order program

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# total_prize = 0

# if size == "S":
#   total_prize += 15
#   if add_pepperoni == "Y":
#    total_prize += 2
  
# elif size == "M":
#   total_prize += 20
#   if add_pepperoni == "Y":
#    total_prize += 3
# else:
#   total_prize += 25
#   if add_pepperoni == "Y":
#    total_prize += 3
# if extra_cheese == "Y":
#   total_prize += 1

# print(f"${total_prize}")

#-------------------------------------------------------------------------------------------------------------
# # Exercise - 5 - Love score calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# final_name = name1 + name2

# lower_final_name = final_name.lower()

# T = int(lower_final_name.count("t"))
# R = int(lower_final_name.count("r"))
# U = int(lower_final_name.count("u"))
# E = int(lower_final_name.count("e"))
# L = int(lower_final_name.count("l"))
# O = int(lower_final_name.count("o"))
# V = int(lower_final_name.count("v"))
# E = int(lower_final_name.count("e"))

# left_digit = T + R + U + E
# right_digit = L + O + V + E

# love_score = str(left_digit)+ str(right_digit)

# love_score = int(love_score)

# if love_score < 10 or love_score > 90:
#   print(f"Your love score is {love_score}, you both together are like coke and mentos.")
# elif love_score > 40 and love_score < 60:
#   print(f"Your love score is {love_score}, you both a make")
# else:
#   print(f"Your score is {love_score}")

#--------------------------------------------------------------------------------------------------------------------
# final project - treasure island game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇

direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if direction == "left":
  swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if swim_or_wait == "wait":
    Doors_option = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue". Which colour do you choose?\n')
    if Doors_option == "red":
      print("You found the treasure! You Win!")
    elif Doors_option == "blue":
      print("It's a room full of fire. Game Over.")
    elif Doors_option == "yellow":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Game Over")
else:
 print("Game Over")





