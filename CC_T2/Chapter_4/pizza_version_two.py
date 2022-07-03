pizzas = ['pepperoni', 'cheese', 'sausage', 'NYC', 'Margarita']
f_pizza = pizzas[:]

pizzas.append('Manhattan')
f_pizza.append('Pinapple')

print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza.title())

print("\nMy friends favorite pizzas are:")
for pizaz in f_pizza[:]:
    print(pizaz.title())