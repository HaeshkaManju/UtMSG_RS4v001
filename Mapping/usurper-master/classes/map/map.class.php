<?PHP

class map {

	var $map_settings, $map, $tile_count, $tile_list, $grid;
	var $placed_tile_count, $terrains_by_sequence;

	function __construct ( $settings = '' ){
		$this->load_settings( $settings );
	}

	function get_settings () {
		return $this->map_settings;
	}

	private function draw_ascii () {
		// Ok, later we will make this json, but for now let's just spit it out!
		$html = '<table class="ascii-map"><tr>';

		// Build row by row (so Y loop is first, don't let that confuse you though)
		for ( $y=0; $y<=$this->map_settings->height; $y++ ) {
			// Build column by column ( X )
			for ( $x=0; $x<=$this->map_settings->width; $x++ ) {
				if ( $x == 0 ) { // First column
					if ( $y == 0 ) { // First row (the empty top-left corner)
						$html .= '<th>&nbsp;</th>';
					} else { // Not the first row, but still the first column
						$html .= '<th>' . $y . '</th>';
					}
				} else if ( $y == 0 ) { // Header row
					$html .= '<th>' . $this->to_alpha ( $x - 1 ) . '</th>';
				} else { // Normal cell
					$terrain_name = $this->grid[$x][$y];
					$html .= '<td style="color: ' . $this->map_settings->terrains->$terrain_name->color  . '">' 
						. $this->map_settings->terrains->$terrain_name->ascii . '</td>';
				}
			}
			$html .= '</tr><tr>'; // Cycle the row
		}

		// Ok close the table and spit the html out.
		$html .= '</tr></table>';

		return $html;
	}

	private function draw_graphical () {
		// Ok, later we will make this json, but for now let's just spit it out!
		$html = '';

		// Build row by row (so Y loop is first, don't let that confuse you though)
		for ( $y=1; $y<=$this->map_settings->height; $y++ ) {
			// Build column by column ( X )
			for ( $x=1; $x<=$this->map_settings->width; $x++ ) {
				$terrain_name = $this->grid[$x][$y];
				$tile_offset_x = $this->map_settings->tile_offset_x * $x;
				$tile_offset_y = $this->map_settings->tile_offset_x * $y;
				$html .= '<img style="position:absolute; top:' . $tile_offset_y
				       . '; left: ' . $tile_offset_x . '; width: ' 
				       . $this->map_settings->tile_size . '; " src="/images/terrain/' 
				       . $this->map_settings->terrains->$terrain_name->image . '">';
			}
		}

		return $html;
	}

	function draw ( $mode = 'ascii' ) {

		switch ( $mode ) {
			case 'graphical' :	
				$out = $this->draw_graphical();
				break;

			default :
				$out = $this->draw_ascii();
		}

		return $out;
	}

	function to_alpha ( $num ) {
		$alphabet = range('A', 'Z');

		return $alphabet[$num];
	}
	
	function roll ( $d=100, $tn=50 ) {
		$dice = rand(1, $d);
		
		if ( $dice >= $tn ) {
			return true;
		} else {
			return false;
		}
	}

	function roll_probability ( $probability ) {
		$tn = 100 - $probability;
		
		return $this->roll( 100, $tn );
	}

	function calc_single_md ( $vector1, $vector2 ) {
		$n = count($vector1);
		$sum = 0;
		for ($i = 0; $i < $n; $i++) {
		    $sum += abs($vector1[$i] - $vector2[$i]);
		}
		return $sum;
	}

	function calc_manhattan_distances ( $origin_coords ) {
		// We need to build the grid with distances as values
		for ( $y=1; $y<=$this->map_settings->height; $y++ ) { 
			for ( $x=1; $x<=$this->map_settings->width; $x++ ) { 
				$d = $this->calc_single_md($origin_coords, array($x, $y));
				$neighbors[$d][] = $this->grid[$x][$y];
			}   
		}

		return $neighbors;
	}			

	function find_open_spot () {
		$found = false;
		$loop_count = 0;

		while ( !$found ) {
			// Choose x spot
			$x = rand(1, $this->map_settings->width);

			// Choose y spot
			$y = rand(1, $this->map_settings->height);
			
			// Check to see if that spot is open
			if ( $this->grid[$x][$y] == false ) {
				$found = true;
			}

			if ( $loop_count >= ($this->tile_count * 10) ) {
				/* We picked randomly 10 times the number of existing slots
				 * and found nothing.  Let's fall back to walking the grid.
				 * If we still find nothing, then we die.
				 */
				for ( $y=1; $y<=$this->map_settings->height; $y++ ) {
					for ( $x=1; $x<=$this->map_settings->width; $x++ ) {
						if ( $this->grid[$x][$y] == false ) {
							$found = true;
							break 2; // Stop! we found one.
						 }
					 }
				 }

				// If still nothing, we are borked.
				 if ( !$found ) {
					 die ( 'Something horrible has happened. '
					     . "We were told to pick an empty spot and there isn\'t one!");
				 }
			}
		}
		
		$spot['x'] = $x;
		$spot['y'] = $y;
		
		return $spot;
	}
	
	function get_neighbor_tiles ( $spot, $distance, $diag_allowed = false ) {
		$x = $spot['x'];
		$y = $spot['y'];

		$origin_coords = array ( $x, $y );
		$list = $this->calc_manhattan_distances ( $origin_coords );

		/* Now we need to prune the list to only include stuff within the distance
		 * and while we are at it, let's flatten these down to a 2d array.
		 * Also, let's prune dupes, and ignore empty spots.
		 */
		for ( $d=1; $d<=$distance; $d++ ) {
			foreach ($list[$d] as $terrain) {
				if ( trim($terrain) != '' ){
					if ( isset($pruned_list) ) {
						if ( !in_array($terrain, $pruned_list) ) {
							$pruned_list[] = $terrain;
						}
					} else {
						$pruned_list[] = $terrain;
					}
				}
			}
		}

		if ( isset($pruned_list) ) {
			return $pruned_list;
		} else {
			return array ('');
		}
	}

	function smart_shuffle () {
		// Get a tile by placement sequence
		foreach ( $this->terrains_by_sequence as $terrain ) {
			$cur_terrain = $this->map_settings->terrains->$terrain;
			
			// Ok, we are going to place all tiles of this type.
			for ( $i=1; $i<=$cur_terrain->count; $i++ ) {
					
				// Clumping?
				if ( @$cur_terrain->clumping ) {
					$clump = true;
					
					// Roll to see if we ignore the clumping for this tile
					if ( $cur_terrain->clumping_probability == '') {
						die ( $terrain . ' clumping_probability not set' );
					}

					if (  !$this->roll_probability ( $cur_terrain->clumping_probability )) {
						$clump = false;	
					}

					/* Check for the presence of a like tile. If there isn't one on the board yet
					 * then clumping won't be possible.
					 */
					 if ( @$this->placed_tile_count[$terrain] < 1 ) {
						 $clump = false;
					 }
				} else {
					$clump = false;
				}

				if ( !$clump ) {
					
					// We don't have to clump, so just randomly pick an unused spot and plunk it down.
					$spot = $this->find_open_spot();

				} else {
					
					/* Have to clump up!  But we better count the attempts.
					 * If there are too many attempts, then we give up trying to clump
					 * and just place.
					 */
					$attempts = 0;
					$settled = false;

					while ( !$settled ) {
						$spot = $this->find_open_spot();
						
						// Let's get all tiles within the clump_distance
						$neighbors = $this->get_neighbor_tiles ( $spot, $cur_terrain->clump_distance );
						// Is this spot close enough to a like tile?
						if ( in_array($terrain, $neighbors ) ) {
							$settled = true;
						}
					}
				}
				
				$spotx = $spot['x'];
				$spoty = $spot['y'];
				$this->grid[$spotx][$spoty] = $terrain;
				 echo "<!-- $terrain placed on $spotx:$spoty -->\n";

				if ( isset($this->placed_tile_count[$terrain]) ) {
					$this->placed_tile_count[$terrain]++;
				} else {
					$this->placed_tile_count[$terrain] = 1;
				}
			}
		}
	}

	function init_grid () {
		for ( $y=1; $y<=$this->map_settings->height; $y++ ) {
			for ( $x=1; $x<=$this->map_settings->width; $x++ ) {
				$this->grid[$x][$y] = false;
			}
		}
	}

	function build () {
		// Set up the array of terrains
		// How many tiles are there
		$this->tile_count = $this->map_settings->width * $this->map_settings->height;

		// Intantiate the grid with false values for empty checking.
		$this->init_grid();

		// Ok, now get the terrains and counts for each
		$terrains = get_object_vars ( $this->map_settings->terrains );
		foreach ( $terrains as $terrain => $terrain_details ) {
			
			$count = $terrain_details->count;
			// is the count literal or a percentage?
			if ( substr($count, -1) == '%' ) {
				
				// Ok, it's a percentage, so let's convert to a literal.
				$fix_count = str_replace('%', '', $count);
				$terrain_count = $this->tile_count * ( $fix_count / 100 );
				$this->map_settings->terrains->$terrain->count = $terrain_count;
				$terrain_sequence = $terrain_details->placement_sequence;
				$this->terrains_by_sequence[$terrain_sequence] = $terrain;

			}
		}

		// Randomize the list
		$this->smart_shuffle ( );

	}
		

	private function load_settings ( $settings = '' ) {
		
		if ( $settings == '' ) { // No settings passed in, load defaults
			if ( !$settings = file_get_contents ( '/var/www/usurper/config/map/default.json' ) ) {
				die ( 'No settings present, and missing default config file.' );
			}
		}
		$this->map_settings = json_decode($settings);
	}

}
