from datetime import datetime
import json

# assign hours of operation for the restaurant and hours of availability for menu items depending on "service" value
    # breakfast 8am-12pm
    # lunch 11am-5pm
    # appetizer 5pm-10pm
    # entree 5pm-10pm
    # dessert 11am-10pm
    # bar 5pm-3am
    # cafe 8am-10pm

class Restaurant:
    def __init__(self,name,cuisine_type,uptime,downtime):
        self.name = name
        self.cuisine_type = cuisine_type
        self.uptime = uptime
        self.downtime = downtime
        self.item = {"order" : None, "taste" : None, "price" : 0.00, "avail" : 0, "service" : None, "allergy" : False}
        if menu is None:
            self.menu = []
        else:
            self.menu = list(menu)
    def describe_restaurant(self):
        print("{self.name} serves {self.cuisine_type}. The restaurant opens at {self.uptime} and closes at {self.downtime}.")
        if #TODO:
            print("The restaurant is currently open.")
        else:
            print("The restaurant is currently closed.")
    def load_menu(self):
        try:
            with open("menu.json", "r") as file:
                self.menu = json.loads(file.read())
        except IOError:
            print("Missing menu file.")
        return self.menu
    def write_menu(self):
        with open("menu.json", "w") as file:
            json.dump(self.menu,file)
    def update_menu(self):
        self.load_menu()
        while True:
            order = input("What's new on the menu today? ").title()
            if order not in self.item.values():
                self.item["order"] = order
            else:
                continue
            self.item["taste"] = input(str("Describe the item in a sentence or two. "))
            price = float(input("What's the market price? "))
            if price >= 0.00:
                self.item["price"] = price
            avail = int(input("How many orders can we serve today? "))
            if avail >= 0:
                self.item["avail"] = avail
            service = input("For which service: breakfast, lunch, appetizer, entree, dessert, cafe, or bar? ").lower()
            if service in ("breakfast", "lunch", "appetizer", "entree", "dessert", "cafe", "bar"):
                self.item["service"] = service
            allergy = input("Are there high-risk allergies associated with this item? ").lower()
            if allergy == "yes":
                self.item["allergy"] = True
            self.menu.append(self.item)
            prompt = input("Any more additions to the menu? ").lower()
            if prompt != "yes":
                break
        self.write_menu()
    def print_menu(self,menu_query="full"):
        self.load_menu()
        service_menu = [self.item for self.item in self.menu if menu_query.lower() in self.item["service"] or menu_query == "full"]
        for self.item in service_menu:
            print(f'\n\t{self.item["order"]}, {self.item["taste"]}, {self.item["price"]}')
    def take_stock(self):
        self.load_menu()
        supply_query = int(input("What's the maximum stock for current inventory you want to review? "))
        low_supply = [self.item for self.item in self.menu if int(self.item["avail"]) <= supply_query]
        print(low_supply)
    def decrement_stock(self):
        self.item["avail"] -= 1
        self.write_menu()
        return self.menu
    def restock(self,stock,restock):
        self.load_menu()
        for self.item in self.menu:
            if stock.title() in self.item["order"]:
                self.item["avail"] += restock
                self.write_menu()
    def destock(self,discontinue):
        for self.item in self.menu:
            if self.item["order"] == discontinue.title():
                self.menu.remove(self.item)
                return
    def customer_order(self):
        if #TODO:
            print("{self.name} is closed. {self.name} opens at {self.uptime}.")
        else:
            self.load_menu()
            self.print_menu()
            customer_allergy = input("Do you have any food allergies? ").lower()
            while True:
                order = input("What would you like to order? ").title()
                if order == "Q":
                    break
                for self.item in self.menu:
                    if order in self.item["order"]:
                        if self.item["service"] #TODO:
                            if customer_allergy == "yes" and self.item["allergy"] == True:
                                print("I'm sorry but you appear to be allergic.")
                            elif int(self.item["avail"]) > 0:
                                self.decrement_stock()
                                print("We'll have that right out to you.")
                            else:
                                print("I'm sorry but we're out of that right now.")
                        else:
                            print("{self.name} doesn't serve {self.item} at this time of day.")

if __name__ == "__main__":
    izakaya = Restaurant("Alice's Restaurant","American","8am","3am")
    izakaya.customer_order()
