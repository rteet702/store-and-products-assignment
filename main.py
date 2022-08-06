from classes.store import Store
from classes.product import Product

new_store = Store('7/11')

new_products = [
    Product('Camel', 7.68, 'tobacco'), 
    Product('Marlboro', 8.68, 'tobacco'), 
    Product('Pyramid', 5.68, 'tobacco'), 
    Product('AmericanSpirits', 10.68, 'tobacco')]

for item in new_products:
    new_store.add_product(item)

new_store.set_clearance('tobacco', .25)
new_store.inflation(.10)
new_store.sell_product(1)
new_store.print_inventory()