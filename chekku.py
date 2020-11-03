# create Ticket class which opens tickets, stores orders, calculates payment, and closes tickets
# Ticket doesn't need to be child class in re Restaurant
# Ticket should I/O multiple orders as json
# Ticket should "close" orders upon payment (it's your choice whether "close" should mean to delete)
# payment should account for prices, taxes, tips, and discounts; use decorators
# overload __len__ to count the number of orders in a given ticket
# overload __repr__ to name the restaurant and list the total due as well as total paid
# however, the receipt should reproduce the ticket to show discrete line item x quantity
