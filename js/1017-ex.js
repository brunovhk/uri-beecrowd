var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace('\n', ' ');

var values = input.split(' ');

var time = parseInt(values[0]);
var speed = parseInt(values[1]);

var result = (speed / 12) * time;

console.log(`${result.toFixed(3)}`);