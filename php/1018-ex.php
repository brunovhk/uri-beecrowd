<?php

$notes = readline('');

echo $notes . PHP_EOL;

echo (int)($notes / 100) . ' nota(s) de R$ 100,00' . PHP_EOL;
$aux = ($notes % 100);

echo (int)($aux / 50) . ' nota(s) de R$ 50,00' . PHP_EOL;
$aux = ($aux % 50);

echo (int)($aux / 20) . ' nota(s) de R$ 20,00' . PHP_EOL;
$aux = ($aux % 20);

echo (int)($aux / 10) . ' nota(s) de R$ 10,00' . PHP_EOL;
$aux = ($aux % 10);

echo (int)($aux / 5) . ' nota(s) de R$ 5,00' . PHP_EOL;
$aux = ($aux % 5);

echo (int)($aux / 2) . ' nota(s) de R$ 2,00' . PHP_EOL;
$aux = ($aux % 2);

echo (int)($aux / 1) . ' nota(s) de R$ 1,00' . PHP_EOL;
