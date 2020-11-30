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

/* for js, you'll need to learn implementations for datetime (getHours()), json, and import 
 * in order to implement describeRestaurant, loadMenu, and writeMenu 
 *
 * in js, unlike python, classes can be elaborated beyond the initializing scope;
 * you can spread the functions out and thus avoid the need to create two subclasses
 *
 * be mindful of the differences between: js objects vs python dictionaries (valid keys, index notation),
 * js arrays vs python lists, js classes and prototypes vs python classes (null, new) */
