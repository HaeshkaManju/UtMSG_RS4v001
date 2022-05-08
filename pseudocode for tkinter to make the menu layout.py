#! TKinter Pseudo-Code for Usurper


# Files:
## Main: contains the main loop, instantiates initial variables/values, and builds the base menu.
## Layout Class: class file that handles the parameters of the menu (i.e.: the UI.)
## Map Class: class file that handles the random generation of the game map, as well as info displayed.
## Settings file to handle things such as resolution, fonts, game difficulty, and other video driver parameters


# Root Frame
## Uses Resolution (height/width) from settings to create a WINDOW size.
## All other frames will fit into root and reference root.

# Top Frame.
## Displays the following information:
### Title of the Game Instance ("Multiplayer, Host IP, So and So's world.")
### Usurpation/Leader Name.
### Time: Turn/Week/Month/Year.
### Which Menu item is "up" in the main frame.
## Frame itself Is Static.  Does not change in size, shape, or composition.  Only in information displayed.
## Always occupies 95%-100% width. (Not sure what padding we will be using, but "full width")
## Always occupies some small amount (10%?) height.
## Always stay in the top of the window.

# Menu Frame.  (AKA: Left Frame)
