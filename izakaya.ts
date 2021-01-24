const describeRestaurant = (name,cuisine,uptime,downtime) => {
	console.log(`${name} serves ${cuisine}. The restaurant opens at ${uptime} and closes at ${downtime}.`);
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

const loadMenu = (menu=[]) => {
	const fs = require("fs");
	fs.readFile("./menu.json","utf8",(err,jsonString) => {
		if (err) {
			console.log("File read failed:",err);
			return;
		} try {
			menu = JSON.parse(jsonString); // menu successfully loads
		} catch (err) {
			console.log("Error parsing JSON string:",err);
		}
	});
}

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
	const menu = // loadMenu()
	const item = {order:null,taste:null,price:0.00,avail:0,service:null,allergy:false};
	const orders = [];
	for (let line of menu()) {
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

const hourly = (uptime,downtime) => {
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
