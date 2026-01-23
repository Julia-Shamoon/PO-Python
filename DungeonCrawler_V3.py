'''
Version 3: Improved indentation efficiency by merging if statements
'''

from time import sleep

# Sword
swordAttack = 7
swordDefense = 4
swordDexterity = 4
# Bow
bowAttack = 8
bowDefense = 1
bowDexterity = 2

# Dagger
daggerAttack = 4
daggerDefense = 4
daggerDexterity = 8

# Inventory
goldAmount = 20
weapon1 = 5

def weapon1Info(weapon1Int): #Check the stats for your starter weapon
    if weapon1Int == 1:
        print("SWORD INFO\nAttack =", swordAttack, "\nDefense =", swordDefense, "\nDexterity =", swordDexterity)
    if weapon1Int == 2:
        print("BOW INFO\nAttack =", bowAttack, "\nDefense =", bowDefense, "\nDexterity =", bowDexterity)
    if weapon1Int == 3:
        print("DAGGER INFO\nAttack =", daggerAttack, "\nDefense =", daggerDefense, "\nDexterity =", daggerDexterity)

def raceInfo(playerRace): # Check the stats for your race
    if playerRace == 1:
        print("HUMAN INFO\n <PLACEHOLDA>\n")
    elif playerRace == 2:
        print("ELF INFO\n <PLACEHOLDA>\n")
    elif playerRace == 3:
        print("DWARF INFO\n <plACEHOLDA>\n")
    elif playerRace == 4:
        print("ORC INFO\n <PLACEHOLDDDKAJDF;LAKSJF>\n")
    
def inventoryInfo(): # Check your inventory
    print("Gold:", goldAmount)
    print("Weapons:", weapon1)
    

def startupMenu(): # Start of the game. Character creation, starter weapon, stats check and first quest.
    originalMenu = 1
    global playerLadySirHuman
    global goldAmount
    global weapon1
    global weapon1Info
    global weapon1Int
    print("...")
    input()
    print("You wake up in a place you do not recognize", end="")
    input()
    print("Someone stands above you. You jump up. They look indifferent to your distress")
    input()
    print("???: Good day, Traveller. Today, your journey starts.", end="")
    input()
    print("???: But first, we need to establish the basics. Select 'Character Creation' in the menu below.\n")
    
    while True:
        print("1 - Character Creation")
        print("2 - Weapon Equipment")
        print("3 - Stats")
        print("4 - Starter Quest")
        menuChoose = int(input())
        if originalMenu == 1 and menuChoose == 1: # Start the character creation menu
            originalMenu = 2
            while True:
                print("\nWhat are your pronouns?\n1 - She/her\n2 - He/him\n3 - They/them")
                playerPronouns = int(input())
                if playerPronouns == 1:
                    playerFirstPronoun = "she"
                    playerSecondPronoun = "her"
                    playerThirdPronoun = "hers"
                    playerLadySirHuman = "fair lady"
                    playerToBe = "is"
                    break
                elif playerPronouns == 2:
                    playerFirstPronoun = "he"
                    playerSecondPronoun = "him"
                    playerThirdPronoun = "his"
                    playerLadySirHuman = "brave sir"
                    playerToBe = "is"
                    break
                elif playerPronouns == 3:
                    playerFirstPronoun = "they"
                    playerSecondPronoun = "them"
                    playerThirdPronoun = "theirs"
                    playerLadySirHuman = "fine fellow"
                    playerToBe = "are"
                    break
                else:
                    print("I did not understand that\n")
            print("\n Hello,", playerLadySirHuman, end=". What's your name?\n")
            playerName = input()
            print("")
            while True:
                print("You chose", playerName, "as your name.",)
                readyToContinue = int(input("Continue?\n1 - Yes\n2 - No\n"))
                if readyToContinue == 1:
                    break
                elif readyToContinue == 2:
                    print("So like why\n")
                else:
                    print("I did not understand that\n")
            print("???: Glad to meet you", playerName, "For the next step, you will need to choose your race.")
            while True:
                print("1 - Human")
                print("2 - Elf")
                print("3 - Dwarf")
                print("4 - Orc\n")
                playerRace = int(input())
                if playerRace == 1:
                    raceInfo(playerRace)
                    print("Continue?\n1 - Yes\n2 - No\n")
                    readyToContinue = int(input())
                    if readyToContinue == 1:
                        break
                elif playerRace == 2:
                    raceInfo(playerRace)
                    print("Continue?\n1 - Yes\n2 - No\n")
                    readyToContinue = int(input())
                    if readyToContinue == 1:
                        break
                elif playerRace == 3:
                    raceInfo(playerRace)
                    print("Continue?\n1 - Yes\n2 - No\n")
                    readyToContinue = int(input())
                    if readyToContinue == 1:
                        break
                elif playerRace == 4:
                    raceInfo(playerRace)
                    print("Continue?\n1 - Yes\n2 - No\n")
                    readyToContinue = int(input())
                    if readyToContinue == 1:
                        break
                else:
                    print("I did not understand that\n")
        elif originalMenu == 1 and menuChoose != 1: # The step to take is the cc menu, but user picks something else
            print("Create your character first!")
        elif originalMenu == 2 and menuChoose == 2: # Start the weapon selection menu
            print("Blacksmith stuff")
            originalMenu = 3
        elif originalMenu == 2 and menuChoose != 2: # The step to take is the ws menu, but the user picks something else
            print("Pick yo weapon first!")
            
startupMenu()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    