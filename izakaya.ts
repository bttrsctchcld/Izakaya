const describeRestaurant = (name,cuisine,uptime,downtime) => {
	console.log(`${name} serves ${cuisine}. The restaurant opens at ${uptime} and closes at ${downtime}.`);
	return [uptime,downtime];
}
const operational = () => {
	const realTimes = hourly(uptime,downtime);
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
const loadMenu = () => {
	const json = require('/Users/jcharity/Documents/GitHub/Izakaya/menu.json');
	return json;
};
const writeMenu = (menu) => {
	const fs = require("fs");
	const loadedMenu = JSON.stringify(menu);
	fs.writeFile("menu2.json",menu,function(err) {
		if (err) {
			console.log(err);
		}
	});
}
const updateMenu = (order,taste,price,avail,service,allergy) => {
	const menu = loadMenu();
	const item = {order:null,taste:null,price:0.00,avail:0,service:null,allergy:false};
	const orders = [];
	for (let line of menu) {
		orders.push(line.order);
	} if (orders.includes(order)) {
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
	menu.push(item);
	writeMenu(menu);
}
const hourly = () => {
	const stringTimes = hoursOfOperation();
	const realTimes = [];
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
const printMenu = (self,menu_query="full") => {
	const menu = load_menu();
	const service_menu = []
	for (let item of menu) {
		if (menu_query in item["service"] || menu_query == "full") {
			service_menu.push(item);
		}
	}
        for (let item in service_menu) {
            console.log(`\n\t{self.item["order"]}, {self.item["taste"]}, {self.item["price"]}`)
	}
}
const take_stock = () => {
	const menu = load_menu()
        const supply_query = int(input("What's the maximum stock for current inventory you want to review? "))
        const low_supply = []
	for (let item of menu) {
		if (item["avail"] <= supply_query) {
			low_supply.push(item);
		}
	}
	console.log(low_supply)
}
const restock = (stock,restock) => {
	const menu = load_menu();
        for (let item of menu) {
		if (stock == item["order"]) {
			self.item["avail"] += restock
		}
	}
        write_menu();
}
const destock = (discontinue) => {
        const menu = load_menu()
        for (let item of menu) {
		if (discontinue == item["order"]) {
			menu.remove(item)
		}
	}
        write_menu()
}
const customerOrder = () => {
        const is_operational = operational()
        if (is_operational === true) {
		const menu = load_menu();
		print_menu();
		const customer_allergy = prompt("Do you have any food allergies? ").toLowerCase()
		while(true) {
			let order = input("What would you like to order? ").title()
			if (order == "Q") {
				break
			}
			for (let item in menu) {
				if (order == item["order"]) {
					if (customer_allergy === "yes" && item["allergy"] === true) {
						console.log("I'm sorry but you appear to be allergic.");
						break;
					} else if (item["avail"] > 0) {
						item["avail"] -= 1;
						write_menu();
						console.log("We'll have that right out to you.");
						break;
					} else {
						console.log("I'm sorry but we're out of that right now.")
						break;
					}
				}
			}
		}
	}
}
console.log(loadMenu());
updateMenu("jeezy","cheesy",9.99,79,"lunch",false);
console.log(loadMenu());
