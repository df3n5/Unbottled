# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define man = Character("Man", image="man")
#image side man = "man.png"

image side man = ("man.png")
define man = Character("Man", image="man")

image side woman = ("woman.png")
define woman = Character("Woman", image="woman")

image side dr = ("dr.png")
define dr = Character("Doctor O'Sullivan", image="dr")

define question = Character("???")
define me = Character("Me")

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

    #man "You've created a new Ren'Py game."

    #man "Once you add a story, pictures, and music, you can release it to the world!"
    #woman "Hello"

    #dr "Hello"

    me "Hello?"

    question "Hello?"

    question "Can you hear me?"

    me "Yes"

    question "That's good. My name is Doctor O'Sullivan, you're in St. Patrick's hospital."

    me "I can't see you, where are you?"

    dr "I am afraid to say that you've been in a car accident."

    dr "You have sustained injuries to your head and a large part of your body."

    dr "It appears as if your sight has been damaged. Whether that is permanent or not."

    dr "I am afraid the damage to your body is very severe."

    dr "We have given you medication for the pain. If we don't see improvement in the next few hours we will have to consider some more extreme measures."

    me "..."

    menu:
        "Am I going to die?":
            dr "Woah, we're not at that stage yet. But I am going to need you to fight hard for the next while."

            me "Doctor, please. I can take it."

            dr "Well, I have never seen a patient recover fully from damage that you have sustained. To be honest, I am shocked you are coherent right now."
        "Thanks doctor.":
            dr "No problem!"

    dr "Your husband is waiting outside for you."

    me "Ex-husband"

    dr "Ah okay! Would you like to see him?"

    me "Sure."

    # This ends the game.

    return
