from izakaya import *
from parlor import *

restaurant_name = input("What's your restaurant's name? ").title()
restaurant_style = input("What style of cuisine does your restaurant serve? ").title()
uptime = input("What time does the establishment open? ")
downtime = input("What time does the establishment close? ")

my_restaurant = Restaurant(restaurant_name, restaurant_style, uptime, downtime)
my_restaurant.load_menu()

dispatch = {
        "describe restaurant": my_restaurant.describe_restaurant,
        "load menu": my_restaurant.load_menu,
        "update menu": my_restaurant.update_menu,
        "print menu": my_restaurant.print_menu,
        "take stock": my_restaurant.take_stock,
        "restock": my_restaurant.restock,
        "destock": my_restaurant.destock,
}

while True:
    general_query = input("""
	
	What would you like to do?
	    
	    load menu  *  update menu  *  print menu

	    take stock  *  restock  *  destock

	    """).lower()

    if general_query == "q":
        break
    else:
        dispatch[general_query]()
