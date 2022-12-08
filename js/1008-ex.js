var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var number = parseInt(lines.shift());
var hours = parseInt(lines.shift());
var valuePerHour = parseFloat(lines.shift());

var salary = hours * valuePerHour

console.log(`NUMBER = ${number}`);
console.log(`SALARY = U$ ${salary.toFixed(2)}`);