from izakaya import Restaurant

class Ticket(Restaurant):
    def __init__(self,tax=0,check=None):
        super().__init__(self)
        self.order = {"order" : None, "price" : 0.00}
        if check is None:
            self.check = []
        else:
            self.check = list(check)
        self.tax = 1 + (tax / 100)
        self.total = sum([self.order["price"] for self.order in self.check]) * self.tax

    def __len__(self):
        return len(self.check)

    def __repr__(self):
        return self.name + " : " + str(self.total)

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
                            update_check()
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
        self.order["order"],self.order["price"] = self.item["order"],self.item["price"]
        self.check.append(self.order)
        return self.check

    def print_check(self):
        receipt = set(self.check)
        for line in receipt:
            print(f"\t#TODO\t{self.order["order"]}\t({self.order["price"] * quantity)")
        print(f"\n\n\nThank you for coming to {self.name} and please come again.\n\t${self.total}")
