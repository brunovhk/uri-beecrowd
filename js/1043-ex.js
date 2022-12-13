let input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let values = lines[0].split(" ");

let a = parseFloat(values[0]);
let b = parseFloat(values[1]);
let c = parseFloat(values[2]);

if (a < b + c && b < a + c && c < b + c) {
  let perimetro = a + b + c;
  console.log(`Perimetro = ${perimetro.toFixed(1)}`);
} else {
  let area = ((a + b) * c) / 2;
  console.log(`Area = ${area.toFixed(1)}`);
}
