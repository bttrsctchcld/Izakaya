there's a parent class, Restaurant, and a couple subclasses, Ticket and IceCreamParlor.

Restaurant hosts a list of dictionaries, a.k.a., a menu. each dictionary holding the name, description, price, stock, service window, and food allergies associated with each item on the menu, stored as json. the user passes the hours of operation as AM/PM strings, and hourly() reprocesses the strings for describe_restaurant() into a 0-23 span in which "12am" == 0 and "12pm" == 12.

Ticket inherits Restaurant and hosts a second list of dictionaries, a.k.a., a ticket, each dictionary holding the name and price of items which customer's have ordered via cross-reference from the Restaurant menu.

Parlor inherits Restaurant but hosts a simplified menu (in txt rather than json) with size-proportionate pricing and a simplified receipt.
