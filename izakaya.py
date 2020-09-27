from restaurant import *
from parlor import *

restaurant_name = input("What's your restaurant's name? ").title()
restaurant_style = input("What style of cuisine does your restaurant serve? ").title()
parlor_base_price = float(input("What's the base price for a serving from your ice cream menu? "))
parlor_size_premium = float(input("What's the price premium for size increases? "))
parlor_scoop_premium = float(input("What's the price premium for scoop additions? "))

my_restaurant = IceCreamParlor(restaurant_name, restaurant_style, parlor_base_price, parlor_scoop_premium, parlor_scoop_premium)
my_restaurant.load_menu()
my_restaurant.get_stored_flavors()

dispatch = {
        'load menu': my_restaurant.load_menu(),
        "update menu": my_restaurant.update_menu(),
        "print menu": my_restaurant.print_menu(),
        "take stock": my_restaurant.take_stock(),
        "decrement stock": my_restaurant.decrement_stock(),
        "restock": my_restaurant.restock(),
        "customer order": my_restaurant.customer_order(),
        "load flavors": my_restaurant.get_stored_flavors(),
        "update flavors": my_restaurant.update_flavors(),
        "print flavors": my_restaurant.describe_flavors(),
        "customer ticket": my_restaurant.customer_ticket(),
}

while True:
    general_query = input("""
	
	What would you like to do?
	    
	    load menu  *  update menu  *  print menu

	    take stock  *  decrement stock  *  restock

	    customer order

	    load flavors  *  update flavors  *  print flavors

	    customer ticket

	    """).lower()

    if general_query == "q":
	break
    else:
        #TODO
