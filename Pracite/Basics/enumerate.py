foods = ["Burger", "Pizza", "Sandwich"]

for index,food in enumerate(foods,start=1):
    print(f"{index}. {food}")

#Modifying a list using enumerate

#for example lets say increase all the price by 10 
prices=[100,200,300,400]

for index,price in enumerate(prices):
    if price > 200 :
        prices[index] = price + 10

print(prices)

#enumurate with dict

food_prices = { 
                "Burger" : 120 ,
                "Pizza" : 150,
                "Cake" : 80
                }
for index,(food,price) in enumerate(food_prices.items(),start=1) :
    print(f"{index} . {food} - {price} ")

foods = ["Burger","Pizaa","Cake"]
prices = [120,130,80]

food_prices_list = zip(foods,prices)

print("the zipped value is : " food_prices)