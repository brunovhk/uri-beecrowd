let input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let values = lines[0].split(" ");

let a = parseInt(values[0]);
let b = parseInt(values[1]);
let c = parseInt(values[2]);

let valuesSort = [a, b, c];
valuesSort.sort(function (a, b) {
  return a - b;
});

console.log(valuesSort[0]);
console.log(valuesSort[1]);
console.log(valuesSort[2]);
console.log('');
console.log(a);
console.log(b);
console.log(c);