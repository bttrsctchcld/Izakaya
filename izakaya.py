from hourly import hourly
from datetime import datetime
import json

class Restaurant:
    def __init__(self,name,cuisine_type,uptime,downtime,menu=None):
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
        print(f"{self.name} serves {self.cuisine_type}. The restaurant opens at {self.uptime} and closes at {self.downtime}.") 
        real_uptime,real_downtime = hourly(self.uptime,self.downtime)
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        if (real_uptime < real_downtime and real_uptime <= current_hour < real_downtime) or (real_uptime > real_downtime and (current_hour >= real_uptime or current_hour < real_downtime)):
            print("The restaurant is currently open.")
            return True
        else:
            print("The restaurant is currently closed.")
            return False
    
    def load_menu(self):
        try:
            with open("menu.json","r") as file:
                self.menu = json.loads(file.read())
        except IOError:
            print("Missing menu file.")
        return self.menu
    
    def write_menu(self):
        with open("menu.json","w") as file:
            json.dump(self.menu,file)
    
    def update_menu(self,order,taste,price,avail,service,allergy):
        self.load_menu()
        if order not in self.item.values():
            self.item["order"] = order
        self.item["taste"] = taste
        if price >= 0.00:
            self.item["price"] = price
        if avail >= 0:
            self.item["avail"] = avail
        if service in ("breakfast","lunch","appetizer","entree","dessert","cafe","bar"):
            self.item["service"] = service
        self.item["allergy"] = allergy
        self.menu.append(self.item)
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
    
    def restock(self,stock,restock):
        self.load_menu()
        for self.item in self.menu:
            if stock.title() == self.item["order"]:
                self.item["avail"] += restock
                self.write_menu()
    
    def destock(self,discontinue):
        self.load_menu()
        for self.item in self.menu:
            if discontinue.title() == self.item["order"]:
                self.menu.remove(self.item)
                self.write_menu()
    
    def customer_order(self):
        operational = self.describe_restaurant()
        if operational == True:
            self.load_menu()
            self.print_menu()
            customer_allergy = input("Do you have any food allergies? ").lower()
            while True:
                order = input("What would you like to order? ").title()
                if order == "Q":
                    break
                for self.item in self.menu:
                    if order.title() == self.item["order"]:
                        if customer_allergy == "yes" and self.item["allergy"] == True:
                            print("I'm sorry but you appear to be allergic.")
                        elif int(self.item["avail"]) > 0:
                            self.item["avail"] -= 1
                            self.write_menu()
                            print("We'll have that right out to you.")
                        else:
                            print("I'm sorry but we're out of that right now.")

if __name__ == "__main__":
    izakaya = Restaurant("Alice's Restaurant","American","8am","12pm")
    izakaya.describe_restaurant()
