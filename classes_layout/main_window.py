from tkinter import *
# This is an import developed SEPARATELY from tkinter to resolve a mac bug.
import settings

# Instantiate the main window, this is BY CONVENTION, called "root".
## I will continue to call the main  file "main_window"
### because I don't know if "root" is a reserved system word in tkinter.
root = Tk()
# configure is a tkinter method.
## "bg" is background color,
## but this works for FRAMES and WINDOWS, not Buttons. (MacOSX Issue)
root.configure()
# geometry is a tkinter method.
## f strings can substitute to create a settings parallel.
root.geometry(f"{settings.win_width}x{settings.win_height}")
# tkinter method to set the main window title (like a browser title)
## need to find out if there is a "favicon" method.
root.title("Usurper: the Medieval Strategy Game")
# this is "width by height" comma ordered.
root.resizable(False, False)

# Frame is a tkinter class.
# name your frame, this is how you can reference it in the future.
# Frame is capitalized like a class.
# When declaring a frame, you MUST declare its "relative" standing.
# If in the 'base', the standing is "root",
## If inside of another frame, call that frame's name instead.
### This will affect how ".place" and ".grid" function.

###############################################################################
#                    Top-Center (Full Width) Frame Area                       #
#                 This will be called the: Status Screen                      #
###############################################################################

# This frame should have two variations: Startup Screen and Gameplay Screen.
## Startup Screen: Display Large Text: "Usurper: the Medieval Strategy Game"
## Gameplay Screen: Display: Usurper Chief Name, Current Game Time, and
## either "Awaiting Orders", "Waiting on Game Engine", or "Awaiting Response."
### Awaiting Orders will indicate to player that they can take actions and
### make adjustments to their gear, etc.
### Waiting on Game Engine will put the player's ability to interact on hold
### while the game/narrator makes its/their updates.
### Awaiting Response will display after the game engine update to let the
### player know that they can respond to updates such as purchasing goods.
## Display the currently selected Menu Item.

top_frame = Frame(
    root,
    bg = "red",
    width = settings.win_width,
    height = settings.height_prct(15)
)
# You have to "place" a frame.  It "exists", but is essentially inaccessible,
## in a visibility sense.
top_frame.place(x = 0, y = 0)


########################
# Status Screen Labels #
########################

# Within the top_frame, there will need to be a Label to house the two Screens
startup_screen_label = Label(
    top_frame,
    activebackground = "white",
    activeforeground = "gray",
    anchor = "center",
    text="Usurper: the Medieval Strategy Game"
)
# Figure out how to Top-Center the label.
# This label should only be placed/visible if on Startup Screen.
startup_screen_label.place(x=650, y=0)

usurpation_top_label = Label(
    top_frame,
    activebackground = "Blue",
    activeforeground = "Yellow",
    anchor = "center",
    text="Chief Name: [], Week 1, Month 1, Year 1"
)
# 
usurpation_top_label.place(x=640, y=25)

game_status_label = Label(
    top_frame,
    activebackground = "White",
    activeforeground = "Gray",
    anchor = "center",
    text="Awaiting Orders"
)
game_status_label.place(x = 710, y = 50)


############################
# End Status Screen Labels #
############################
###############################################################################
#                 End Top-Center (Full Width) Frame Area                      #
#                 This will be called the: Status Screen                      #
###############################################################################



###############################################################################
#                   Left-Side, Navigation Bar Frame Area                      #
#                   This will be called the: Navigation Bar                   #
###############################################################################
nav_frame = Frame(
    root,
    bg = "yellow",
    width = settings.width_prct(20),
    height = settings.height_prct(85)
)
# Place the Frame.
nav_frame.place(x = 0, y = settings.height_prct(15))

#########################
# Navigation Bar Labels #
#########################

navigation_bar_label = Label(
    nav_frame,
    activebackground = "Gray",
    activeforeground = "Black",
    text = "Menu"
)
navigation_bar_label.grid(column = 0, row = 0)
#############################
# End Navigation Bar Labels #
#############################

#######################
# Navigation Bar Menu #
#######################

# The word "Menu" may not be necessary at all.

# The Menu should have all of the buttons LEFT justified.
# When a button is selected the following should occur:
## 1) Update that button to be PRESSED.
## 2) Update the Top_Frame, to contain the name of the Selected Menu Item,
### or "Usurper: the Medieval Strategy Game" as appropriate.
## 3) Update the Center View to host the information pertinent to that menu.

###########################
# End Navigation Bar Menu #
###########################

##########################
# Navigation Bar Buttons #
##########################

home_button = Button(
    nav_frame,
    text = "Main Menu"
)
home_button.grid(column = 1, row = 1)

usurpation_button = Button(
    nav_frame,
    text = "My Usurpation"
)
usurpation_button.grid(column = 1, row = 2)

lair_button = Button(
    nav_frame,
    text = "My Lair"
)
lair_button.grid(column = 1, row = 3)

orders_button = Button(
    nav_frame,
    text = "Orders"
)
orders_button.grid(column = 1, row = 4)

map_button = Button(
    nav_frame,
    text = "Map"
)
map_button.grid(column = 1, row = 5)

review_turn_results_button = Button(
    nav_frame,
    text = "Review Results"
)
review_turn_results_button.grid(column = 1, row = 6)
##############################
# End Navigation Bar Buttons #
##############################

###############################################################################
#                   End Left-Side, Navigation Bar Frame Area                  #
#                   This will be called the: Navigation Bar                   #
###############################################################################

###############################################################################
#         Mid, Wide-Area, Proportionate Scaling "Main View" Frame Area        #
#                   This will be called the: Main View                        #
###############################################################################
main_frame = Frame(
    root,
    bg = "blue",
    width = settings.width_prct(80),
    height = settings.height_prct(85)
)
# Place the Frame.
main_frame.place(x = settings.width_prct(20), y = settings.height_prct(15))

###############################################################################
#         Mid, Wide-Area, Proportionate Scaling "Main View" Frame Area        #
#                   This will be called the: Main View                        #
###############################################################################


# Yeah, I don't know what this ACTUALLY does.
## It *seems* to run similar to the __init__ magic method of main, but...
### I don't actually know.
root.mainloop()
