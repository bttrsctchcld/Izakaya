from datetime import datetime

def hourly(func):
    def decorate(self):

        print(f"{self.name} serves {self.cuisine_type}. The restaurant opens at {self.uptime} and closes at {self.downtime}.")

        now = datetime.now()
        current_hour = int(now.strftime("%H"))

        if self.uptime == "12am":
            real_uptime = 0
        elif "pm" in self.uptime:
            real_uptime = int("".join(filter(str.isdigit,self.uptime))) + 12
        else:
            real_uptime = int("".join(filter(str.isdigit,self.uptime))) 

        if self.downtime == "12am":
            real_downtime = 0
        elif "pm" in self.downtime:
            real_downtime = int("".join(filter(str.isdigit,self.downtime)))  + 12
        else:
            real_downtime = int("".join(filter(str.isdigit,self.downtime))) 
        
        if (real_uptime < real_downtime and real_uptime <= current_hour < real_downtime) or (real_uptime > real_downtime and (current_hour >= real_uptime or current_hour < real_downtime)):
            print("The restaurant is currently open.")
            return True
        else:
            print("The restaurant is currently closed.")
            return False
    return decorate
