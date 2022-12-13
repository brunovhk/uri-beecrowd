let input = require("fs").readFileSync("/dev/stdin", "utf8");
input = input.replace("\n", " ");

let values = input.split(" ");

let codigo = parseInt(values[0]);
let qtd = parseInt(values[1]);

let total = 0;
let itens = [
  {
    codigo: 1,
    especificacao: "Cachorro Quente",
    preco: 4.0,
  },
  {
    codigo: 2,
    especificacao: "X-Salada",
    preco: 4.5,
  },
  {
    codigo: 3,
    especificacao: "X-Bacon",
    preco: 5.0,
  },
  {
    codigo: 4,
    especificacao: "Torrada simples",
    preco: 2.0,
  },
  {
    codigo: 5,
    especificacao: "Refrigerante",
    preco: 1.5,
  },
];

itens.forEach((item) => {
  if (item.codigo === codigo) {
    total = qtd * item.preco;
  }
});

console.log(`Total: R$ ${total.toFixed(2)}`);
