for CS50:
at the course's end, I considered the implementations which gave me the most trouble and trepidation in the problem sets: working across modules, working across functions, writing and reading across files and formats, list comprehension, and managing indeces in iteration.

so I opened a restaurant.

in Python, I've written two classes: a parent class Restaurant, a child class IceCreamParlor. Restaurant hosts a list of dictionaries, a.k.a., a menu. each dictionary holds the name, description, price, stock, service window, and food allergies associated with each item on the menu, stored as json. the user passes the hours of operation as AM/PM strings, and the decorator function for describe_restaurant() reprocesses the strings into a 0-23 span in which "12am" == 0.

print_menu() can print the full menu or else a service menu, e.g. breakfast, based on user input. customer_order() calls describe_restaurant() to determine, via datetime module, whether the restaurant is currently open or closed. if open, customer_order() takes two command-line inputs: (1) the customer's allergies and (2) the customer's order. customer_order() rejects orders for off-menu items, rejects orders from customer's whose allergy status matches a dictionary's allergy flag, rejects orders which are out-of-stock; and otherwise fulfills valid orders and decrements the item's stock by one unit per order. take_stock() prints a list of items with available units less than or equal to the user's input. restock_item() increments the stock for an item by however many units the user specifies.

but what if I want to open a chic, scaled-down IceCreamParlor next door to my Restaurant? I want IceCreamParlor to have access to Restaurant but otherwise want to manage a simpler menu with size-based pricing. so IceCreamParlor stores its flavors as a simple string in txt. customer_ticket() takes two inputs: (1) the order's flavor and (2) the order's size. the base price is hardcoded, and the dictionary, storing the sizes as keys, calculates the size's premium in addition to the base price.
