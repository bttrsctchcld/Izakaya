from datetime import datetime

def hourly(func):
    def decorate(self):

        print(f"{self.name} serves {self.cuisine_type}. The restaurant opens at {self.uptime} and closes at {self.downtime}.")

        now = datetime.now()
        current_hour = int(now.strftime("%H"))

        string_times = (self.uptime,self.downtime)
        real_times = []

        for time in string_times:
            if time == "12am":
                real_time = 0
            elif time == "12pm":
                real_time = 12
            elif "pm" in time:
                real_time = int("".join(filter(str.isdigit,time))) + 12
            else:
                real_time = int("".join(filter(str.isdigit,time)))
            real_times.append(real_time)

        real_uptime,real_downtime = real_times

        if (real_uptime < real_downtime and real_uptime <= current_hour < real_downtime) or (real_uptime > real_downtime and (current_hour >= real_uptime or current_hour < real_downtime)):
            print("The restaurant is currently open.")
            return True
        else:
            print("The restaurant is currently closed.")
            return False
    return decorate
