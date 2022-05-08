<?PHP
function distance($vector1, $vector2)
    {
        $n = count($vector1);
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += abs($vector1[$i] - $vector2[$i]);
        }
        return $sum;
    }

$vector = array($_GET['x'],$_GET['y']);

//echo distance($vector, $neighbor);

for ( $y=1; $y<=10; $y++ ) {
	for ( $x=1; $x<=10; $x++ ) {
		$d = distance($vector, array($x, $y));
		echo str_pad($d, 3);
	}
	echo "\n";
}


?>
