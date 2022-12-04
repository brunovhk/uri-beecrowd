<?php

$time = readline();
$hours = floor($time / 3600);
$minutes = floor($time / 60) % 60;
$seconds = $time % 60;

echo $hours . ':' . $minutes . ':' . $seconds . PHP_EOL;
