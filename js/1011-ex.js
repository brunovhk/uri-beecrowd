var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var raio = parseFloat(lines.shift()).toFixed(2);

var volume = ((4/3) * Math.PI.toFixed(5) * (Math.pow(raio, 3))).toFixed(3);

console.log(`VOLUME = ${volume}`);