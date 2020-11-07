from izakaya import Restaurant
from datetime import datetime
import json

class Ticket(Restaurant):
    def __init__(self,name,cuisine_type,uptime,downtime,tax=0,check=None):
        super().__init__(name,cuisine_type,uptime,downtime)
        self.order = {"order" : None, "price" : 0.00, "quantity" : 1}
        if check is None:
            self.check = []
        else:
            self.check = list(check)
        self.tax = 1 + (tax / 100)
        self.total = sum([self.order["price"] for self.order in self.check]) * self.tax

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
                            self.update_check()
                            print(self.check)
                            self.item["avail"] -= 1
                            self.write_menu()
                            print("We'll have that right out to you.")
                        else:
                            print("I'm sorry but we're out of that right now.")

    def load_check(self):
        try:
            with open("chekku.json","r") as file:
                self.check = json.loads(file.read())
        except IOError:
                print("Missing check.")
        return self.check
    
    def write_check(self):
        with open("chekku.json","w") as file:
            json.dump(self.check,file)

    def update_check(self):
        if self.item["order"] not in self.order.values():
            self.order["order"],self.order["price"],self.order["quantity"] = self.item["order"],self.item["price"],1
            self.check.append(self.order)
        else:
            for self.order in self.check:
                if self.item["order"] == self.order["order"]:
                    self.order["quantity"] += 1
    
    #@discount
    def staff_meal(self):
        pass

    #@discount
    def employee_discount(self):
        pass
    
    #@discount
    def lockdown_discount(self):
        pass

    def print_check(self):
        for self.order in self.check:
            print(f"""

                    {self.order["quantity"]}     {self.order["order"]}     {self.order["price"] * self.order["quantity"]}

                    """)
        print(f"""

            Thank you for coming to {self.name} and please come again.
                ${self.total}

                """)

if __name__ == "__main__":
    izakaya = Ticket("Alice's Restaurant","American","8am","12am",4.0)
    izakaya.customer_order()
