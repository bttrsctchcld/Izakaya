from izakaya import Restaurant
from datetime import datetime
import json

class Ticket(Restaurant):
    def __init__(self,name,cuisine_type,uptime,downtime,tip=0,employee=False,check=None):
        super().__init__(name,cuisine_type,uptime,downtime)
        if check is None:
            self.check = []
        else:
            self.check = list(check)
        self.deductions = []
        self.employee = employee
        self.tip = 1 + (tip / 100)

    def __str__(self):
        self.load_check()
        self.total = self.calculate_total()
        return "%s : $%.2f" % (self.name,self.total)

    def __iter__(self):
        self.load_check()
        return(self.item["order"] for self.item in self.check)
    
    def __len__(self):
        self.load_check()
        return len(self.check)

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
                            self.check.append(self.item)
                            self.write_menu()
                            self.write_check()
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
                print("New check.")
        return self.check
    
    def write_check(self):
        with open("chekku.json","w") as file:
            json.dump(self.check,file)
    
    def strike_order(self,strike):
        self.load_check()
        for self.item in self.check:
            if strike.title() == self.item["order"]:
                self.check.remove(self.item)
                break
        self.write_check()

    def comp_order(self,comp):
        self.load_check()
        for self.item in self.check:
            if comp.title() == self.item["order"]:
                self.item["price"] = 0.00
                break
        self.write_check()

    def staff_meal(self):
        self.total = self.calculate_total()
        print("Employee discount applied.")
        return round(self.total * 0.00 if self.total <= 20.00 else self.total - 20.00,2)

    def happy_hour(self):
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        if current_hour >= 16 and current_hour < 19:
            print("Happy hour discount applied.")
            return round(self.total * 0.50,2)
        else:
            return self.total

    def ad_hoc_discount(self,revision):
        self.deductions.append(revision)

    def process_deductions(self):
        return sum(deduction for deduction in self.deductions)

    def calculate_total(self):
        self.total = round(sum([self.item["price"] for self.item in self.check]) * self.tip,2)
        self.total = self.happy_hour() 
        return self.total

    def simple_receipt(self):
        self.total = self.calculate_total() if self.employee == False else self.staff_meal()
        receipt = list(set([self.item["order"] for self.item in self.check]))
        adjustment = self.process_deductions()
        self.total -= adjustment
        print(f"""






                           {self.name}


                """)
        for unique_item in receipt:
            quantity = 0
            for self.item in self.check:
                if unique_item == self.item["order"]:
                    price = self.item["price"]
                    quantity += 1
            print(f"""
                    {quantity}     {unique_item}     {price * quantity}
                    """)
        print(f"""
            Thank you for visiting {self.name} and please come again.
                ${round(self.total,2)} (after {round((self.tip - 1) * 100,2)}% tip)
                
                """)
        for deduction in self.deductions:
            print(f"${deduction} deduction applied.")

    def itemized_receipt(self):
        self.total = self.calculate_total() if self.employee == False else self.staff_meal()
        adjustment = self.process_deductions()
        self.total -= adjustment
        print(f"""






                           {self.name}


                """)
        for self.item in sorted(self.check,key=lambda n: n["price"],reverse=True):
            print(f"""
                              {self.item["order"]}     {self.item["price"]}
                    """)
        print(f"""
            Thank you for visiting {self.name} and please come again.
                ${round(self.total,2)} (after {round((self.tip - 1) * 100,2)}% tip)
                
                """)
        for deduction in self.deductions:
            print(f"${deduction} deduction applied.")

if __name__ == "__main__":
    izakaya = Ticket("Alison's Restaurant","American","8am","12am",20.0)
    izakaya.customer_order()
    izakaya.simple_receipt()
