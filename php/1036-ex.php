<?php
$input = fgets(STDIN);
$values = explode(' ', $input);

$a = round($values[0], 1);
$b = round($values[1], 1);
$c = round($values[2], 1);
$delta = ($b * $b) - (4 * $a * $c);

if($delta <= 0 || $a == 0){
    echo "Impossivel calcular" . PHP_EOL;
} else{
    $r1 = (-$b + sqrt($delta))/ (2 * $a);
    $r2 = (-$b - sqrt($delta))/ (2 * $a);
    
    echo "R1 = " . round($r1, 5) . PHP_EOL;
    echo "R2 = " . round($r2, 5) . PHP_EOL;
}