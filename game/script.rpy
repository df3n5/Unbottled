# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define man = Character("Man", image="man")
#image side man = "man.png"

image side man = ("man.png")
define man = Character("Man", image="man")

image side woman = ("woman.png")
define woman = Character("Woman", image="woman")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hospital_room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show man

    # These display lines of dialogue.

    #"Hello, world."

    man "You've created a new Ren'Py game."

    #man "Once you add a story, pictures, and music, you can release it to the world!"
    woman "Hello"

    # This ends the game.

    return
