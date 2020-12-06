class Restaurant {
	constructor(name,cuisine,uptime,downtime,menu=[]) {
		this.name = name;
		this.cuisine = cuisine;
		this.uptime = uptime;
		this.downtime = downtime;
		this.menu = menu;
		}
	describeRestaurant() {
		console.log(`${this.name} serves ${this.cuisine}. The restaurant opens at ${this.uptime} and closes at ${this.downtime}.`);
		}
	updateMenu(order,taste,price,avail,service,allergy) {
		const item = {order:null,taste:null,price:0.00,avail:0,service:null,allergy:false};
		const orders = [];
		for (const line of this.menu) {
			orders.push(line.order);
		}
		console.log(orders);
		if (!(order in orders)) {
			item.order = order;
		} else {
		}
		item.taste = taste;
		if (price >= 0.00) {
			item.price = price;
		}
		if (avail > 0) {
			item.avail = avail;
		}
		const services = ["breakfast","lunch","appetizer","entree","dessert","cafe","bar"];
		if (services.includes(service)) {
			item.service = service;
		}
		item.allergy = allergy;
		this.menu.push(item);
		console.log(this.menu);
	}
}



izakaya = new Restaurant("Alice's Restaurant","American","8am","12pm");
izakaya.describeRestaurant();
izakaya.updateMenu("hamburger","It's a hamburger",3.99,100,"lunch",false);
izakaya.updateMenu("cheeseburger","It's a cheeseburger",5.99,100,"lunch",false);
izakaya.updateMenu("cheeseburger","It's a cheeseburger",5.99,100,"lunch",false);


/* for js, you'll need to learn implementations for datetime (getHours()), json, and import 
 * in order to implement describeRestaurant, loadMenu, and writeMenu 
 *
 * in js, unlike python, classes can be elaborated beyond the initializing scope;
 * you can spread the functions out and thus avoid the need to create two subclasses
 *
 * be mindful of the differences between: js maps vs python dictionaries (valid keys, index notation),
 * js arrays vs python lists, js classes and prototypes vs python classes (null, new) */
