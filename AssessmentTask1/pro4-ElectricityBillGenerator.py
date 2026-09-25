#Electricity Bill Generator 

customer_name = input("Enter the Name : ")
electricity_usage = float (input ("Enter the electricity Units Consumed : "))

match electricity_usage:

    case x if 0 <= x <= 100:
        electricity_bill_amount = x * 0

    case x if 101 <= x <= 200:
        electricity_bill_amount = x * 2.35

    case x if 201 <= x <= 400:
        electricity_bill_amount = x * 4.70

    case x if 401 <= x <= 500:
        electricity_bill_amount = x * 6.30

    case x if 501 <= x <= 600:
        electricity_bill_amount = x * 8.40

    case x if 601 <= x <= 800:
        electricity_bill_amount = x * 9.45

    case x if 801 <= x <= 1000:
        electricity_bill_amount = x * 10.50

    case x if x > 1000:
        electricity_bill_amount = x * 11.55

    case _:
        electricity_bill_amount = 0

tax = electricity_bill_amount * 0.05

total_bill = electricity_bill_amount + tax


print("Customer Name :", customer_name)
print("Units Consumed :", electricity_usage)
print()
print("Electricity Charge :", electricity_bill_amount)
print("Tax (5%)           :", tax)
print("------------------------------------------------")
print("Total Bill         :", total_bill)

