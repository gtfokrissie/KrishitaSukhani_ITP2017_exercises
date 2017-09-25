favorite_pizzas = ['cheese', 'pepperoni', 'pineapple']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("mushroom")
friend_pizzas.append('carbonara')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(  pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print( pizza)
