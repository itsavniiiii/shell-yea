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


    scene bg lightning sleep #lightning flash
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
    
    

label darkSide:  
    scene bg dark side scene 1
    show s
    s "Halt! State your business trespasser"

    menu:
        "Draw your sword":
            jump fight
        "Explain yourself":
            jump explain


    label fight:
        "You draw your sword"
        s "You will perish like those before have, those who dared challenge our great king."
        "You fight"
        "The soldier is young, inexperienced, overconfident. You side step his blows, and plunge your sword deep into his chest. He falls."
        hide s
        "He looks younger in death somehow. He had to be eighteen? Nineteen? He couldn’t have a wife or kids to miss him, but did he have a beloved, someone he hoped to marry some day?"
        "No matter. He was dead now."
        jump DarkSideScene2


    label explain:
        "You say you’re here to offer your services as a priest of Qhuarae."
        s "We have no use for you here. Turn back or I will remove you from the land of our lord myself."
        menu: 
            "Run":
                jump RunFromSolider
            "Draw your sword":
                jump fight
    label RunFromSoldier:
        "You turn and flee"
        scene bg lose
        return




    label DarkSideScene2:
        scene bg dark side scene 2
        show s
        s "Turn back trespasser or you will meet the same fate as those before you."
            menu: 
                "Run":
                    jump RunFromSolider2
                "Draw your sword":
                    jump fight2
    label RunFromSoldier2:
        "You turn and flee"
        scene bg lose
        return
	
    label fight2:
        "You draw your sword"
        s "Very well. You cannot say I did not offer mercy."
        "This soldier is older, more experienced. His jabs have none of the unnecessary flourish of the rookie. He actually manages to cut your shoulder, but it is shallow."
        "While he is still close you slash across his chest. He falls."
        hide s
        show ds
        "As you watch his blood drain with light from his eyes, you notice something."
        "The wedding band glints in the darkness, splattered with blood."
        "You tear your eyes away. It doesn’t matter now."
        hide ds


 
    scene bg dark side scene 3
    show s
        menu:
            "Fight":
                jump fight3
            "Let him speak":
                jump LetHimSpeak
	
    label fight3:
        "You lunge forward."
        "The soldier stumbles back in surprise. You thrust your sword into his chest. He dies."
        hide s
        show ds
        pause 1.0
        hide ds
        "Your chest heaves, and you’re breathing hard from the battles. You’ve killed three men. You stumble back from the weight of the fact. You killed three people. One barely a man. One married. And one who didn’t even get the chance to defend himself."
        "Three lives lost just to kill one more. Wasn’t it enough? Their sacrifices for their King, while misguided, were noble. Shouldn’t it count for something? Shouldn’t it stop here?"
        jump DarkSideScene4


    label LetHimSpeak:
        s "You have raised your sword against the soldiers of our Lord, and thus you are an enemy of this kingdom."
        "He lunges."
        "You fight. He sees your bleeding shoulder and underestimates you. A deadly mistake."
        "You tear a gash into his thigh and he falls. You stand over him, sword raised." 
        s "No! Please spare me! My sister is very sick! If I die there will be no one to take care of her! You’ll have killed her too!" 
            menu:
                "Spare him":
                    label spare
                "Kill him":
                    label kill
    label spare:
        "You lower your sword."
        pause 0.5
        "Leave."
        s "Thank you—thank you."
 			"The soldier runs away."
            hide s
            "Your chest heaves, and you’re breathing hard from the battles. You’ve killed two men. You stumble back from the weight of the fact. You just killed two people. One barely a man. One married."
            "Two lives lost just to kill one more. Wasn’t it enough? Their sacrifices for their King, while misguided, were noble. Shouldn’t it count for something? Shouldn’t it stop here?"
            scene bg dark side scene 4
                pause 0.5
            scene bg dark side scene 3
                pause 0.5
                "No. Their deaths will not be in vain. You came to ride their kingdom of this tyrant, and redeem your soul. You even spared one soldier from the bloodshed."
            scene bg dark side throne scene
                show s at left
                show sc1 at center
                show sc2 at right
                s "CHARGE!!"
                "The soldier you spared ratted you out. The army kills you."
                hide s
                hide sc1
                hide sc2
            scene bg lose
        label kill:
            "You slash open his chest."
            hide s
            show ds
            pause 0.5
            hide ds
            "Your chest heaves, and you’re breathing hard from the battle—well, battles. You’ve killed three men. You stumble back from the weight of the fact. You killed three people, really four. One barely a man. One married. One with a family to care for. And his sickly sister will be dead soon too."
        "Fours lives lost just to kill one more. Wasn’t it enough? Their sacrifices for their King, while misguided, were noble. Shouldn’t it count for something? Shouldn’t it stop here?"
            jump DarkSideScene4


label DarkSideScene4:
    scene bg dark side scene 4 #lightning for one sec
        pause 0.5
    scene bg dark side scene 3
        pause 0.5
        "No. Their deaths can not be in vain. You came to rid their kingdom of this tyrant, and redeem your soul. There was no turning back."


    scene bg dark side throne scene	
    show ek
    ek "Ah, it seems the gods have sent another champion to slay me. A vain hope."
    ek "Sir Xalvador of Lord Rhihdes, Sire Raolin of Lady Cesnos, Lady Topaz of Lord Therdis, I killed them all."
    ek "So why dear /’champion’/ do you think you can do what they couldn’t?"
    ek "What makes you so special that you will be able to even attempt slaying the greatest king of all the land, the greatest warrior on both sides of the sea?" 
    ek "How dear champion do you plan to slay the greatest—"
    "You run up and plunge your sword into his chest."
    hide ek
    show dek
    "The force of the blow tips him over, and he falls, your sword still buried in his chest."
    pause 1.0
    hide dek
"You’re breathing hard, heart bounding, blood roaring in your ears. Is this what it feels like? How it feels to redeem your own soul? The blood is still wet on your hands, slick like oil. Your legs shake, knees buckling. Your stomach heaves, your tongue goes dry as bile rises in your throat. The room whirls around you, like the sun watching the world spin.You speak to the crowned corpse at your feet."
    "I am no champion."
    scene bg win
    return

