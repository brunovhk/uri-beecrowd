var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

var values = input.split(" ");

var time = parseInt(values[0]);

var hours = parseInt(time / 3600);
var minutes = parseInt((time / 60) % 60);
var seconds = parseInt(time % 60);

console.log(`${hours}:${minutes}:${seconds}`);