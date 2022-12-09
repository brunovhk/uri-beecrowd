var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace('\n', ' ');

var values = input.split(' ');

var x1 = parseFloat(values[0]);
var y1 = parseFloat(values[1]);
var x2 = parseFloat(values[2]);
var y2 = parseFloat(values[3]);

var distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

console.log(`${distancia.toFixed(4)}`);
