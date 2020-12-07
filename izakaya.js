class Restaurant {
	constructor(name,cuisine,uptime,downtime) {
		this.name = name;
		this.cuisine = cuisine;
		this.uptime = uptime;
		this.downtime = downtime;
		this.menu = [];
		}
	describeRestaurant() {
		console.log(`${this.name} serves ${this.cuisine}. The restaurant opens at ${this.uptime} and closes at ${this.downtime}.`);
		const realTimes = hourly(this.uptime,this.downtime);
		const realUptime = realTimes[0];
		const realDowntime = realTimes[1];
		const today = new Date();
		const currentHour = today.getHours();
		if ((realUptime < realDowntime && realUptime <= currentHour < realDowntime) || (realUptime > realDowntime && (currentHour >= realUptime || currentHour < realDowntime))) {
			console.log("The restaurant is currently open.");
			return true;
		} else {
			console.log("The restaurant is currently closed.");
			return false;
		}
	}

	/* in js, you need to use arrow notation in order to share methods within a class
	 * otherwise, "this" will misbehave
	 * in this case, this.menu works fine when called by loadMenu() directly but updateMenu()
	 * malfunctions when calling loadMenu() to load this.menu indirectly */

	updateMenu(order,taste,price,avail,service,allergy) {
		this.loadMenu();
		const item = {order:null,taste:null,price:0.00,avail:0,service:null,allergy:false};
		const orders = [];
		for (const line of this.menu) {
			orders.push(line.order);
		}
		if (orders.includes(order)) {
			return;
		} else {
			item.order = order;
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
		this.writeMenu();
	}
	loadMenu() {
		const fs = require("fs");
		fs.readFile("./menu.json","utf8",(err,jsonString) => {
			if (err) {
				console.log("File read failed:",err);
				return;
			}
			try {
				const loadedMenu = JSON.parse(jsonString);
				this.menu = loadedMenu;
			} catch (err) {
				console.log("Error parsing JSON string:",err);
			}
		});
	}
	writeMenu() {
		const fs = require("fs");
		let loadedMenu = JSON.stringify(this.menu);
		fs.writeFile("menu2.json",loadedMenu,function(err) {
			if (err) {
				console.log(err);
			}
		});
	}
}

function hourly(uptime,downtime) {
	stringTimes = [uptime,downtime];
	realTimes = [];
	for (let time of stringTimes) {
		if (time == "12am") {
			realTime = 0;
		}
		else if (time == "12pm") {
			realTime = 12;
		}
		else if (time.includes("pm")) {
			realTime = parseInt(time) + 12;
		} else {
			realTime = parseInt(time);
		}
		realTimes.push(realTime);
	}
	return realTimes;
}

izakaya = new Restaurant("Alice's Restaurant","American","8am","3pm");
izakaya.updateMenu("jeezy","cheesy",9.99,79,"lunch",false);
