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
