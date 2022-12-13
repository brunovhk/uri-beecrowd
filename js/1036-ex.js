var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

var values = input.split(" ");

var a = parseFloat(values[0]);
var b = parseFloat(values[1]);
var c = parseFloat(values[2]);

let delta = b * b - 4 * a * c;

if (delta <= 0 || a === 0) {
  console.log("Impossivel calcular");
} else {
  let r1 = (-b + Math.sqrt(delta)) / (2 * a);
  let r2 = (-b - Math.sqrt(delta)) / (2 * a);

  console.log(`R1 = ${r1.toFixed(5)}`);
  console.log(`R2 = ${r2.toFixed(5)}`);
}
