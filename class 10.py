# Membership Operators 
# Membership Operators ka use hota hai ye check karne ke 
# liye ki koi value (element) kisi sequence me present hai ya nahi.
# Sequence ho sakta hai:
# String
# List etc.

# 1) in
# Definition:
# in tab True return karta hai jab value sequence me present ho.

# Example:
# fruits = ["apple", "banana", "cherry"]

# print("apple" in fruits)   # True
# print("mango" in fruits)   # False


# 2) not in
# Definition:
# not in tab True return karta hai jab value sequence me present na ho.

# # Example:
# fruits = ["apple", "banana", "cherry"]

# print("mango" not in fruits)   # True
# print("banana" not in fruits)  # False

# ------------------------------------------------------------------------------------------------------------

# Identity Operators – Notes
# Definition
# Identity Operators ka use hota hai do variables ke memory address
#  compare karne ke liye, ye check karte hain ki kya dono variables same object ko refer kar rahe hain ya nahi.
# Important: Ye values compare nahi karte, sirf memory location 
# (object identity) compare karte hain.


# 1) is
# Definition:
# is tab True return karta hai jab dono variables same 
# object ko point karein (same memory address).

# Example:
# x = [1, 2, 3]
# y = x  # y bhi same list ko refer karta hai

# print(x is y)   # True


# 2) is not
# # Definition:
# # is not tab True return karta hai jab dono 
# variables different objects ko refer karein (memory address alag ho).

# Example:
# x = [1, 2, 3]
# y = [4, 5, 6]  # values same, lekin alag objects

# print(x is not y)   # True
