#List toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#List Prices
prices = [2, 6, 1, 3, 2,  7, 2]
#Counting how many "2" are in the list "prices"
num_two_dollar_slices = prices.count(2)
#getting lengh of list "toppings"
print(num_two_dollar_slices)
#Printing how many pizzas are in the first list
num_pizzas = len(toppings)
#Printing the the number of pizza toppings
print("We sell " + str(num_pizzas) + " diffrent kinds of pizza!")
# 2D list with pizza price and type
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]