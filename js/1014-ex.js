var input = require("fs").readFileSync("/dev/stdin", "utf8");
var values = input.split("\n");

var km = parseInt(values[0]);
var l = parseFloat(values[1]);

var kmL = km / l;

console.log(`${kmL.toFixed(3)} km/l`);
