from datetime import datetime

def hourly(func):
    def decorate(self):

        if self.uptime == 0:
            print_uptime = "midnight"
        elif self.uptime > 0 and self.uptime < 12:
            print_uptime = str(self.uptime) + "am"
        else:
            print_uptime = str(self.uptime - 12) + "pm"

        if self.downtime == 0:
            print_downtime = "midnight"
        elif self.downtime > 0 and self.downtime < 12:
            print_downtime = str(self.downtime) + "am"
        else:
            print_downtime = str(self.downtime - 12) + "pm"
        print(f"{self.name} serves {self.cuisine_type}. The restaurant opens at {print_uptime} and closes at {print_downtime}.")
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        if (self.uptime < self.downtime and self.uptime <= current_hour < self.downtime) or (self.uptime > self.downtime and (current_hour >= self.uptime or current_hour < self.downtime)):
            print("The restaurant is currently open.")
            return True
        else:
            print("The restaurant is currently closed.")
            return False
    return decorate
