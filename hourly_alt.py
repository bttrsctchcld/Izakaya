def hourly(uptime,downtime):
        
    if uptime == "12am":
        real_uptime = 0
    elif "pm" in uptime:
        real_uptime = int("".join(filter(str.isdigit,uptime))) + 12
    else:
        real_uptime = int("".join(filter(str.isdigit,uptime))) 

    if downtime == "12am":
        real_downtime = 0
    elif "pm" in self.downtime:
        real_downtime = int("".join(filter(str.isdigit,downtime)))  + 12
    else:
        real_downtime = int("".join(filter(str.isdigit,downtime)))
    
    return real_uptime,real_downtime
