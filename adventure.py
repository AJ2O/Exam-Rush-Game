from game_data import World, Item, Location
from player import Player
import Events

# Executes the actions of the player
def do_action(World, PLAYER, location, choice):
    '''

    :param World:
    :param Player:
    :param Location:
    :param Choice:
    :return:
    '''

    if (choice == "[menu]"):
        print("Menu Options: \n")
        for option in menu:
            print(option)
        choice = input("\nChoose action: ")
        choice.lower()

    while choice in menu:
        if choice == "look":
            print(location.get_full_description())
        elif choice == "inventory":
            print("Your Inventory:")
            for i in PLAYER.inventory:
                print("\t" + i + ": " + World.items[i].desc)
            print('\n')
        elif choice == "score":
            print("Your score is currently " + str(PLAYER.score))
        elif choice == "notes":
            notechoice = input("What would you like to do? (read notebook / create note / back)")
            while notechoice != "back":
                if notechoice == "read notebook":
                    print("Your notes:")
                    for x in PLAYER.notes:
                        print("\t", x, "\n")
                else:
                    create = input("What would you like to note down?")
                    PLAYER.notes.append(create)
                notechoice = input("What would you like to do? (read notebook / create note / back)")
        elif choice == "help":
            print('''
            HELP

            Hypothermia:
            Since you don't have your jacket, this meter will fill up whenever you go outside or do an action
            outside. If it reaches level 4, you will be warned. If it reaches level 5, you dash all the way back
            to your residence for warmth. If you had a jacket though, this would not be a problem...

            Basic Commands:
            Commands are enclosed by a pair of "|"

            |quit|
            Quits the game

            |look|
            Describes in detail your current location

            |inventory|
            Displays your current inventory and each item's description

            |score|
            Displays your current score

            |go north| / |go south| / |go east| / |go west|
            Moves you around the map in the direction desired

            |lounge|
            Lounge around and don't do anything for 5 minutes.

            |use (item)|
            Uses an item from your inventory where "(item)" is replaced by a real item's name

            |drop (item)|
            Drops an item from your inventory into the current location where "(item)" is replaced by a real item's name

            |recover (item)|
            Picks up an item from the location where it was previously dropped where "(item)" is replaced by a real item's name
            and adds it to your inventory

            Additional commands are listed for each location under [menu]

            Ex. |warm up|
                Resets Hypothermia Meter to 0

            Ex. |study|
                Increases your score by 100

            There is a note taking feature simply accessed by typing in |notes| and it is extremely useful for recording clues that
            you may find around campus to lead you to your items. You can also read all the notes you have taken during
            the evening.

            Happy Playing! :)
            ''')
        choice = input("\nChoose action: ")
        choice.lower()

    # Basic Commands
    if choice[:2] == "go" and len(choice) > 3 and choice[3:5] != "to":
        c = choice.split()
        if c[1] == "west":
            PLAYER.move_west()
            timer(1)
        elif c[1] == "east":
            PLAYER.move_east()
            timer(1)
        elif c[1] == "north":
            PLAYER.move_north()
            timer(1)
        elif c[1] == "south":
            PLAYER.move_south()
            timer(1)

    elif choice == "lounge":
        print("You lounge around for 5 minutes.")
        timer(5)

    elif choice[:4] == "drop":
        dropped = False
        temp_inventory = PLAYER.inventory.copy()
        for stuff in temp_inventory:
            if stuff == choice[5:]:
                print("Dropped " + choice[5:] + " from inventory!")
                World.items[stuff].drop_loc = location.index
                PLAYER.remove_item(World.items[stuff])
                dropped = True
        if not dropped:
            print("This item does not exist in your inventory.")

    elif choice[:7] == "recover":
        recovered = False
        for things in World.items:
            if World.items[things].drop_loc == location.index and World.items[things].name == choice[8:]:
                if not PLAYER.weight + World.items[things].weight > 3:
                    print("Recovered " + choice[8:] + "!")
                    PLAYER.add_item(World.items[things])
                    World.items[things].drop_loc = -1
                    recovered = True
                else:
                    print("You can't carry that many textbooks!")
        if not recovered:
            print("This item does not exist at this location.")

    elif choice == "use your cellphone":
            if "your cellphone" in PLAYER.inventory:
                Events.CellPhone()
            else:
                print("You look around for your cellphone, but just can't find it here!")
            timer(1)

    elif choice[:3] == "use" and choice[4:] != "computer" and choice[4:] != "your cellphone" and choice[4:] != "stapler" and choice[4:] != "hole puncher":
        temp_inventory = PLAYER.inventory.copy()
        for things in World.items:
            if World.items[things].useable and World.items[things].name in temp_inventory and World.items[things].name == choice[4:]:
                print("You used " + World.items[things].name + "!\n")
                PLAYER.remove_item(World.items[things])
                if World.items[things].name == "chocolate bar" or World.items[things].name == "candy cane":
                    PLAYER.choc_timer += 12
                    Events.Healthy_Eater = False
                elif World.items[things].name == "energy drink":
                    teleport = input("Where do you want to dash to?"
                                     "(residence / kaneff / student centre / deerfield / davis / ib / cct)")
                    if teleport == "residence":
                        PLAYER.set_pos(0, 4)
                        timer(1)
                    elif teleport == "kaneff":
                        PLAYER.set_pos(3, 4)
                        timer(1)
                    elif teleport == "student centre":
                        PLAYER.set_pos(2, 2)
                        timer(1)
                    elif teleport == "deerfield":
                        PLAYER.set_pos(4, 0)
                        timer(1)
                    elif teleport == "davis":
                        PLAYER.set_pos(3, 6)
                        timer(1)
                    elif teleport == "ib":
                        PLAYER.set_pos(5, 3)
                        timer(1)
                    elif teleport == "cct":
                        PLAYER.set_pos(4, 4)
                        timer(1)


    elif choice in location.available_actions():
        if choice == "study":
            if "ned's study notes" in PLAYER.inventory:
                print("You quickly glance over Ned's amazing notes in preparation for the exam.")
                PLAYER.score += 500
                timer(1)
            else:
                print("You quickly glance over your notes in preparation for the exam.")
                PLAYER.score += 100
                timer(1)
            Events.Professional_crammer += 1

        elif choice == "warm up":
            print("You get near the closest heater and warm yourself up for a minute.")
            PLAYER.hypothermia = 0
            timer(1)

        # Talking Events
        elif choice[:7] == "talk to":
            if choice[8:] == "jessica" and location.index == 6:
                if not Events.bus1:
                    Events.Bus_Stop1()
                    print("\nObtained T-Card!\n")
                    PLAYER.add_item(World.items["t-card"])
                    Events.bus1 = True
                    location.available_actions().remove(choice)
                    timer(1)
                talkative(choice)

            elif choice[8:] == "jessica" and location.index == 39:
                if "t-card" not in PLAYER.inventory:
                    Events.IB120_1()
                    print("\nObtained T-Card!\n")
                    PLAYER.add_item(World.items["t-card"])
                    Events.bus1 = True
                    location.available_actions().remove(choice)
                else:
                    Events.IB120_2()
                timer(1)
                talkative(choice)
            elif choice[8:] == "mike":
                Events.KC_1()
                timer(3)
                talkative(choice)
            elif choice[8:] == "bystander":
                Events.Bus_Stop2()
                timer(1)
                talkative(choice)
            elif choice[8:] == "boys":
                Events.SC_1()
                timer(1)
                talkative(choice)
            elif choice[8:] == "foosball players":
                Events.SC_2()
                timer(1)
                talkative(choice)
            elif choice[8:] == "musical dude":
                Events.CPathway()
                timer(1)
                talkative(choice)

            elif choice[8:] == "ned":
                if "Ned's Gadget" in PLAYER.inventory:
                    Events.CCT_2()
                    print("\nObtained Ned's Study Notes!\n")
                    PLAYER.add_item(World.items["ned's study notes"])
                    PLAYER.remove_item(World.items["ned's gadget"])
                    location.available_actions().remove(choice)
                    PLAYER.score += 750
                    Events.Helping_hand += 1
                else:
                    Events.CCT_1()
                timer(1)
                talkative(choice)

            elif choice[8:] == "musicians":
                if Events.SC_3():
                    Events.sc1 = True
                    print("\nObtained Cheat Sheet Top Half!\n")
                    PLAYER.add_item(World.items["cheat sheet top half"])
                    location.available_actions().remove(choice)
                    timer(3)
                talkative(choice)

            elif choice[8:] == "friends":
                Events.Caf_1()
                timer(3)
                talkative(choice)

            elif choice[8:] == "dave":
                if "calculus textbook" in PLAYER.inventory and "sociology textbook" in PLAYER.inventory and "anthropology textbook" in PLAYER.inventory:
                    Events.LibF1_2()
                    PLAYER.remove_item(World.items["calculus textbook"])
                    PLAYER.remove_item(World.items["sociology textbook"])
                    PLAYER.remove_item(World.items["anthropology textbook"])
                    PLAYER.add_item(World.items["lucky pen"])
                    print("\nObtained Lucky Pen!\n")
                    location.available_actions().remove(choice)
                    World.map[4][5] = 27
                else:
                    Events.LibF1_1()
                timer(1)
                talkative(choice)

            elif choice[8:] == "sheldon":
                if "proofs textbook" in PLAYER.inventory:
                    print("You return Sheldon's textbook to him. He quickly replies with a thank you and takes his seat.")
                    PLAYER.remove_item(World.items["proofs textbook"])
                    location.available_actions().remove(choice)
                    PLAYER.score += 750
                    Events.Helping_hand += 1
                else:
                    Events.IB120_3()
                talkative(choice)

            elif choice[8:] == "lauren":
                if "psychology textbook" in PLAYER.inventory:
                    print("To Lauren's delight, you return her Psychology Textbook back to her. She says she owes\n"
                          "you big time. Again.\n")
                    PLAYER.remove_item(World.items["psychology textbook"])
                    location.available_actions().remove(choice)
                    PLAYER.score += 750
                    Events.Helping_hand += 1
                else:
                    Events.LibF3()
                talkative(choice)
                timer(1)

            elif choice[8:] == "kristina":
                Events.IB110_1()
                print("\nObtained Kristina's USB!\n")
                PLAYER.add_item(World.items["kristina's usb"])
                location.available_actions().remove(choice)
                timer(1)
                talkative(choice)

            elif choice[8:] == "brian":
                Events.LibF4_1()
                print("\nObtained Cheat Sheet Bottom Half!\n")
                PLAYER.add_item(World.items["cheat sheet bottom half"])
                location.available_actions().remove(choice)
                timer(1)
                talkative(choice)

        # Going to Places
        elif "go to" in choice:
            if choice[6:] == "deerfield":
                PLAYER.set_pos(4, 0)
            elif choice[6:] == "student centre":
                PLAYER.set_pos(2, 2)
            elif choice[6:] == "western pathway":
                PLAYER.set_pos(2, 3)
            elif choice[6:] == "dh path":
                PLAYER.set_pos(3, 1)
            elif choice[6:] == "ib-dh path":
                PLAYER.set_pos(5, 0)
            elif choice[6:] == "athletic centre":
                PLAYER.set_pos(1, 7)
            elif choice[6:] == "davis":
                PLAYER.set_pos(3, 6)
            elif choice[6:] == "bus stop":
                PLAYER.set_pos(2, 4)
            elif choice[6:] == "library floor 1":
                PLAYER.set_pos(6, 8)
            elif choice[6:] == "library floor 2":
                PLAYER.set_pos(5, 4)
            elif choice[6:] == "ib path":
                PLAYER.set_pos(4, 2)
            elif choice[6:] == "central pathway":
                PLAYER.set_pos(3, 5)
            elif choice[6:] == "kaneff":
                PLAYER.set_pos(3, 4)
            elif choice[6:] == "cct":
                PLAYER.set_pos(4, 4)
            elif choice[6:] == "ib":
                PLAYER.set_pos(5, 3)
            timer(1)
        elif choice[:5] == "enter":
            if choice[6:] == "dv-2084":
                PLAYER.set_pos(2, 8)
            elif choice[6:] == "dh-2026":
                PLAYER.set_pos(4, 8)
            elif choice[6:] == "exam room":
                PLAYER.set_pos(7, 1)
            elif choice[6:] == "ib-110":
                PLAYER.set_pos(6, 2)
            elif choice[6:] == "ib-235":
                PLAYER.set_pos(0, 0)
            elif choice[6:] == "ib-245":
                PLAYER.set_pos(0, 2)
            elif choice[6:] == "ib-335":
                PLAYER.set_pos(2, 2)
            elif choice[6:] == "ib-345":
                PLAYER.set_pos(7, 7)
            timer(1)

        # Searching Events
        elif choice[:6] == "search":
            if choice[7:] == "bus stop":
                Events.Bus_Search()
                timer(5)
            elif choice[7:] == "case room":
                Events.K_Search()
                timer(3)
            elif choice[7:] == "tables":
                Events.Caf_Search()
                timer(3)
            elif choice[7:] == "hallway":
                Events.DavisHalls()
                timer(3)
            elif choice[7:] == "open locker":
                Events.O_Locker()
                print("\nObtained Candy Cane!\n")
                PLAYER.add_item(World.items["candy cane"])
                location.available_actions().remove(choice)
                timer(1)
            elif choice[7:] == "study zone":
                if location.index == 28:
                    if "sociology textbook" not in PLAYER.inventory:
                        if Events.LibZ_1():
                            if PLAYER.weight + World.items["sociology textbook"].weight < 4:
                                print("Obtained Sociology Textbook!\n")
                                PLAYER.add_item(World.items["sociology textbook"])
                                location.available_actions().remove(choice)
                            else:
                                print("Your bag can't take that many textbooks!")
                    else:
                        Events.LibZ_2()
                elif location.index == 29 or location.index == 30:
                    Events.LibZ_2()
                timer(5)

            elif choice[7:] == "room":
                if location.index == 33 or location.index == 36:
                    Events.IB_Rooms1()
                elif location.index == 35:
                    Events.IB_Rooms2()
                else:
                    if World.items["anthropology textbook"] not in PLAYER.inventory:
                        if Events.IB_Rooms3():
                            if PLAYER.weight + World.items["anthropology textbook"].weight < 4:
                                print("Obtained Anthropology Textbook!\n")
                                PLAYER.add_item(World.items["anthropology textbook"])
                                location.available_actions().remove(choice)
                            else:
                                print("Your bag can't take that many textbooks!")
                    else:
                        Events.IB_Rooms1()
                timer(5)

        # Picking up items
        elif choice[:3] == "get":
            for things in World.items.keys():
                if World.items[things].start == location.index and World.items[things].name == choice[4:]:
                    print("Obtained " + choice[4:] + "!\n")
                    PLAYER.add_item(World.items[things])
                    location.available_actions().remove(choice)

        elif choice[:7] == "pick up":
            if PLAYER.weight <= 2:
                for books in World.items.keys():
                    if World.items[books].start == location.index and World.items[books].name == choice[8:]:
                        print("Obtained " + choice[8:] + "!\n")
                        PLAYER.add_item(World.items[books])
                        location.available_actions().remove(choice)
                        if choice[8:] == "your cellphone":
                            Events.gotphone = True
            else:
                print("You can't carry that many textbooks!")

        # Miscellaneous Events
        elif choice == "wake up brandon":
            Events.LibB_1()
            PLAYER.score += 750
            location.available_actions().remove(choice)
            Events.Helping_hand += 1

        elif choice == "check bus times":
            Events.Bus_Times()
            location.available_actions().remove(choice)
            timer(1)

        elif choice == "investigate locker":
            if Events.Adv_Locker():
                print("\nObtained Gift Coat!\n")
                PLAYER.add_item(World.items["gift coat"])
                Events.Survivalist = False
                location.available_actions().remove(choice)
                timer(5)

        elif choice == "follow glow":
            if Events.glow == False and "gift Coat" in PLAYER.inventory:
                if Events.glow_event():
                    print("\nObtained Ned's Gadget!\n")
                    PLAYER.add_item(World.items["ned's gadget"])
                    Events.glow = True
                    location.available_actions.remove(choice)
                    timer(8)
            else:
                print("You need a jacket to be out exploring out in this cold!\n")

        elif choice == "ride with michael":
            print("Michael drives you to IB free of charge.")
            PLAYER.set_pos(5, 3)
            timer(4)

        elif choice == "use computer":
            if "kristina's usb" in PLAYER.inventory and not Events.printed:
                Events.Computer1()
                Events.printed = True
                print("\nObtained Kristina's Cheat Sheet!\n")
                PLAYER.add_item(World.items["kristina's cheat sheet"])
            else:
                Events.Computer2()
            timer(1)

        elif choice == "use stapler":
            if "cheat sheet bottom half" in PLAYER.inventory and "cheat sheet top half" in PLAYER.inventory and not Events.stapled:
                Events.Stapler1()
                Events.stapled = True
                print("\nObtained Obtained Full Cheat Sheet!\n")
                PLAYER.add_item(World.items["full cheat sheet"])
                PLAYER.remove_item(World.items["cheat sheet bottom half"])
                PLAYER.remove_item(World.items["cheat sheet top half"])
            else:
                Events.Stapler2()
            timer(1)

        elif choice == "use hole puncher":
            Events.HolePuncher()
            timer(1)

        elif choice == "write exam":
            if "t-card" in PLAYER.inventory and "lucky pen" in PLAYER.inventory:
                if "full cheat sheet" in PLAYER.inventory or "kristina's cheat sheet" in PLAYER.inventory:
                    if Events.Write_Exam():
                        PLAYER.victory = True
                        Events.Wrote_Exam = True
                        if float(PLAYER.timer[:1]) < 7:
                            Events.Punctual = True
                        if "full cheat sheet" in PLAYER.inventory and "kristina's cheet sheet" in PLAYER.inventory and "extra supplies" in PLAYER.inventory:
                            Events.Over_prepared = True
                else:
                    print("You don't have all your necessary materials!")
            else:
                print("You don't have all your necessary materials!")
        PLAYER.past_choices.append(choice)
    else:
        print("That is not a valid command!")

# Handles the clock
def timer(time):
    '''

    :param time:
    :return:
    '''
    hours = int(PLAYER.timer[:1])
    if PLAYER.choc_timer > 0 and time > 0:
        seconds = float(PLAYER.timer[2:]) + time * 0.5
        PLAYER.choc_timer -= 1
    else:
        seconds = float(PLAYER.timer[2:]) + time

    if seconds >= 60:
        seconds = seconds - 60
        hours += 1

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = "{0}:{1}".format(hours, seconds)
    PLAYER.timer = time

# Handles walls, map changes and hypothermia
def check_loc(World, PLAYER):
    '''
    :param World:
    :param PLAYER:
    :param location:
    :param choice:
    :return:
    '''
    location = World.get_location(PLAYER.x, PLAYER.y)
    outside_locs = [3, 4, 5, 6, 7, 8, 10, 13, 20, 32, 37]
    if location is None:
        PLAYER.x = lastposx
        PLAYER.y = lastposy
        timer(-1)
        print("That way is blocked.\n")
    elif PLAYER.x < 0 or PLAYER.y < 0:
        PLAYER.x = lastposx
        PLAYER.y = lastposy
        timer(-1)
        print("That way is blocked.\n")

    elif location.index in outside_locs and "gift coat" not in PLAYER.inventory:
        PLAYER.hypothermia += 1

    if "gift coat" in PLAYER.inventory:
        PLAYER.hypothermia = 0

    if PLAYER.hypothermia == 4:
        print("You can't stay outside without a jacket for much longer!")

    if PLAYER.hypothermia == 5:
        print("Your Hypothermia Alert is Level 5!!!")
        print("You cannot risk getting sick out here before your exam and dash back to the warmth of your residence.\n")
        PLAYER.set_pos(0, 4)
        PLAYER.hypothermia = 0

    if (float(PLAYER.timer[2:]) >= 30 and float(PLAYER.timer[:1]) == 5) or float(PLAYER.timer[:1]) > 5:
        World.map[4][0] = 1
        if Events.gotphone:
            World.map[4][0] = 2

    if (float(PLAYER.timer[2:]) >= 45 and float(PLAYER.timer[:1]) == 5) or float(PLAYER.timer[:1]) > 5:
        World.map[4][2] = 6

    if (float(PLAYER.timer[2:]) >= 30 and float(PLAYER.timer[:1]) == 6) or float(PLAYER.timer[:1]) > 6:
        World.map[4][2] = 7
        World.map[7][3] = 18

# Handles Talkative Achievement
def talkative(choice):
    '''
    :param choice: the choice made by the player
    :return:
    '''
    if choice not in PLAYER.past_choices:
        Events.Talkative += 1

# Handles Tour Guide Achievement
def tguide(World, Player, location):
    '''
    :param choice: the choice made by the player
    :return:
    '''
    if location.name not in Player.past_places:
        Player.past_places.append(location.name)

    count = 0
    for x in World.locations:
        if World.locations[x].name in Player.past_places:
            count += 1
    if count >= 34:
        Events.Tour_Guide = True

# Handles Achievement Scoring
def A_Checker(Player):
    '''

    :param Player: the player object
    :return:
    '''
    print("Your Achievements:")
    counter = 0
    if Events.Wrote_Exam:
        counter += 1
        s = "\tA1: Wrote the Exam - {0}".format(Events.Wrote_Exam_desc)
        print(s)
        Player.score += 750
    if Events.Helping_hand >= 5:
        counter += 1
        s = "\tA2: Helping Hand - {0}".format(Events.Helping_hand_desc)
        print(s)
        Player.score += 1000
    if Events.Professional_crammer >= 10:
        counter += 1
        s = "\tA3: Professional Crammer - {0}".format(Events.Professional_crammer_desc)
        print(s)
        Player.score += 1000
    if Events.Over_prepared:
        counter += 1
        s = "\tA4: Over Prepared - {0}".format(Events.Over_prepared_desc)
        print(s)
        Player.score += 1250
    if Events.Punctual:
        counter += 1
        s = "\tA5: Punctual - {0}".format(Events.Punctual_desc)
        print(s)
        Player.score += 1250
    if Events.Healthy_Eater:
        counter += 1
        s = "\tA6: Healthy Eater - {0}".format(Events.Healthy_Eater_desc)
        print(s)
        Player.score += 1500
    if Events.Survivalist:
        counter += 1
        s = "\tA7: Survivalist - {0}".format(Events.Survivalist_desc)
        print(s)
        Player.score += 1500
    if Events.Talkative == 14:
        counter += 1
        s = "\tA8: Talktative - {0}".format(Events.Talkative_desc)
        print(s)
        Player.score += 2000
    if Events.Tour_Guide:
        counter += 1
        s = "\tA9: Tour Guide - {0}".format(Events.Tour_Guide_desc)
        print(s)
        Player.score += 1500
    if counter >= 9:
        counter += 1
        s = "\tA10: Multitasker - {0}".format(Events.Multitasker_desc)
        print(s)
        Player.score += 3000

    print("Your total score is " + str(PLAYER.score))

    if PLAYER.score >= 25000:
        print("You got perfect on the exam!")
    elif PLAYER.score >= 20000 and PLAYER.score < 25000:
        print("You got 99% on the exam!")
    elif PLAYER.score >= 19000 and PLAYER.score < 20000:
        print("You got 95% on the exam!")
    elif PLAYER.score >= 19000 and PLAYER.score < 20000:
        print("You got 90% on the exam!")
    elif PLAYER.score >= 17000 and PLAYER.score < 19000:
        print("You got 85% on the exam!")
    elif PLAYER.score >= 15000 and PLAYER.score < 17000:
        print("You got 80% on the exam!")
    elif PLAYER.score >= 12500 and PLAYER.score < 15000:
        print("You got 75% on the exam!")
    elif PLAYER.score >= 10000 and PLAYER.score < 12500:
        print("You got 70% on the exam!")
    elif PLAYER.score >= 8000 and PLAYER.score < 10000:
        print("You got 65% on the exam!")
    else:
        print("You got 60% on the exam!")
    print("\n")

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")

    print('''
You slowly wake up in your residence after a short nap and you feel that you are very confident in writing your CSC108
exam today in IB-120. You studied pretty hard yesterday and this morning. You pack your bag with your notebook, study
notes, pencil case and you start to notice...
Where's your T-Card? As a matter of fact, where's your lucky exam pen and cheat sheet too? You can't possibly write the
exam without all 3 items. Also the weather report for this evening is... around -20°C!? You forgot to bring your winter
jacket from home this weekend too! Now you have to search across campus while not trying to be caught outside for too long.
The exam begins at 7:10pm, only about 2 hours away! You take a deep breath...
(Type in "help" for tips)
    ''')

    PLAYER = Player(0,4)

    menu = ["look", "inventory", "score", "notes", "help"]

    inventory_menu = [""]

    while not PLAYER.victory:
        lastposx = PLAYER.x
        lastposy = PLAYER.y
        location = WORLD.get_location(PLAYER.x, PLAYER.y)
        HUD = "Player Score: {0}                    Hypothermia Alert: {1}                  Clock: {2}\n".format(PLAYER.score, PLAYER.hypothermia, PLAYER.timer)
        print(location.get_name())
        print(HUD)
        if location.visited == False:
            print(location.get_full_description())
        else:
            print(location.get_brief_description())
        location.visited = True

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        for things in WORLD.items:
            if WORLD.items[things].drop_loc == location.index:
                print("recover " + WORLD.items[things].name)
        for things in PLAYER.inventory:
            if WORLD.items[things].useable:
                print("use " + WORLD.items[things].name)
        choice = input("\nEnter action: ")
        choice.lower()
        print("\n")

        if choice == "quit":
            break

        do_action(WORLD, PLAYER, location, choice)
        check_loc(WORLD, PLAYER)
        tguide(WORLD, PLAYER, location)

        #Check Player's weight
        PLAYER.weight = 0
        for stuff in PLAYER.inventory:
            PLAYER.weight += int(WORLD.items[stuff].weight)

        # Game Over at 7:10
        if float(PLAYER.timer[:1]) == 7 and float(PLAYER.timer[2:]) >= 10:
            print("You couldn't make it to your exam in time!")
            print("Game Over!")
            break

    if choice == "quit":
        print("You quit the game.")


    if PLAYER.victory == True:
        PLAYER.score += 5000
        print("\nYour score is: " + str(PLAYER.score) + "\n")
        x = A_Checker(PLAYER)
