var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var employee = lines.shift();
var salary = parseInt(lines.shift());
var sales = parseFloat(lines.shift());

var comission = (sales * 0.15) + salary

console.log(`TOTAL = R$ ${comission.toFixed(2)}`);