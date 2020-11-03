# create Ticket subclass which opens tickets, stores orders, calculates payment, and closes tickets
# Ticket should I/O multiple orders as json
# Ticket should "close" orders upon payment (it's your choice whether "close" should mean to delete)
# payment should account for prices, taxes, tips, and discounts; use decorators
# overload __len__ to count the number of orders in a given ticket
# overload __repr__ to name the restaurant and list the total due as well as total paid
# however, the receipt should reproduce the ticket to show discrete line item x quantity

from izakaya import Restaurant

class Ticket(Restaurant):
    def __init__(self,check=None):
        super().__init__(self)
        self.line_item = {"order" : None, "price" : 0.00}
        if check is None:
            self.check = []
        else:
            self.check = list(check)
        self.total = total
        self.total = sum([self.line_item["price"] for self.line_item in self.check])
 
