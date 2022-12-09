var input = require("fs").readFileSync("/dev/stdin", "utf8");
var values = input.split(" ");

var a = parseInt(values[0]);
var b = parseInt(values[1]);
var c = parseInt(values[2]);

var result = parseInt((a + b + Math.abs(a - b)) / 2);

var maiorAB = parseInt((result + c + Math.abs(result - c)) / 2);

console.log(`${maiorAB} eh o maior`);
