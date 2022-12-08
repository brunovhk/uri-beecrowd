var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var primeiro = lines.shift().split(' ');
var segundo = lines.shift().split(' ');

var peca1 = parseInt(primeiro[0])
var qtd1 = parseInt(primeiro[1])
var valorUnit1 = parseFloat(primeiro[2]);

var peca2 = parseInt(segundo[0])
var qtd2 = parseInt(segundo[1])
var valorUnit2 = parseFloat(segundo[2]);

var valPagar = parseFloat((qtd1 * valorUnit1) + (qtd2 * valorUnit2)).toFixed(2);


console.log(`VALOR A PAGAR: R$ ${valPagar}`);