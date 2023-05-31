class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        # return [order.customer for order in self.orders()]
        customers = []
        for order in self.orders():
            if order.customer not in customers:
                customers.append(order.customer)
        return customers
        
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / len(self.orders())