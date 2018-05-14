var Observable = require("FuseJS/Observable");

var foobar = Observable(1);
foobar.value = 10;


function someFunction(x){
	var thisFunctionDoesSomething = "foo";

	for (var i = 0; i < 10; i++){
		debug_log("We do some logging");
	}

	return thisFunctionDoesSomething;
}

module.exports = {
	foobar: foobar,
	someFunction: someFunction
};
