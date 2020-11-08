from izakaya import Restaurant
from datetime import datetime
import json

class Ticket(Restaurant):
    def __init__(self,name,cuisine_type,uptime,downtime,tip=0,employee=False,check=None):
        super().__init__(name,cuisine_type,uptime,downtime)
        self.order = {"order" : None, "price" : 0.00, "quantity" : 1}
        if check is None:
            self.check = []
        else:
            self.check = list(check)
        self.employee = employee
        self.tip = 1 + (tip / 100)
        self.adjustments = []
        self.total = sum([self.order["price"] for self.order in self.check])
        self.paid = False

    def customer_order(self):
        operational = self.describe_restaurant()
        if operational == True:
            self.load_menu()
            self.load_check()
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
                            break
                        elif int(self.item["avail"]) > 0:
                            self.item["avail"] -= 1
                            
                            for self.order in self.check:
                                if self.item["order"] == self.order["order"]:
                                    self.order["quantity"] += 1
                                    break
                            self.order["order"] = self.item["order"]
                            self.order["price"] = self.item["price"]
                            self.check.append(self.order)
                            self.write_menu()
                            self.update_check()
                            print("We'll have that right out to you.")
                            break
                        else:
                            print("I'm sorry but we're out of that right now.")
                            break

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
        for self.order in self.check:
            if self.item["order"] == self.order["order"]:
                self.order["quantity"] += 1
                print(self.check)
                return
        self.order["order"],self.order["price"] = self.item["order"],self.item["price"]
        self.check.append(self.order)
        print(self.check)
    
    def adjustment(self,func):
        self.adjustments.append(func)
        return func

    @adjustment
    def sales_tax(self):
        return self.total * 1.04

    @adjustment
    def staff_meal(self):
        return self.total * 0 if self.employee == True and self.total <= 20.00

    @adjustment
    def staff_discount(self):
        return self.total * 0.50 if self.employee == True and self.total > 20.00
    
    def final_adjustments(self):
        print(self.adjustments)

    def close_check(self):
        for self.order in self.check:
            print(f"""

                    {self.order["quantity"]}     {self.order["order"]}     {self.order["price"] * self.order["quantity"]}

                    """)
        print(f"""

            Thank you for coming to {self.name} and please come again.
                ${self.total * self.tip}

                """)
        self.paid = True

if __name__ == "__main__":
    izakaya = Ticket("Alice's Restaurant","American","8am","12am",4.0)
    izakaya.customer_order()
