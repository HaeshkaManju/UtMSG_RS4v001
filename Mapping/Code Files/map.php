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
}
.tagline {
	font-family: 'New Rocker', cursive;
	position: absolute;
	font-size: 24pt;
	top: 655px;
	left: 200px;
	color: #CCC;
}
.title {
	font-family: 'Bahiana', cursive;
	color: #F42;
	font-size: 48pt;
	margin-bottom: 5px;
	position: absolute;
	top: 650px;
	left: 45px;
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
<div style="position:relative" id="map-outer-container">
	<img src="/images/map/Map_Frame_no_Background.png" style="position:absolute; width:650px; height: 650px;" />
	<div style="position:relative; top: 0px; left: 20px;" id="map">
<?PHP

$map->build();
echo $map->draw('graphical');

?>
	</div>
	<span class="title">usurper</span>
	<span class="tagline">The Medieval Strategy Game</span>
</div>
</body>
</html>
