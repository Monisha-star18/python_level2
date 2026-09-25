print("Welcome to the Shopping Cart Calculator ")

cart_count = int(input("Enter the no of items : "))

cart = {}

for i in range(cart_count):
    item_name = input("Enter the cart item name : ")
    item_price = float(input ("Enter the item Price : "))

    cart[item_name] = item_price

subtotal = 0
for i in cart.values():
    subtotal += i


if subtotal > 5000:
    discount_percentage = 0.5
elif subtotal > 4000:
    discount_percentage = 0.4
elif subtotal > 3000:
    discount_percentage = 0.3
elif subtotal > 2000:
    discount_percentage = 0.2
elif subtotal > 1000:
    discount_percentage = 0.1
else:
    discount_percentage = 0

discount = subtotal * discount_percentage

tax = (subtotal-discount) * 0.05

total = subtotal -discount + tax


print()

for key,value in cart.items() :
    print(f"{key}                 : Rs.{value} ")

print("********************************************")
print(f"Subtotal          {subtotal}")
print(f"Discount          {discount}")
print(f"Tax               {tax}")
print("-----------------------------------")
print(f"Total               {total}")


