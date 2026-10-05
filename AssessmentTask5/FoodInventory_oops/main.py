from datetime import date

from src.config import get_foodPath, get_orderPath
from src.models.order import Order
from src.repositories.food_repository import FoodRepository
from src.repositories.order_repository import OrderRepository
from src.services.food_service import FoodService
from src.services.order_service import OrderService
from src.utility.display import money

#from src.exceptions.exceptions import  get_positive_integer , get_text_input
from src.utility.input_exceptions import InputValidator

ALLOWED_PAYMENT_METHODS = ["Cash", "Card", "UPI"]


def display_menu() -> None:

    print("\n===================================")
    print("        FOOD ORDER SYSTEM")
    print("===================================")
    print(" 1. Display Food Items")
    print(" 2. Search Food")
    print(" 3. Find Maximum Price Food")
    print(" 4. Find Minimum Price Food")
    print(" 5. Display Orders")
    print(" 6. Find Order By ID")
    print(" 7. Find Orders By Status")
    print(" 8. Calculate Order Total")
    print(" 9. Calculate Total Revenue")
    print("10. Calculate Total Orders")
    print("11. Add Order")
    print("12. Exit")
    print("===================================")




def main() -> None:

    try:
        food_repository = FoodRepository(get_foodPath())
        order_repository = OrderRepository(get_orderPath())

        foods = food_repository.get_all()
        orders = order_repository.get_all()

        food_service = FoodService(foods)
        order_service = OrderService(orders, foods)

        while True:

            display_menu()
            choice = input("Enter your choice: ").strip()

            # ---------- FOOD OPERATIONS ----------

            if choice == "1":
                food_service.display_foods()

            elif choice == "2":
                name = InputValidator.get_text_input("Enter food name: ")
                food_service.display_search_results( food_service.search_food(name))

            elif choice == "3":
                food = food_service.find_maximum_price()

                if food:
                    print(f"\nMaximum Price Food :  {food.food_name} | {money(food.price)}")
                else:
                    print("No food items found.")

            elif choice == "4":
                food = food_service.find_minimum_price()

                if food:
                    print( f"\nMinimum Price Food : {food.food_name} | {money(food.price)}")
                else:
                    print("No food items found.")

            # ---------- ORDER OPERATIONS ----------

            elif choice == "5":
                order_service.display_orders()

            elif choice == "6":
                order_id = InputValidator.get_positive_integer("Enter Order ID: ")
                order = order_service.find_order_by_id(order_id)

                if order:
                    order_service.display_order_details(order)
                else:
                    print("Order not found.")

            elif choice == "7":
                status = InputValidator.get_text_input("Enter status: ")
                matches = order_service.find_orders_by_status(status)

                if matches:
                    order_service.display_order_table(matches)
                else:
                    print("No orders found.")

            elif choice == "8":
                order_id = InputValidator.get_positive_integer("Enter Order ID: ")
                order = order_service.find_order_by_id(order_id)

                if order:
                    total = order_service.calculate_order_total(order)
                    print(f"\nOrder Total : {money(total)}")
                else:
                    print("Order not found.")

            elif choice == "9":
                revenue = order_service.calculate_total_revenue()
                print(f"\nTotal Revenue : {money(revenue)}")

            elif choice == "10":
                print(f"\nTotal Orders : {order_service.calculate_total_orders()}")

            # ---------- ADD ORDER ----------

            elif choice == "11":
                print("\n--------- ADD ORDER ---------")

                order_id = InputValidator.get_positive_integer("Enter Order ID: ")

                #check if the order id already exist or not 
                if order_service.find_order_by_id(order_id):
                    print("Order ID already exists.")
                    continue

                customer_name = InputValidator.get_text_input("Enter Customer Name: ")
                food_id = InputValidator.get_positive_integer("Enter Food ID: ")

                #check whether the food exist
                food = food_service.find_food_by_id(food_id)

                if food is None:
                    print("Food ID does not exist.")
                    continue

                #check the quantity as the quanity should not exceed 
                quantity = InputValidator.get_positive_integer("Enter Quantity: ")

                if quantity > food.stock_quantity:
                    print(f"Only {food.stock_quantity} items available.")
                    continue

                #is the payment method correct 
                payment_input = InputValidator.get_text_input("Enter Payment Method (Cash/Card/UPI): ")

                payment_method = [ m 
                                    for m in ALLOWED_PAYMENT_METHODS
                                    if m.lower() == payment_input.lower()]

                if payment_method is None:
                    print("Invalid payment method.")
                    print("Allowed: Cash, Card, UPI")
                    continue

                new_order = Order( order_id=order_id, customer_name=customer_name, food_id=food_id,
                                    quantity=quantity, order_date=date.today(), status="Pending", payment_method=payment_method,)

                # Reduce stock, then save both files
                food.stock_quantity -= quantity
                order_service.orders.append(new_order)

                order_repository.save_all(order_service.orders)
                food_repository.save_all(foods)

                print("Order added successfully.")
                order_service.display_order_details(new_order)

            # ---------- EXIT ----------

            elif choice == "12":
                print("Thank you for using Food Order System.")
                break

            else:
                print("Invalid choice. Please select 1-12.")

    except FileNotFoundError as error:
        print(f"File error: {error}")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
