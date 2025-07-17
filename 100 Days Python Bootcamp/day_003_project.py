print(r'''
                      ____________________________________________________________________
                     / \-----     ---------  -----------     -------------- ------    ----\
                     \_/__________________________________________________________________/
                     |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
                     |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
                     | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
                     |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
                     |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
                     |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
                     |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
                     |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
                     | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
                     |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
                     |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
                     | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
                     |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
                     | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
                     |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
                     | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
                     |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
                     | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
                     |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
                     |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
                     / \----- ----- ------------  ------- ----- -------  --------  -------\
                     \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_question = input("You see 2 doors. One is on the left one is on the right. Which one are you going to choose?\n").lower()
if  "left" in first_question:
    second_question = input("You choose the left door. It opened to a lake that you could not see the en of it. What will you do wait or swim ?\n").lower()
    if  "wait" in second_question:
        third_question = input("You waited and realize that the door you came in disappeared. And suddenly three doors came in to existence.\nThere is red, blue, and yellow door in front of you now.\nWhich one are you going to choose?\n").lower()
        if "yellow" in third_question :
            print("You choose the yellow door. When you open the door you see a chest on the middle of the room.\nYou cautiously walk towards it and open it. ")
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
            print("It is the treasure you have been looking for!!!\nYOU WIN !!")
        elif "red" in third_question:
            print("You choose the red door. When you walk in suddenly door close behind your back and fire start.\nYou started to panic and burned by fire\nGAME OVER")
            print(r'''
                     88                               88           
                     88                         ,d    88           
                     88                         88    88           
             ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
            a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
            8b       88 8PP""""""" ,adPPPPP88   88    88       88  
            "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
             `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  
            ''')
        elif "blue" in third_question:
            print("You choose the blue door. When you walk in suddenly door close behind your back and you see beasts comming towards you.\nYou started to panic and eaten by them.\nGAME OVER")
            print(r'''
                     88                               88           
                     88                         ,d    88           
                     88                         88    88           
             ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
            a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
            8b       88 8PP""""""" ,adPPPPP88   88    88       88  
            "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
             `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  
            ''')
        else:
            print(f"You choose the {third_question}.")
            print(r'''
                         88                               88           
                         88                         ,d    88           
                         88                         88    88           
                 ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
                a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
                8b       88 8PP""""""" ,adPPPPP88   88    88       88  
                "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
                 `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  
                ''')
    else:
        print(f"You choose the {second_question}. Suddenly you saw a Trout as big as a lion. It attacked you.\nGAME OVER")
        print(r'''
                 88                               88           
                 88                         ,d    88           
                 88                         88    88           
         ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
        a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
        8b       88 8PP""""""" ,adPPPPP88   88    88       88  
        "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
         `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  
        ''')
else:
    print(f"You choose the {first_question}. It is a dark corridor(?),at least you are thinking it is, when you were walking blink of time you felt like you were flying until you realize\nthat you fell into a hole.\nGAME OVER")
    print(r'''
             88                               88           
             88                         ,d    88           
             88                         88    88           
     ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
    a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
    8b       88 8PP""""""" ,adPPPPP88   88    88       88  
    "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
     `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  
    ''')