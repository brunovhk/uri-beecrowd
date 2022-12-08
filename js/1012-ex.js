var input = require("fs").readFileSync("/dev/stdin", "utf8");
var values = input.split(" ");

var a = parseFloat(values[0]);
var b = parseFloat(values[1]);
var c = parseFloat(values[2]);

var tri = (a * c) / 2;
var circ = Math.PI.toFixed(5) * (c * c);
var trap = ((a + b) * c) / 2;
var quad = b * b;
var ret = a * b;

console.log(`TRIANGULO: ${tri.toFixed(3)}`);
console.log(`CIRCULO: ${circ.toFixed(3)}`);
console.log(`TRAPEZIO: ${trap.toFixed(3)}`);
console.log(`QUADRADO: ${quad.toFixed(3)}`);
console.log(`RETANGULO: ${ret.toFixed(3)}`);
