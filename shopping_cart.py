class Item:
    def __init__(self, price, name, amount):
        self.price = price
        self.name = name
        self.amount = amount
    
    def __add__(self, item): 
        return Item(self.amount + item.amount)
    
    def __sub__(self, items_to_remove): 
        return Item(self.amount - items_to_remove)
    
class ShoppingCart: 
    def __init__(self):
        self.total_price = 0
        self.items = []
        self.discount = 0

    def add_item(self, new_item: Item):
        for item in self.items: 
            if new_item.name == item.name:
                item = item+new_item
                return
        self.total_price = self.total_price+new_item.price
        self.items.append(new_item)
        return

    def remove_item(self, item_to_remove, amount): 
        for item in self.items: 
            if item.name == item_to_remove:
                if item.amount - item_to_remove <= 0: 
                    self.total_price = self.total_price - (item.amount * item.price)
                    self.items.remove(item)
                    return
                else: 
                    item - item_to_remove
                    return

    def show_total_price(self): 
        return self.total_price - (self.total_price * self.discount)
    
    def discount_overall(self, discount): 
        self.discount = discount
