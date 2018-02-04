__author__ = 'student'
# Event Markers
res1 = False
res2 = False
glow = False
bus1 = False
bus2 = False
sc1 = False
cct1 = False
printed = False
stapled = False
gotphone = False
hardmode = False

# Potential Achievements
Wrote_Exam = False
Wrote_Exam_desc = "Managed to write the exam! +750"
Helping_hand = 0
Helping_hand_desc = "Helped others everywhere possible! +1000"
Professional_crammer = 0
Professional_crammer_desc = "Somehow managed to cram in at least 10 minutes of study time! +1000"
Over_prepared = False
Over_prepared_desc = "Brought two cheat sheets and extra supplies to the exam room! +1250"
Punctual = False
Punctual_desc = "Ready for the exam before 7pm! +1250"
Healthy_Eater = True
Healthy_Eater_desc = "Did not consume sweets at all! +1500"
Survivalist = True
Survivalist_desc = "Made it through the evening without a jacket! +1500"
Talkative = 0
Talkative_desc = "Talked to everyone possible! +2000"
Tour_Guide = False
Tour_Guide_desc = "Explored every corner of UTM +2500"
Multitasker = False
Multitasker_desc = "Unlocked all the achievements! +3000"

# Actual Events / Story Text
def glow_event():
    '''
    :return: True or False if player went through the full event
    '''
    print("You decide to follow that glowing light in the forest. It leads you deeper and deeper into the forest.")
    choose = input("Would you like to still follow it? (yes / no)")
    choose.lower()
    if choose == "yes":
            print("The light is getting brighter and brighter as you move closer. You start to feel uneasy.")
            choose1 = input("Would you like to still follow it? (yes / no)")
            if choose1 == "yes":
                    print("It seems like the light is coming from the ground in the clearing in front of you. As you move closer \n"
                          "to investigate, the object emitting the light becomes more visible. It is a phone; it is Ned's phone,\n"
                          "the top student in the class! You should return it to him ASAP")
                    return True
    print("It seems a bit odd to follow a weird light in the middle of the forest this late. You decide to return\n"
          "back onto the path.")
    return False

def Bus_Stop1():
    '''
    :return: True or False if player went through the full event
    '''
    print("You wave at Jessica to get her attention as you enter the bus shelter. She smiles excitedly as she sees you\n"
          "and pulls something out...\n"
          "It is your T-Card! She explains that when you two went to study together, your T-Card must have gotten mixed\n"
          "up with her things. You're just glad that you have it back now.")

def Bus_Stop2():
    '''
    :return:
    '''
    print("You approach the bystander and tell him about your situation. He replies with the only hope for you is the\n"
          "advanced locker in Davis. Legend says that it's contents always give you exactly what you need. Intrigued,\n"
          "you ask for the code, which he unfortunately doesn't know. He heard that the code is a combination of 2\n"
          "words and a face, whatever that means. As you walk away, you have even more questions, but those won' do\n"
          "any good now.")

def Bus_Times():
    '''
    :return:
    '''
    print("110-S:\n"
          "...\n"
          "4:57\n"
          "5:45\n"
          "6:30\n"
          "7:11\n"
          "7:49\n"
          "...")

def Bus_Search():
    '''
    :return:
    '''
    print("After thoroughly searching around the bus stop and its shelters for 5 minutes, you have nothing to show for it.\n"
          "Nothing is here. Maybe you can try again and if there's still nothing here, then searching more will do no good.\n"
          "Even so, you feel something of value could be here.")

def SC_1():
    '''
    :return:
    '''
    print("You go and ask the group of boys about this special locker they are talking about. Apparently it's in one of\n"
          "the Davis Halls and sticks out considerably. They heard that the password is apparently a 10-character combination\n"
          "with regular and special characters. They never were able to guess the locker code. Maybe you can try.")

def SC_2():
    '''
    :return:
    '''
    print("You go and attempt to talk or even get the attention of the Foosball Players, but they are too engrossed\n"
          "in their game to even notice you. What a waste of time. You can't be wasting time right now.")

def SC_3():
    '''
    :return:
    '''
    print("As you near the musicians' room, you look through the glass wall to a table on the other side, and you see\n"
          "half a piece of paper, with your name on it. It's half of your cheat sheet! As you try and enter, one girl\n"
          "inside stops you at the doorway and asks for the password. You try to explain you only want a piece of paper\n"
          "but she is having none of it. She says to get in, you must fill in the blanks to a song she gives you.")
    choose = input("Do you take her up on her offer? (yes / no): ")
    if choose == "yes":
        print("~ever since I left the ____")
        choose1 = input("What's the lyric?: ")
        if choose1 == "city":
            print("~____ places where you don't belong")
            choose2 = input("What's the lyric?: ")
            choose2 = choose2.lower()
            if choose2 == "going":
                print("____ ____ ____ call me on my cellphone")
                choose3 = input("What's the lyric?: ")
                choose3 = choose3.lower()
                if choose3 == "you used to":
                    print("I know ____ ____ ____ ____")
                    choose4 = input("What's the lyric?: ")
                    choose4 = choose4.lower()
                    if choose4 == "when that hotline bling":
                        print("The girl is pleasantly surprised with your musical prowess and gives you access to the room.")
                        return True
        print("She is not pleased with your lyrics and slams the door in your face! If you could just find out the lyrics,\n"
              "you could be close to getting your cheat sheet.")
    return False

def KC_1():
    '''
    :return:
    '''
    print("You approach Mike and after exchanging greetings, you tell him your predicament. He reminds you that you spent\n"
          "a lot of time at the Library and around Davis yesterday, so those should be the best places to start. He also\n"
          "said that you should keep notes of whatever happens as it can lead you to figure out where everything is.\n"
          "You thank him for the advice and you two part ways.")

def K_Search():
    '''
    :return:
    '''
    print("There are notes strewn all over the place. Whoever was here last should have definitely cleaned up. You can read\n"
          "some of these notes if you're curious. You'll take whatever assistance you can get.")
    choose = input("Read notes? (yes / no)")
    while choose == "yes":
        choose1 = int(input("Which one? (1, 2, 3, 4, 5)"))
        if choose1 == 1:
            print('This one reads: "Good luck, gud luck, G00D luck! :)" Huh. Odd.')
        elif choose1 == 2:
            print('This neatly written one reads: "To whomever finds these, these were written for your encouragement!\n'
                  'We all need it in exam season! Good luck friend! - XOXO :)" That one is the most normal one so far.')
        elif choose1 == 3:
            print("This one is a picture of a star on top of a 4-leafed clover. There is a huge letter U beside the\n"
                  "clover. And a smiley face is in the corner of the page too. What does this all mean?")
        elif choose1 == 4:
            print('This one has stars (*) everywhere. It reads: "*You have 00 chance of failing!* ->U<- are gonna be\n'
                  'a *! Rock that exam!" You feel like these people are just messing with you now.')
        elif choose1 == 5:
            print("This one isn't even a note. This is a complex origami contraption of... a door? A locker? A fridge?\n"
                  "There's also a smiley face drawn on the front of this thing. Is this all some sort of practical joke?\n"
                  "You don't really know at this point. You stopped asking questions a while ago. It looks nice though.")
        choose = input("Keep Reading Notes? (yes / no)")
    print("You decide to leave this messy room.")


def CPathway():
    '''
    :return:
    '''
    print("You go up to the musical dude and jam out with him to his music. You even sing along:\n"
          "~Ever since I left the city\n"
          "~You got a reputation for yourself now\n"
          "~Everybody knows and I feel left out\n"
          "!Girl you got me down, you got me stressed out...\n")
    choose = input("Keep Listening? (yes / no)")
    if choose == "yes":
        print("~You used to call me on my cell phone\n"
          "~Late night when you need my love\n"
          "~Call me on my cell phone\n"
          "~Late night when you need my love...\n")
        choose1 = input("Keep Listening? (yes / no)")
        if choose1 == "yes":
            print("~Ever since I left the city, you, you, you\n"
            "~You and me we just don't get along\n"
            "~You make me feel like I did you wrong\n"
            "~Going places where you don't belong...\n")
            choose2 = input("Keep Listening? (yes / no)")
            if choose2 == "yes":
                print("~And I know when that hotline bling\n"
                "~That can only mean one thing\n"
                "~I know when that hotline bling\n"
                "~That can only mean one thing...\n")
                choose3 = input("Keep Listening? (yes / no)")
                if choose3 == "yes":
                    print("Ok this is getting out of hand. Did you forget you have an exam to write?")


def CCT_1():
    '''
    :return:
    '''
    print("You go and talk to Ned, but before you get to explain your problem, he explains his own problem. He lost \n"
          "his new gadget somewhere outside and he is extremely upset. You can't make any progress with him until he \n"
          "has that thing back in his hands.")

def CCT_2():
    '''
    :return:
    '''
    print("You go and return Ned's lost gadget to him. He is overjoyed and in his joy, he gives you some extra notes \n"
          "he made for the CSC108 exam, without you even asking for it. You ask him about the odd locker in Davis and \n"
          "he says that by his calculations, it is 99% probable that the lock setter used two of the same character at one point, to \n"
          "try and throw people off. He also theorizes that the code could be a popular saying. You thank him for advice  \n"
          "and continue on your adventure.")

def DavisHalls():
    '''
    :return:
    '''
    print("There's nothing here.")

def O_Locker():
    '''
    :return:
    '''
    print("When no one is looking, you run up to the locker and open it up. What you find inside is no T-Card, binder,\n"
          "notes or any school related stuff. It is instead a huge stash of good looking candy canes. I guess someone was getting\n"
          "into the holiday spirit pretty early. You decide to take one; who's gonna notice that one is missing?")

def Adv_Locker():
    '''
    :return:
    '''
    print("So this is the locker that has been rumored to be on campus. The locker itself really isn't all that special, but"
          "there is a big smiley face on it. That does seem pretty weird. Who does this thing belong to? As for the lock,\n"
          "it is a totally different story It looks like something out of a sci-fi movie. As you put your hand near it, "
          "a keyboard flips out from the front of the locker and the screen on the lock lights up.")
    choose = input("Try to open it? (yes / no)")
    while choose == "yes":
        code = input("ENTER CODE:")
        if code == "G00DL*CK:)":
            print("ACCESS GRANTED")
            print('Something inside the lock clicks and now you can open it. Inside, you do not find any of your supplies,\n'
                  'but see an amazing, cozy-looking winter coat with note attached. The note reads "Congratulations! You are the\n'
                  'first test subject of this locker designed to give students their greatest desires! Take the jacket please! :)"'
                  'You do not ask any questions and take it with you. Now you can roam outside for as long as you want!')
            return True
        else:
            print("ACCESS DENIED")
            choose = input("Try again? (yes / no)")
    print("You decide to leave this complex locker for now.")
    return False


def Caf_1():
    '''
    :return:
    '''
    print("Your friends are all gathered around one table, discussing the upcoming CSC108 exam. You tell them about\n"
          "how you lost all your things and they all offer some helpful bits of information. Josh says that maybe it's\n"
          "a good idea to sometimes re-enter places you've already visited later. Things could have moved back. Olivia\n"
          "adds that when she lost something, she recorded EVERYTHING that she observed inside her notebook. It helped\n"
          "lead her to the lost possessions. Finally, Mo suggests that it doesn't hurt to check new places. Even if you're\n"
          "sure you weren't at that location yesterday, perhaps someone took your items there. With these things in mind,\n"
          "you continue your search.")

def Caf_Search():
    '''
    :return:
    '''
    print("As you are scouring through the tables, you get odd glances from the janitor. Unfortunately, there's nothing\n"
          "of significance here.")

def P_Lot_1():
    '''
    :return:
    '''
    print("You go to grab your lucky pen, but Dave snatches it first. He says he is feeling nice today and will give\n"
          "the pen back to you, but there's a catch. He said he lost 3 textbooks somewhere in IB, Davis and Kaneff.\n"
          "You reluctantly agree to his terms.")

def LibF1_1():
    '''
    :return:
    '''
    print("You go to grab your lucky pen, but Dave snatches it first. With a smirk he that says he is feeling generous today and will give\n"
          "the pen back to you, but there's a catch. He said he lost 3 textbooks somewhere in IB, Davis and the Library. You already\n"
          "know where this is going and reluctantly agree to his terms of the trade.")

def LibF1_2():
    '''
    :return:
    '''
    print("You return with all 3 textbooks in hand and return them to Dave. He then tosses your pen to you. That actually went\n"
          "smoother than you thought it would.")

def LibB_1():
    '''
    :return:
    '''
    print("You see your CSC108 classmate Brandon sleeping in one of the cubicles. As the good friend you are, you go and \n"
          "try to wake him up. He sluggishly glances at his wristwatch. Once he sees the time, he packs up all his things and\n"
          "dashes to IB. Good thing you were here, right?")

def LibZ_1():
    '''
    :return: True or False if the player picked up the textbook
    '''
    print("After searching for a while... you find a Sociology Textbook in one of the cubicles.")
    choose = input("Pick it up? (yes / no)")
    if choose == "yes":
        return True
    return False

def LibZ_2():
    '''
    :return:
    '''
    print("After searching for a while, there's nothing useful here.\n")

def LibF3():
    '''
    :return:
    '''
    print("As you approach Lauren, she notices you and frantically gestures for you to come closer. She tells you about her horrible day;\n "
          "she lost her water bottle, lost her newest necklace, needs a hot coffee, needs an Iphone charger, etc. She's already sent "
          'people out on these "missions" and she tasks you with a lost Psychology textbook in Davis. Like the other 100 times\n'
          'you helped her in the past, she promises that she owes you big time. Although you have not gotten anything back till\n'
          'this day, it would not hurt to help someone in need.')

def LibF4_1():
    '''
    :return:
    '''
    print("Brian says that his dog tore the paper in half last night and he lost the top half around the student centre. \n"
          "That would sound pretty ridiculous to another person, but you know this is just typical for Brian.")

def IB110_1():
    '''
    :return:
    '''
    print("You tell her your situation and she immediately hands you her USB. She says that she has a cheat sheet on\n"
          "there. Kristina says that you can just return it to her tomorrow, and you should get the cheat sheet printed\n"
          "ASAP.")

def IB120_1():
    '''
    :return:
    '''
    print("Jessica runs to you and tells you that she's been trying to reach your cellphone all day. She has your T-Card!\n"
          "It must have gotten mixed up with her things when you were studying together yesterday.")

def IB120_2():
    '''
    :return:
    '''
    print("Jessica tells you that everything is going to be OK. You shouldn't really be shaking anyway. You've studied\n"
          "extremely hard for this exam.")

def IB120_3():
    '''
    :return:
    '''
    print("You approach Sheldon who is digging through his bag for something. He says he lost his proofs textbook\n"
          "somewhere in Deerfield. Maybe you can be a nice person and find it for him.")

def IB_Rooms1():
    '''
    :return:
    '''
    print("This is just an empty room. Nothing else is here.")

def IB_Rooms2():
    '''
    :return:
    '''
    print("There is one girl studying in this room. Better not disturb her. Other than that, nothing else is here.")

def IB_Rooms3():
    '''
    :return: True or False if the player picked up the textbook
    '''
    print("After searching for a while... you find an Anthropology Textbook under one of the chairs.")
    choose = input("Pick it up? (yes / no)")
    if choose == "yes":
        return True
    return False

def Computer1():
    '''
    :return:
    '''
    print("You find the nearest computer, slam in the USB and print off Kristina's Cheat Sheet!")

def Computer2():
    '''
    :return:
    '''
    print("Now's not really the time to be using a computer.")

def Stapler1():
    '''
    :return:
    '''
    print("Just what you needed! You staple the two halves together to put the sheet back together (mostly)!")

def Stapler2():
    '''
    :return:
    '''
    print("You don't really have anything to staple...")

def HolePuncher():
    '''
    :return:
    '''
    print("You don't really have anything to hole punch...")

def CellPhone():
    '''
    :return:
    '''
    print("You had some messages sent to you while your phone was charging.")
    choose = input("Check recent texts? (yes / no)")
    while choose == "yes":
        choose1 = input("Which one? (unknown, jessica, steve)")
        choose1 = choose1.lower()
        if choose1 == "unknown":
            print('"L*CK!" Who is this and how did this person get your number? This message is even stranger.')
        elif choose1 == "jessica":
            print('"Hey! You forgot your T-Card w/ me yesterday! I will be at bus stop around 5:45 and in the exam room at 6:30!\n'
                  'When you want to, come grab it!"')
        elif choose1 == "steve":
            print('"yo do u know what day the comp sci exam is?" Oh, good old Steve. Never change bro. \n')
        choose = input("Check recent texts? (yes / no) ")
    print("You put your phone in your pocket.\n")

def Write_Exam():
    '''
    :return:
    '''
    print("You have everything, but there is still a little bit of time until 7:10.")
    choose = input("Do you need anything else before you write? (yes / no) ")
    if choose == "yes":
        print("What an evening it's been! You never thought you would have made it to this moment. The only thing left\n"
              "to do tonight is write that exam!")
        return True
    print("You still have some time, but don't forget to return!")
    return False