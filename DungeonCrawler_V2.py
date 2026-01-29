.capitalize()

def startupMenu():
    originalMenu = 1
    global playerLadySirHuman
    global goldAmount
    global weapon1
    global weapon1Info
    global weapon1Int
    while True:
        print("...")
        input()
        print("You wake up in a place you do not recognize", end="")
        input()
        print("Someone stands above you. You jump up. They look indifferent to your distress")
        input()
        print("???: Good day, Traveller. Today, your journey starts.", end="")
        input()
        print("???: But first, we need to establish the basics. Select 'Character Creation' in the menu below.\n")
        break
    
    while True:
        print("1 - Character Creation")
        print("2 - Weapon Equipment")
        print("3 - Stats")
        print("4 - Starter Quest")
        menuChoose = int(input())
        if menuChoose == 1:
            if originalMenu == 1:
                while True:
                    originalMenu = 2
                    print("\nWhat are your pronouns?\n1 - She/her\n2 - He/him\n3 - They/them\n")
                    playerPronouns = int(input())
                    if playerPronouns == 1:
                        playerFirstPronounCapital = "She"
                        playerFirstPronoun = "she"
                        playerSecondPronounCapital = "Her"
                        playerSecondPronoun = "her"
                        playerThirdPronounCapital = "Hers"
                        playerThirdPronoun = "hers"
                        playerLadySirHumanCapital = "Fair lady"
                        playerLadySirHuman = "fair lady"
                        playerToBe = "is"
                        break
                    elif playerPronouns == 2:
                        playerFirstPronounCapital = "He"
                        playerFirstPronoun = "he"
                        playerSecondPronounCapital = "Him"
                        playerSecondPronoun = "him"
                        playerThirdPronounCapital = "His"
                        playerThirdPronoun = "his"
                        playerLadySirHumanCapital = "Brave sir"
                        playerLadySirHuman = "brave sir"
                        playerToBe = "is"
                        break
                    elif playerPronouns == 3:
                        playerFirstPronounCapital = "They"
                        playerFirstPronoun = "they"
                        playerSecondPronounCapital = "Them"
                        playerSecondPronoun = "them"
                        playerThirdPronounCapital = "Theirs"
                        playerThirdPronoun = "theirs"
                        playerLadySirHumanCapital = "Fine fellow"
                        playerLadySirHuman = "fine fellow"
                        playerToBe = "are"
                        break
                    else:
                        print("I did not understand that", end="")
            print("\n Hello,", playerLadySirHuman, end=". What's your name?\n")
            playerName = input()
            print("\nYou chose", playerName, "as your name.",)
            readyToContinue = int(input("Continue?\n1 - Yes\n2 - No\n"))
            if readyToContinue == 1:
                print("???: Glad to meet you", playerName, "For the next step, you will need to choose your race.")
                while True:
                    print("1 - Human")
                    print("2 - Elf")
                    print("3 - Dwarf")
                    print("4 - Orc\n")
                    playerRace = int(input())
                    if playerRace == 1:
                        raceInfo(playerRace)
                        print("Press Y to choose this race, press N to go back.")
                        YN = input("Y/N ")
                        if YN == "Y":
                            YN = "empty"
                            break
                    elif playerRace == 2:
                        raceInfo(playerRace)
                        print("Press Y to choose this race, press N to go back.")
                        YN = input("Y/N ")
                        if YN == "Y":
                            YN = "empty"
                            break
                    elif playerRace == 3:
                        raceInfo(playerRace)
                        print("Press Y to choose this race, press N to go back.")
                        YN = input("Y/N ")
                        if YN == "Y":
                            YN = "empty"
                            break
                    elif playerRace == 4:
                        raceInfo(playerRace)
                        print("Press Y to choose this race, press N to go back.")
                        YN = input("Y/N ")
                        if YN == "Y":
                            YN = "empty"
                            break
                    else:
                        print("I did not understand")
                print(playerRace)
            elif readyToContinue == 2:
                print("So like why\n")
            else:
                print("Try again wtf\n") 
        elif menuChoose == 2:
            while True:
                if originalMenu == 2:
                    print("\nYou and ??? travel to the local blacksmith.", end="")
                    input()
                    print("Thankfully, it's not too far ahead. When you walk in, the blacksmith seems to recognize ???", end="")
                    input()
                    print("Blacksmit: ???! Good to see you, lad! I and I see you brought someone too... Who is this", playerLadySirHuman, "you brought today?", end="")
                    input()
                    print("???: This is", playerName, end=". ")
                    print(playerFirstPronounCapital, playerToBe,"looking for a starter weapon.")
                    print("\nYou look around. Which weapon attracts your interest the most?")
                    while True:
                        weaponInfo = int(input("1: Sword.\n2: Bow.\n3: Dagger.\nType 1, 2 or 3 to for more info! "))
                        if weaponInfo == 1:
                            weapon1Int = 1
                            weapon1Info(weapon1Int)
                            print("Press Y to choose this weapon, press N to go back.")
                            YN = input("Y/N ")
                            if YN == "Y":
                                weapon1 = "sword"
                                originalMenu = 3
                                break
                        elif weaponInfo == 2:
                            weapon1Int = 2
                            weapon1Info(weapon1Int)
                            print("Press Y to choose this weapon, press N to go back.")
                            YN = input("Y/N ")
                            if YN == "Y":
                                weapon1 = "bow"
                                originalMenu = 3
                                break
                        elif weaponInfo == 3:
                            weapon1Int = 3
                            weapon1Info(weapon1Int)
                            print("Press Y to choose this weapon, press N to go back.")
                            YN = input("Y/N ")
                            if YN == "Y":
                                weapon1 = "dagger"
                                originalMenu = 3
                                break
                        else:
                            print("Try again")
                            break
                    complete = "True"
                    print("You point to the", weapon1, end=".")
                    input()
                    print("You: I want the", weapon1, end=". Please.")
                    input()
                    print("Blacksmith: As you wish,", playerLadySirHuman, end="! That shall be... 5 gold coins.")
                    input()
                    print("???: That shall leave you with", (goldAmount - 5), "coins.")
                    goldAmount = goldAmount - 5
                    input()
                    print("???: Your basic character setup is now complete. As you progress you shall find more options to buy armor, weapons, and spells.", end="")
                    input()
                    print("It's now time for the main quest to begin... But first, let's check the stats we just set up.")
                    originalMenu = 3
                elif originalMenu == 3:
                    break
                else:
                    print("\nCreate your character first!\n")
                    sleep(0.5)
        elif menuChoose == 3:
            if originalMenu == 3:
                raceInfo(playerRace)
                print("")
                inventoryInfo()
                print("")
                weapon1Info(weapon1Int)
                print("")
                break
            else:
                print("fout")
                exit()

    startgame()

startupMenu()
for x in range(4):
    print("...")
    input()
    print("???: Hello?")
    input()
    print("???: Anyone here?")
    input()
    print("A light flickers on.")
    input()
    print("Shadows cast on the walls of a big tavern.")
    input()
    print("???: They're waking up, lads!")
    input()
                    


    