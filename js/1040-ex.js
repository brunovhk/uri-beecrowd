let input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let values = input.split("\n");

let values1 = lines[0].split(" ");

let n1 = parseFloat(values1[0]);
let n2 = parseFloat(values1[1]);
let n3 = parseFloat(values1[2]);
let n4 = parseFloat(values1[3]);
let nExame = parseFloat(values[1]);

let media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10;
console.log(`Media: ${media.toFixed(1)}`);

if (media >= 7.0) {
  console.log(`Aluno aprovado.`);
} else if (media < 5.0) {
  console.log(`Aluno reprovado.`);
} else {
  console.log(`Aluno em exame.`);
}

if (media >= 5.0 && media <= 6.9) {
  console.log(`Nota do exame: ${nExame.toFixed(1)}`);
  var final = (media + nExame) / 2;
  if (final >= 5.0) {
    console.log(`Aluno aprovado.`);
    console.log(`Media final: ${final.toFixed(1)}`);
  } else if (final <= 4.0) {
    console.log(`Aluno reprovado.`);
    console.log(`Media final: ${final.toFixed(1)}`);
  }
}
