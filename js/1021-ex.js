var input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

var values = input.split(" ");

var money = parseFloat(values[0]);

money += 0.001;

let notes = [100, 50, 20, 10, 5, 2];
let coins = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01];

console.log(`NOTAS:`);

notes.forEach((note) => {
  var qtyNotes = parseInt(money / note);
  console.log(`${qtyNotes} nota(s) de R$ ${note.toFixed(2)}`);
  money %= note
});

console.log(`MOEDAS:`);

coins.forEach(coin => {
    var qtyCoins = parseInt(money / coin);
    console.log(`${qtyCoins} moeda(s) de R$ ${coin.toFixed(2)}`);
    money -= qtyCoins * coin;
});
