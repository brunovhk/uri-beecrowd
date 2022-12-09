var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace('\n', ' ');

var values = input.split(' ');

var distance = parseInt(values[0]) * 2;

console.log(`${distance} minutos`);
