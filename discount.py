discounts = []

def discount(func):
    discounts.append(func)
    return func

@discount
def employee_discount(total):
    return round(total * 0.00 if total <= 20.00 else total - 20.00,2)

@discount
def lockdown_discount(total):
    return round(total * 0.85,2)

@discount
def ad_hoc_discount(total):
    revision = input("Deduct how much, in dollar amount, from customer's check? ")
    return round(total - revision,2)

print(discounts)
