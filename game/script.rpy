# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("lilgirl")
define s = Character("soldier")
define gk = Character("goodDude")
define dg = Character("lilgirldead")
define sg = Character("lilgirlsleeping")
define ek = Character("evilDude")
define gg = Character("guardgargoyle")
define agd = Character("angryGoodDude")
define ds = Character("deadsoldier")
define sc1 = Character("soldier copy")
define sc2 = Character("soldier copy 2")
define dek = Character("deadEvilKing")

# the game starts here.
label start:
scene bg scrool
scene bg choosing

menu:
    "side 1":
        jump light
    "side 2":
        jump dark

label light:
    scene bg light side scene 1
label dark:
    scene bg dark side scene 1
    #they choose light or dark side





    #if they choose the light side v
    
    scene bg light side scene 1 #js show nothing happens 
    play music "good castle intro.mp3"

    scene bg light side scene 2 #still walking
    play music "seeing the good castle.mp3"

    scene bg light side scene 3 
    # priest tells king hey i come to offer services and bro says bless 
    # my daughter bc shes sick. he goes looking for daughter 

    "You tell the King that you are here to offer your services as a priest."
    show good dude at right

    gk "G'day priest. I have use for your services. My daughter is ill. I beg you to bless her. 
    Save her, please."

    hide good dude


    scene bg light side scene 4 
    with fade
    #ends up here and gargoyle starts attacking. priest has to make 
    #decision to stay and call help or run away. if run away go back to scene one. 
    #bros a coward he failed. if call for help then the princess comes and 
    #tells the gargoyle to go away. priest and princess talk and bond

    "You are looking for the princess in the garden. She loves flowers."

    show guardgargoyle with moveinright
    
    gg "Bark Bark"
    gg "attack attack"

    menu: 
        "Call for help":
            jump saved
        "Run away":
            jump lose

    label saved:
        scene bg light side scene 4
        show guardgargoyle at right
        show lilgirl at left 
        g "Don't worry! I'll save you!"
        hide guardgargoyle
        "Wow. The princess is so kind and valiant. She's litttyy man."

        scene bg light side scene 5 #girl sleeping and bro sneaking up...he 
    #has to bless princess and say can she have long healthy life rid 
    #of sickness etc etc. rbos got a mental debate. kill innocaent child 
    #he bonded with or kill her. even if she dies of sickness hes 
    #still cutting her life even shorter.  
    show lilgirlsleeping at left
    "She's gonna die anyway right? So should I kill or let her die. Maybe I should actually bless her. 
    The princess is such a fire person bro should be blessed."


    scene lightning sleep #lightning flash
    pause 1.0
    
    scene bg light side scene 5 #kill or not killl 
    
    menu:
        "Kill her":
            jump dead
        "Spare her":
            jump youLose

    label dead:
        hide lilgirlsleeping
        scene bg light side scene 5
        show lilgirldead at left
        scene bg win
        hide lilgirldead
        play sound "you won.mp3"
        pause 5.0
        return

    label youLose:
        scene bg lose
        play sound "boohoo you failed.mp3"
        return
   
    label lose:
        scene bg lose
        play sound "boohoo you failed.mp3"
        pause 5.0
        return


   



    #if they choose the dark side v
    
    scene bg dark side scene 1

    scene bg dark side scene 2

    scene bg dark side scene 3 

    scene bg dark side scene 4 #lightning for one sec

    scene bg dark side scene 3

    scene bg dark side throne scene

   
return: