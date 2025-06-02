# Game buying platform for PC, console and android
#============================================================================================

# Modules being imported section
# These are placeholders; define these modules or remove if not used
# import Android_Games
# import PS_5_and_4_games
# import Xbox_Games
# import Nintendo_Games
# import PC_Games
# import Add_friend
# import Check_out
# import View_Games

import pyttsx3

# Initialize speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()

#============================================================================================

# Intro Section
print("\n" + ("="*130) + "\n")
print("....(▀̿Ĺ̯▀̿ ̿)...Hello, I am Patrick, your A.I for this program\n")
print("="*50, "Welcome to Trapster", "="*50, "\n")

speak("Hello, I am Patrick, your AI for this program Trapster. Let's go")

#============================================================================================

f = {}  # Cart Dictionary
sum1 = 0

def main():
    while True:
        print('''\nChoose one of the options:
1. Buy Game
2. View games for free
3. Add a friend
4. Check out
5. Exit''')

        speak("Here are 5 options, Buy game, view games, add a friend, check out and exit. Select by writing serial number.")
        
        try:
            ch = int(input("\nEnter your choice by number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if ch == 1:
            speak("Tell me what device are you using.")
            print('''\nChoose device:
1.) Android
2.) Console
3.) PC''')

            try:
                cho = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input.")
                continue

            # ANDROID SECTION
            if cho == 1:
                print("\n" + "="*40, "Android games", "="*40 + "\n")
                speak("Here are games for android")
                print('''1. Minecraft\n2. Ludo King\n3. Roblox\n4. GTA-VC\n5. GTA-SA''')
                speak("Select by serial number")
                choice = int(input("Enter choice: "))

                if choice == 1:
                    speak("Minecraft is a block-based world builder. Buy it for ₹400 in the Trapster Sale!")
                    print("Minecraft added to cart.")
                    f["Minecraft"] = 400
                elif choice == 2:
                    speak("Ludo King is a casual game you can play anytime.")
                    print("Ludo King added to cart.")
                    f["Ludo King"] = 0
                elif choice == 3:
                    speak("Roblox lets you create and play games. It's free!")
                    print("Roblox added to cart.")
                    f["Roblox"] = 0
                elif choice == 4:
                    speak("GTA Vice City is a classic. Enter coupon to get it for ₹108")
                    coupoun = input("Enter coupon code: ")
                    if coupoun == 'mute speakers':
                        print("Discount applied!")
                        f["GTA-VC"] = 108
                    else:
                        f["GTA-VC"] = 121
                elif choice == 5:
                    speak("GTA San Andreas is all about gang wars. Special Trapster price ₹142.")
                    f["GTA-SA"] = 142

            # CONSOLE SECTION
            elif cho == 2:
                print("="*40, "C O N S O L E", "="*40)
                speak("Tell me which console do you have. PS-5, PS-4, Xbox-X or Nintendo switch. Select serial number")
                print('''1. PS-5\n2. PS-4\n3. Xbox-X\n4. Nintendo Switch''')
                choic = int(input("Enter your choice: "))

                # Console options mapped to games
                games_dict = {
                    1: [("The Last of Us", 5470), ("Ghost of Tsushima", 5000), ("Demon's Souls", 5499),
                        ("Spider-Man: Miles Morales", 4049), ("Gran Turismo 7", 5000)],
                    2: [("The Last of Us", 5470), ("Ghost of Tsushima", 5000), ("Demon's Souls", 5499),
                        ("Spider-Man: Miles Morales", 4049), ("Gran Turismo 7", 5000)],
                    3: [("Hogwarts Legacy", 4000), ("Watch Dogs Legion", 2180), ("FIFA 23", 4199),
                        ("COD: Black Ops", 4049), ("WWE 2K22", 3999)],
                    4: [("Pokemon Violet", 4230), ("Fire Emblem Engage", 3664), ("Zelda", 4999),
                        ("Mario Kart 8", 4340), ("Celeste", 1628)]
                }

                if choic in games_dict:
                    speak("Select by serial number")
                    for idx, game in enumerate(games_dict[choic], 1):
                        print(f"{idx}. {game[0]} - ₹{game[1]}")
                    choice = int(input("Enter your choice: "))
                    selected_game = games_dict[choic][choice - 1]
                    f[selected_game[0]] = selected_game[1]

            # PC SECTION
            elif cho == 3:
                pc_games = [("Prince of Persia: FS", 813), ("GTA V", 3000), ("Roblox", 0), 
                            ("Mafia 3", 121), ("GTA-SA", 142)]
                speak("PC Games List. Select serial number")
                for idx, game in enumerate(pc_games, 1):
                    print(f"{idx}. {game[0]} - ₹{game[1]}")
                choice = int(input("Enter choice: "))
                selected_game = pc_games[choice - 1]
                f[selected_game[0]] = selected_game[1]

        elif ch == 2:
            speak("View Games is not implemented yet. But the list will soon be available.")
            print("Coming soon... Stay tuned for Free Games showcase!")

        elif ch == 3:
            speak("Adding a friend feature coming soon.")
            print("Friend module under construction.")

        elif ch == 4:
            sum1 = 0
            print("\n" + "="*20, "Games in cart List", "="*20)
            print("Games\t\t\tPrice")
            for i in f:
                print(i, "\t\t\t", f[i])
                sum1 += f[i]
            print("\nTotal Price to be paid: ₹", sum1)
            speak("Thank you for shopping from Trapster. Program created by Rishabh Dhillon")
            print("\n" + "="*20, "RISHABH DHILLON", "="*20)
            print("༼ ಥ ‿ ಥ ༽ ( ͡❛ 👅 ͡❛) ( ͡❛ ㅅ ͡❛).........bye")
            break

        elif ch == 5:
            speak("Exiting Trapster. Thank you.")
            break

        else:
            print("Invalid option selected!")

# Run the program
main()
