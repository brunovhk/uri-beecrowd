var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

var values = input.split(" ");

var a = parseFloat(values[0]);
var b = parseFloat(values[1]);
var c = parseFloat(values[2]);
var d = parseFloat(values[3]);

let exp1 = c + d;
let exp2 = a + b;

if (b > c && d > a && exp1 > exp2 && c > 0 && d > 0 && a % 2 == 0) {
  console.log("Valores aceitos");
} else {
  console.log("Valores nao aceitos");
}
