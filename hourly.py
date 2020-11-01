def hourly(uptime,downtime):
    
    string_times = (uptime,downtime)
    real_times = []
    
    for time in string_times:
        if time == "12am":
            real_time = 0
        elif "pm" in time:
            real_time = int("".join(filter(str.isdigit,time))) + 12
        else:
            real_time = int("".join(filter(str.isdigit,time)))
        real_times.append(real_time)

    real_uptime,real_downtime = real_times
    return real_uptime,real_downtime
