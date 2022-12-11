<?php

$days = readline('');

echo (int)($days / 365) . ' ano(s)' . PHP_EOL;
$aux = ($days % 365);

echo (int)($aux / 30) . ' mes(es)' . PHP_EOL;
$aux = ($aux % 30);

echo (int)($aux / 1) . ' dia(s)' . PHP_EOL;