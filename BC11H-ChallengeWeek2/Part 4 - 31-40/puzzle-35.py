# Pizza prices
pizza_prices = {
    "Americano": 13.45,
    "Beef": 15.80,
    "Calzone": 11.95,
    "Diet": 11.55,
    "Extra": 15.75,
    "Fantasia": 14.70,
}

# Total amount
total_amount = 62.00


def find_pizza_combination(pizzas, amount, combination=[]):
    if amount == 0 and len(combination) == 4:
        return combination

    if amount < 0 or len(combination) == 4:
        return None

    for pizza in pizzas:
        new_combination = combination + [pizza]
        remaining_amount = amount - pizza_prices[pizza]
        result = find_pizza_combination(pizzas, remaining_amount, new_combination)
        if result:
            return result


pizzas = list(pizza_prices.keys())
valid_combination = find_pizza_combination(pizzas, total_amount)

print("Valid pizza combination:", " ".join(valid_combination))

# Extra Beef Extra Fantasia -> BEEF
