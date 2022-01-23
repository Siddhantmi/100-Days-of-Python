# Data type

## Exercuse 1 

#Press ctrl + / to uncomment this part of code

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆


# ####################################
# #Write your code below this line 👇


# sum = int(two_digit_number[0]) + int(two_digit_number[1])

# print(sum)

#-----------------------------------------------------------------------------------------------------------------------

##class task change print 3.0 insted of 7.0 

# # given code
# # print(3 * 3 + 3 / 3 - 3) // output 7.0
# # my code 
# print((3 + 3) / 3 * 3 - 3)

#-----------------------------------------------------------------------------------------------------------------------

## Exercise 2 - BMI calculator

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# new_height = float(height)
# BMI = float(weight) / (new_height * new_height)

# new_BMI = int(BMI)
# print(new_BMI)

#----------------------------------------------------------------------------------------------------------------------------

## Exercise - 3 - Days, weeeks and months you have left in your life calculator

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?\n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# years_left = 90 - int(age)

# days_left = years_left * 365

# weeks_left = years_left * 52

# months_left = years_left * 12

# print(f"You have {days_left} day, {weeks_left} weeks, and {months_left} months left" )
 
#--------------------------------------------------------------------------------------------------------------------
# Day 2 - Project - Tip calulator

print("welcome to tip calculator")


total_bill = input("What is your total bill ?")

tip_percentage = input("What percentage tip would you like to give ?")

total_people = input("How many people to split the bill ?")

tip_amount = (float(total_bill) * float(tip_percentage)) / 100

final_total_amount = float(total_bill) + tip_amount

each_person_amount = round(final_total_amount / int(total_people), 2)


print(f"Each person would have to pay amount : Rupee {each_person_amount} only  Enjoy!")
