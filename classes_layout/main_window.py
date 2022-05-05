from tkinter import *
# This is an import developed SEPARATELY from tkinter to resolve a mac bug.
from tkmacosx import Button
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
# Top-Center (Full Width) Frame Area
###############################################################################

top_frame = Frame(
    root,
    bg = "red",
    width = settings.win_width,
    height = settings.height_prct(15)
)
# You have to "place" a frame.  It "exists", but is essentially inaccessible,
## in a visibility sense.
top_frame.place(x = 0, y = 0)

###############################################################################
# Left-Side, Navigation Bar Frame Area
###############################################################################
nav_frame = Frame(
    root,
    bg = "yellow",
    width = settings.width_prct(20),
    height = settings.height_prct(85)
)
# Place the Frame.
nav_frame.place(x = 0, y = settings.height_prct(15))

###############################################################################
# Mid, Wide-Area, Proportionate Scaling "Main View" Frame Area
###############################################################################
main_frame = Frame(
    root,
    bg = "blue",
    width = settings.width_prct(80),
    height = settings.height_prct(85)
)
# Place the Frame.
main_frame.place(x = settings.width_prct(20), y = settings.height_prct(15))


# Yeah, I don't know what this ACTUALLY does.
## It *seems* to run similar to the __init__ magic method of main, but...
### I don't actually know.
root.mainloop()
