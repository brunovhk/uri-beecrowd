var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

var values = input.split(" ");

var time = parseInt(values[0]);

var years = parseInt(time / 365);
var months = parseInt((time % 365) / 30);
var days = parseInt((time % 365) % 30);

console.log(`${years} ano(s)`);
console.log(`${months} mes(es)`);
console.log(`${days} dia(s)`);