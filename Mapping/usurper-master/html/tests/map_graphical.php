<?PHP

require_once '/var/www/classes/map/map.class.php';
$map = new map();
$map->build();
$map->show('graphical');

?>
