pizzas=['cheese', 'pepperoni', 'pineapple','hawaiian','mushroom']
print("Here are the first three types of pizza in my list:")
for pizza in pizzas[:3]:
    print(pizza.title())

pizzas=['cheese', 'pepperoni', 'pineapple','hawaiian','mushroom']
print("\nHere are some other three types of pizza in my list:")
for pizza in pizzas[1:4]:
    print(pizza.title())

pizzas=['cheese', 'pepperoni', 'pineapple','hawaiian','mushroom']
print("\nHere are the last three types of pizza in my list:")
for pizza in pizzas[-3:]:
    print(pizza.title())
