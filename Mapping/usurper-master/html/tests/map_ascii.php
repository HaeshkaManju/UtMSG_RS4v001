<?PHP
require_once '/var/www/classes/map/map.class.php';
$map = new map();
?>
<html>
<body>
<style>
body {
	color: #CCC;
	background-color: #000;
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
<?PHP

$map->build();
echo $map->draw();

?>
</body>
</html>
