<?php
$input = fgets(STDIN);
$values = explode(' ', $input);

$a = (int)$values[0];
$b = (int)$values[1];
$c = (int)$values[2];
$d = (int)$values[3];

$exp1 = $c + $d;
$exp2 = $a + $b;

if ($b > $c && $d > $a && $exp1 > $exp2 && $c > 0 && $d > 0 && ($a % 2 == 0)) {
    echo "Valores aceitos" . PHP_EOL;
} else {
    echo "Valores nao aceitos" . PHP_EOL;
}
