let input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let values = lines[0].split(" ");

let a = parseInt(values[0]);
let b = parseInt(values[1]);

if (a % b === 0 || b % a === 0) {
  console.log("Sao Multiplos");
} else {
  console.log("Nao sao Multiplos");
}
