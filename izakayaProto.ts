function Restaurant(name,cuisine,uptime,downtime) {
	this.name = name;
	this.cuisine = cuisine;
	this.uptime = uptime;
	this.downtime = downtime;
	this.menu = [];
}

Restaurant.prototype.description = function() {
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
};

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
};

Restaurant.prototype.load_menu = function() {
	const fs = require("fs");
	fs.readFile("./menu.json","utf8",(err,jsonString) => {
		if (err) {
			console.log("File read failed:",err);
			return;
		}
		try {
			menu = JSON.parse(jsonString); // menu successfully loads
			return menu;
		} catch (err) {
			console.log("Error parsing JSON string:",err);
		}
	});
};

let blue_collar = new Restaurant("Blue Collar","American","9am","6pm");
blue_collar.description();
blue_collar.load_menu();
console.log(blue_collar.menu);
