from cmu_graphics import *

def drawBackgroundImage():
    # Create the game window
    runGraphicsFunction(800, 600, myDrawFunction)

def myDrawFunction():
    # Load the background image
    backgroundImage = loadImage('figure/background1.png')

    # Draw the background image at the top-left corner of the window
    drawImage(backgroundImage, 0, 0)

    # Add other drawings or game elements here
    # ...

# Call the function to create the graphics window
drawBackgroundImage()
