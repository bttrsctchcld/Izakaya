class Restaurant {
	constructor(name,cuisine,uptime,downtime,menu=null) {
		this.name = name;
		this.cuisine = cuisine;
		this.uptime = uptime;
		this.downtime = downtime;
		this.item = {order:null,taste:null,price:0.00,avail:0,service:null,allergy:false}
		if menu = null {
			this.menu = [];
		} else {
			this.menu = menu;
		}
	}
}

function describeRestaurant {
	console.log(`${this.name} serves ${this.cuisine}. The restaurant opens at ${this.uptime} and closes at ${this.downtime}.`);
	realUptime,realDowntime = hourly(this.uptime,this.downtime);
	currentHour = getHours();
        if (realUptime < realDowntime && real_uptime <= current_hour < real_downtime) || (real_uptime > real_downtime && (current_hour >= real_uptime || current_hour < real_downtime)) {
		console.log("The restaurant is currently open.");
		return true;
	} else {
		console.log("The restaurant is currently closed.");
		return false;
	}
}

/* for js, you'll need to learn implementations for datetime (getHours()), json, and import 
 * in order to implement describeRestaurant, loadMenu, and writeMenu 
 *
 * in js, unlike python, classes can be elaborated beyond the initializing scope;
 * you can spread the functions out and thus avoid the need to create two subclasses
 *
 * be mindful of the differences between: js maps vs python dictionaries (valid keys, index notation),
 * js arrays vs python lists, js classes and prototypes vs python classes (null, new) */
