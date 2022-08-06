class Product:
    # giving every product an unique id
    stored_ids = [0]
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

        # check last id, create new id.
        self.id = self.stored_ids[-1] + 1
        self.stored_ids.append(self.id)

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        print(f'{self.name}, "{self.category}" : {self.price} id: {self.id}')