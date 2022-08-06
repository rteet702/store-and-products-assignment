class Store:
    def __init__(self, name):
        self.name = name

        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        for item in self.products:
            if item.id == id:
                item.print_info()
                self.products.pop(self.products.index(item))

    def inflation(self, percent_increase):
        for item in self.products:
            item.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for item in self.products:
            if item.category == category:
                item.update_price(percent_discount, False)

    def print_inventory(self):
        print('Printing Inventory:\n')
        for item in self.products:
            item.print_info()