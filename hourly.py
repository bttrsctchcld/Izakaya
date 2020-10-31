# pass uptime and downtime, as 0-23 integers, to hourly() and return AM/PM strings

def hourly(self):
    def decorate(func):
        def hours (*_args):
            if real_hour = 0:
	        print_hour = "midnight"
            elif real_hour > 0 and current_hour < 12:
	        print_hour = str(current_hour) + "am"
            else:
	        print_hour = str(current_hour - 12) + "pm"
            return print_hour
        return hours
    return decorate

@hourly
def describe_restaurant(self):
    print(f"{self.name} serves {self.cuisine_type}. The restaurant opens at {print_uptime} and closes at {print_downtime}.")
    now = datetime.now()
    current_hour = int(now.strftime("%H"))
    if (self.uptime < self.downtime and self.uptime <= current_hour < self.downtime) or (self.uptime > self.downtime and (current_hour >= self.uptime or current_hour < self.downtime)):
        print("The restaurant is currently open.")
        return True
    else:
        print("The restaurant is currently closed.")
        return False
