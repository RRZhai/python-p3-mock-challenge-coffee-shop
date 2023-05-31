class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if len(name) < 15 and len(name) > 1 and type(name) == str:
    #         self.name = name
    #     else:
    #         raise TypeError('Names must be between 1 and 15 characters')

    def orders(self, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if order.customer == self]
        
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        # return [order.coffee for order in self.orders()]
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees