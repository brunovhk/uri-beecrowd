var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace('\n', ' ');

var values = input.split(' ');

var money = parseInt(values[0]);

var notes = [100, 50, 20, 10, 5, 2, 1];

console.log(money);

notes.forEach((note) => {
  var qtynotes = parseInt(money / note);
  console.log(`${qtynotes} nota(s) de R$ ${note.toFixed(2).replace(".", ",")}`);
  money %= note;
});
