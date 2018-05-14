var Observable = require("FuseJS/Observable");

function Person(picture){
	this.picture = picture;
}

function Item(time, ampm, title, project, people){
	this.time = time;
	this.ampm = ampm;
	this.title = title;
	this.project = project;
	this.people = people;
}

var items = Observable(
	new Item(8, "AM", "Finish Home Screen", "Use Macaw", Observable()),
	new Item(11, "AM", "Lunch Break", "", Observable()),
	new Item(2, "PM", "Finish prototype", "InVision", [new Person("Assets/avatarcalendar3.png"), new Person("Assets/avatarcalendar2.png"), new Person("Assets/avatarcalendar.png")])
);

var itemsView = items.map(function(item, index){
	return {
		item : item, delay : index * 0.08,
		lineDelay : (items.length - index + 1) * 0.1,
		isLast : index === items.length - 1,
		hasTitle : item.title.length > 0,
		hasProject : item.project.length > 0,
		hasPeople : item.people.length > 0
	};
});

module.exports =  {
	items: itemsView
};
