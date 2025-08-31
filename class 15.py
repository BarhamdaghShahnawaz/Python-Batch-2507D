print("----Restaurant Menu----")
print("1. Pizza - Rs. 500")
print("2. Burger - Rs. 200")
print("3. Pasta - Rs. 300")
print("4. Salad - Rs. 150")
print("5. Biryani - Rs. 400")

choice = int(input("Enter the number of the item you want to order: "))

if choice == 1:
    item = "pizza"
    price = 500

elif choice == 2:
    item = "burger"
    price = 200

elif choice == 3:
    item = "pasta"
    price = 300

elif choice == 4:
    item = "salad"
    price = 150

elif choice == 5:
    item = "biryani"
    price = 400

else:
    print("invalid Choice")
    
    quit()


qty = int(input("Enter the quantity: "))

if qty <1:
    print("Invalid Quantity")

subtotal = price * qty




Student_card = input("Do you have a student card? (yes/no): ")


if Student_card == "yes":
 discount = subtotal * 0.10
 total = subtotal - discount

else:
 discount = 0
 total = subtotal


print("\n----Bill Details----")
print("Item:", item)
print("Quantity:", qty)
print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Total: Rs.", total)
print("Thank you for ordering!")
