# 1. What are Loops?
# Loop ek programming structure hai jo humein ek hi code ko bar-bar repeat karne ki
# facility deta hai, jab tak koi condition true hai.
# Iska use tab hota hai jab humein repetitive tasks perform karne ho (e.g. numbers print karna, 
#  list traverse karna, etc.).


#  (a) for loop

#  Jab humein sequence (list, tuple, string, range, etc.) ke elements
#   par iterate karna ho.

#  Syntax :
# for variable in sequence:
#     # code to repeat


#  Example 1:
# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#    print(fruit)


#  Example 2:
# for i in range(1, 6):
#     print(i)



#(b) while loop

# Jab tak condition true rahe, tab tak code repeat hota hai.

# Syntax:
# while condition:
#     # code to repeat


# Example 1:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# Example 2:
# pin = ""
# while pin != "1234":
#     pin = input("Enter PIN: ")
# print("Access Granted!")
