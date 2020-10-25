from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_hour = int(now.strftime("%H"))
print("Current time is",current_time)
print("Current hour is",current_hour)
