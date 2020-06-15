class ShoppingCart:
    # write your code here
    def __init__(self,  employee_discount=None,total = 0,items = []):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
    def add_item(self, name, price, quantity=1):
        for n in range(quantity):
            self.total += price
            self.price = price
            self.items.append(name)
        return self.total
    def mean_item_price(self):
        return self.total/len(self.items)

    def median_item_price(self):
        pass

    def apply_discount(self):
        if self.employee_discount != None:
            self.total -= self.total*self.employee_discount/100
            return self.total
        return "Sorry, there is no discount to apply to your cart :("
        
    def void_last_item(self):
        last = self.items[-1]
        self.total -= 