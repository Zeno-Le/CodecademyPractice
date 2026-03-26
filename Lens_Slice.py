# List of pizzas Len's Pizza Place sells
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

# List of prices for each of the types of Pizza
prices = [
  1,
  6,
  1,
  3,
  2,
  7,
  2
]

# Checking to see the number of pizza's priced at $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Finding the total number of types of pizzas sold at this joint
num_pizzas = len(toppings)

# Outputting infromation about the types of pizzas
print(f"We sell {num_pizzas} different kinds of pizza!")

# Creating a two dimensional list to combine prices and pizza toppings
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# Outputting the 2D list to display prices with the topping for the user
print(pizza_and_prices)

# Sorting by lowest price to highest price
pizza_and_prices.sort()

# Creating a variable for the cheapest pizza slice
cheapest_pizza = pizza_and_prices[0]

# Creating a variable for the most expesive slice
priciest_pizza = pizza_and_prices[-1]

# Removing a slice that the store is out of quantity for
pizza_and_prices.pop()

# Adding another topping to the list and resorting
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

# Creating a list for the top 3 cheapest slices
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)







