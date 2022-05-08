<?PHP
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require_once '/var/www/usurper/classes/map/map.class.php';
$map = new map();
?>
<html>
<body>
<style>
body {
	color: #CCC;
	background-color: #000;
	font-family: 'New Rocker', cursive;
}
h1 {
	font-family: 'Bahiana', cursive;
	color: #F42;
	font-size: 36pt;
	margin-bottom: 5px;
}
.ascii-map td {
	border-top: solid <?PHP echo $map->map_settings->grid->size; ?> <?PHP echo $map->map_settings->grid->color; ?>;
	border-left: solid <?PHP echo $map->map_settings->grid->size; ?> <?PHP echo $map->map_settings->grid->color; ?>;
}
.ascii-map {
	border: solid <?PHP echo $map->map_settings->grid->size; ?> <?PHP echo $map->map_settings->grid->color; ?>;
}
.ascii-map td {
	padding: 12px;
}
</style>
<link href="https://fonts.googleapis.com/css?family=Bahiana|New+Rocker" rel="stylesheet">
<h1>usurper</h1>
The Medieval Strategy Game<br />
<br />
<div style="position:relative" id="map-outer-container">
	<img src="/images/map/Map_Frame_no_Background.png" style="position:absolute; width:650px; height: 650px;" />
	<div style="position:relative; top: 0px; left: 20px;" id="map">
<?PHP

$map->build();
echo $map->draw('graphical');

?>
	</div>
</div>
</body>
</html>
