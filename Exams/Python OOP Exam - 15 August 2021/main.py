from project.bakery import Bakery


b = Bakery('Niko')

print(b.add_table('OutsideTable', 52, 8))
print(b.add_table('InsideTable', 1, 4))


print(b.add_food('Cake', 'Torta', 4.50))
print(b.add_food('Cake', 'Garash', 7.50))
print(b.add_food('Bread', 'NewBread', 2.50))
print(b.add_drink('Tea', 'icy', 150, 'Lipton'))
# print(b.add_drink('Tea', 'icy', 150, 'Lipton'))
print(b.add_drink('Tea', 'Forest', 1, 'Loyd'))
print(b.add_drink('Water', 'clear', 500, 'Brand'))
print(b.reserve_table(7))


print(b.order_food(1, 'Torta', 'Burger', 'Steck', 'Garash'))
print(b.order_drink(1, 'Forest', 'clear', 'Bear', 'Water'))

print(b.order_food(52, 'Garash', 'Burger', 'Steck', 'Bread'))
print(b.order_drink(52, 'Mineral', 'icy', 'Water', 'Forest', 'clear'))

print(b.leave_table(1))
print(b.leave_table(52))
print(b.get_free_tables_info())

print(b.get_total_income())

