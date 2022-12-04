<?php

$money = round(floatval(readline()), 2);
$money += 0.001;

$notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00];
$coins = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01];

echo "NOTAS:" . PHP_EOL;

foreach ($notes as $note) {
    $qtyNotes = (int)($money / $note);
    echo $qtyNotes . " nota(s) de R$ " . number_format($note, 2) . PHP_EOL;
    $money = fmod($money, $note);
}

echo "MOEDAS:" . PHP_EOL;

foreach ($coins as $coin) {
    $qtyCoins = (int)($money / $coin);
    echo $qtyCoins . " moeda(s) de R$ " . number_format($coin, 2) . PHP_EOL;
    $money -= $qtyCoins * $coin;
}
