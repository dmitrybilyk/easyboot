<?php
$n = $i = $_GET['count'] ?? 5;
echo '<pre>';
while ($i--) {
    echo str_repeat(' ', $i).str_repeat('* ', $n - $i)."\n";
}
echo '</pre>';