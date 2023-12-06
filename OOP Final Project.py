# OOP Final Project
import sys
import time
import os

def clear_terminal():
    os.system("cls")
os.system("cls")

def art():
    art = '''
    _____  _   _  ___    _      ____    ____  _____    _____  ___    _   _   ____
   |_   _|| |_| ||  _|  | |    | __ |  |  __||_   _|  /  _  \|  _|  | | | | |  __|
     | |  |  _  ||  _|  | |   | |__| |  \ \    | |    | | | || |_   | | | |  \ \ 
     | |  | | | || |_   | |__ |  __  | __| |   | |    | |_| || __|  | |_| | __| |
     |_|  |_| |_||___|  |____||_|  |_||____/   |_|    \_____/|_|    \_____/|____/

 _______________________________________________________________________________________            

    '''
    print(art)
art()

def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
slowprint("The Last of Us: Bustos \n\n")    

def new_game():
    art()
    slowprint("It's 9:00am in the morning and you just entered the school premises.\nWhile you're walking, you saw a bunch of students who are screaming and causing a commotion.\n")
    time.sleep(0.5)
    slowprint("And you were shocked to witness other students suddenly become aggressive.\n\n")
    time.sleep(0.5)
    slowprint("Do you want to find out what's happening?\n\n")
    time.sleep(0.5)
    
    def startgame():
        art()
        slowprint("Stay put and observe them from a safe distance.\n")
        time.sleep(0.5)
        slowprint("After a few minutes, you could see them becoming extremely frightened.\nYou also recognized that the other students was bleeding and acting strangely.\n")
        time.sleep(0.5)
        slowprint("When you noticed them coming towards where you were located, you quickly run and hide in the guard house.\n")
        time.sleep(0.5)
        slowprint("While you were hiding in the guard house, you received an alert message.\n\n")
        time.sleep(1.5)
        clear_terminal()
        art()
        
        slowprint('\t\t"!!!BREAKING NEWS!!!"\n"A BulSU Campus is ground zero for the zombie apocalypse."\n')
        time.sleep(0.5)
        slowprint('"If you received this message, please reply your name and current location."\n\n')
        time.sleep(0.5)
        
        student_name = input("Your name: ")
        slowprint(f"\n'My name is {student_name}, and I was currently trapped at the guard house.'\n\n")
        time.sleep(0.5)
        slowprint(f'"Hello, {student_name}. I will be your guide for you to survive this outbreak."\n')
        time.sleep(0.5)
        slowprint('"First, you must go to the Auditorium and find something you can use to protect yourself from the zombies."\n\n')
        time.sleep(0.5)
        slowprint("As you're approaching to the Auditorium, some zombies are running towards to you.\n")
        time.sleep(0.5)
        slowprint("But the front door is locked, what will you do?\n\n")
        time.sleep(0.5)

        def choice_one():
            art()
            slowprint("You see an open window on other side of the building and you go throught it.\n")
            time.sleep(0.5)
            slowprint("\n\t*1 new message*\n")
            time.sleep(0.5)
            slowprint(f'"Hey, {student_name}. Are you in the Auditorium now?"\n\n')
            time.sleep(0.5)
            slowprint("'Yes. Where should I go next?'\n\n")
            time.sleep(0.5)
            slowprint('"Great! The next building you must go is at the Pancho Hall."\n"But before that, do you have any protection and weapon you can use?"\n\n')
            time.sleep(0.5)
            slowprint("'I do have. I found a baseball bat and some duct tapes, I'm going to wrap it around on my arms and legs.'\n\n")
            time.sleep(0.5)
            slowprint('"Okay, good. To kill the zombie, directly strike it in the head as hard as you can"\n\n')
            time.sleep(0.5)
            slowprint("On your way out, you encounter a zombie. What will you do?\n\n")
            time.sleep(0.5)

            def zombie_attack():
                art()
                slowprint("*Smashed it in the head*\n\n")
                time.sleep(0.5)
                slowprint("Good job! You just killed a zombie and now run and go to the Pancho Hall.\n")
                time.sleep(0.5)
                slowprint("As you arrived at the Pancho Hall, you heard a scream coming from the faculty room.\n")
                time.sleep(0.5)
                slowprint("\n\t*1 new message*\n")
                time.sleep(0.5)
                slowprint(f'"What is your current location right now, {student_name}?"\n\n')
                time.sleep(0.5)
                slowprint("'I'm right now at the Pancho Hall and I heard someone is screaming at the faculty room.'\n\n")
                time.sleep(0.5)
                slowprint(f'"Okay, {student_name}. Listen carefully. The zombies are attracted to noises, so be careful."\n"Do not make any noises on your way out."\n\n')
                time.sleep(0.5)
                slowprint("As you approaching the faculty room, you saw Sir Cruz, one of your professor, screaming for help.\n")
                time.sleep(0.5)
                slowprint("\nBut a lot of zombies are piling up outside the faculty room.\nWill you help Sir Cruz?\n\n")
                time.sleep(0.5)

                def choiceOne():
                    art()
                    slowprint("There is a fire alarm at the hallway and you remember what the Admin said earlier.\n")
                    time.sleep(0.5)
                    slowprint("You set the fire alarm and all of the zombies rushed into the hallway where the alarm was buzzing.\n")
                    time.sleep(0.5)
                    slowprint("As the zombies gathered around at the hallway, you make your way now at the faculty room to save Sir Cruz.\n")
                    time.sleep(0.5)
                    slowprint("\n\t*1 new message*\n")
                    time.sleep(0.5)
                    slowprint(f'"Hey, {student_name}. Do you save the person who got trapped at the faculty room?"\n\n')
                    time.sleep(0.5)
                    slowprint("'Yes, I'm now with Sir Cruz. Where should we go next?'\n\n")
                    time.sleep(0.5)
                    slowprint('"Okay, both of you need to head to the CBA Building. All of the survivors have gathered there."\nWe will send out a helicopter to rescue all of the survivors."\n\n')
                    time.sleep(0.5)
                    slowprint("As you and Sir Cruz successfully escaped the Pancho Hall, where do you want to go now?\n\n")

                    def activity_center():
                        art()
                        slowprint("A lot of zombies are in there. Both of you are eaten by the zombies.\nGame over!\n")
                        time.sleep(0.5)
                        slowprint("Do you want to try again?\n\n")
                        time.sleep(0.5)

                        while True:
                            slowprint("[1] YES\n")
                            time.sleep(0.5)
                            slowprint("[2] NO\n\n")
                            time.sleep(0.5)

                            student_choice = input("Press [1] if YES or press [2] if NO: ")
                            print()
                            clear_terminal()

                            if student_choice == '1':
                                new_game()
                                break
                            elif student_choice == '2':
                                quit_game()
                                break
                            else:
                                art()
                                slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")

                    def hangar_room():
                        art()
                        slowprint("You're now meters away from surviving this outbreak.\n\n")
                        time.sleep(0.5)
                        slowprint("When you exit the Hangar Room, you found an army of zombies at the ground floor of the CBA Building.\n")
                        time.sleep(0.5)
                        slowprint("\n\t*1 new message*\n")
                        time.sleep(0.5)
                        slowprint(f'"{student_name}, you need to climb up to the rooftop of the CBA Building"\n"A lot of zombies are now at the ground floor. So hurry up before they get to the top"\n\n')
                        time.sleep(0.5)
                        slowprint("The surviving time is running out. What should you do now?\n\n")

                        def sneaky_time():
                            art()
                            slowprint("You and Sir Cruz sneak into the side of the building and climb up to the rooftop using the fire exit ladder.\n")
                            time.sleep(0.5)
                            slowprint(f"You successfully reach now the rooftop and finally survived the zombie apocalypse!\n\n\t\tCongratulations, {student_name}!!!\n")
                            clear_terminal()
                            exit()
                        
                        def running_time():
                            art()
                            slowprint("Both of you run into the stairs of the CBA Building. However, only you or Sir Cruz can proceed to the rooftop.\n")
                            time.sleep(0.5)
                            slowprint("The other one has to lure the zombies outside the CBA Buildin. Who should do it?\n\n")

                            def ChoiceOne():
                                art()
                                slowprint(f"You lured the zombies. Sir Cruz survived the outbreak.\nThank you for your courage, {student_name}. Game over!")
                                time.sleep(0.5)

                                exit()
                            
                            def ChoiceTwo():
                                art()
                                slowprint(f"Sir Cruz lured the zombies. You've survived the outbreak.\nCongratulations, {student_name}.")
                                time.sleep(0.5)

                                exit()
                            
                            while True:
                                slowprint("[1] You\n")
                                time.sleep(0.5)
                                slowprint("[2] Sir Cruz\n\n")
                                time.sleep(0.5)
                
                                student_choice = input("Press [1] or press [2]: ")
                                print()
                                clear_terminal()

                                if student_choice == '1':
                                    ChoiceOne()
                                    break
                                elif student_choice == '2':
                                    ChoiceTwo()
                                    break
                                else:
                                    art()
                                    slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
                        
                        while True:
                            slowprint("[1] Sneak out\n")
                            time.sleep(0.5)
                            slowprint("[2] Run\n\n")
                            time.sleep(0.5)
                
                            student_choice = input("Press [1] or press [2]: ")
                            print()
                            clear_terminal()

                            if student_choice == '1':
                                sneaky_time()
                                break
                            elif student_choice == '2':
                                running_time()
                                break
                            else:
                                art()
                                slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")

                    while True:
                        slowprint("[1] Activity Center\n")
                        time.sleep(0.5)
                        slowprint("[2] Hangar room\n\n")
                        time.sleep(0.5)
                
                        student_choice = input("Press [1] or press [2]: ")
                        print()
                        clear_terminal()

                        if student_choice == '1':
                            activity_center()
                            break
                        elif student_choice == '2':
                            hangar_room()
                            break
                        else:
                            art()
                            slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")

                
                def choiceTwo():
                    art()
                    slowprint("You left Sir Cruz and run away.\n")
                    time.sleep(0.5)
                    slowprint("You attract the zombies and you became one of them. Game over!\n\n")
                    time.sleep(0.5)

                    while True:
                        slowprint("[1] YES\n")
                        time.sleep(0.5)
                        slowprint("[2] NO\n\n")
                        time.sleep(0.5)

                        student_choice = input("Press [1] if YES or press [2] if NO: ")
                        print()
                        clear_terminal()

                        if student_choice == '1':
                            new_game()
                            break
                        elif student_choice == '2':
                            quit_game()
                            break
                        else:
                            art()
                            slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
                
                while True:
                    slowprint("[1] YES\n")
                    time.sleep(0.5)
                    slowprint("[2] NO\n\n")
                    time.sleep(0.5)

                    student_choice = input("Press [1] if YES or press [2] if NO: ")
                    print()
                    clear_terminal()

                    if student_choice == '1':
                        choiceOne()
                        break
                    elif student_choice == '2':
                        choiceTwo()
                        break
                    else:
                        art()
                        slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
                    
            
            def zombie_bite():
                art()
                slowprint("The zombie bit you. You've been eaten by the zombie. Game over!\n")
                time.sleep(0.5)
                slowprint("Do you want to try again?\n\n")
                time.sleep(0.5)

                while True:
                    slowprint("[1] YES\n")
                    time.sleep(0.5)
                    slowprint("[2] NO\n\n")
                    time.sleep(0.5)

                    student_choice = input("Press [1] if YES or press [2] if NO: ")
                    print()
                    clear_terminal()

                    if student_choice == '1':
                        new_game()
                        break
                    elif student_choice == '2':
                        quit_game()
                        break
                    else:
                        art()
                        slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
            while True:
                slowprint("[1] Attack\n")
                time.sleep(0.5)
                slowprint("[2] Run\n\n")
                time.sleep(0.5)
                
                student_choice = input("Press [1] or press [2]: ")
                print()
                clear_terminal()

                if student_choice == '1':
                    zombie_attack()
                    break
                elif student_choice == '2':
                    zombie_bite()
                    break
                else:
                    art()
                    slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
    
        def choice_two():
            art()
            slowprint("It doesn't open. You've been eaten by the zombie. Game over!\n")
            time.sleep(0.5)
            slowprint("Do you want to try again?\n\n")
            time.sleep(0.5)
                
            while True:
                slowprint("[1] YES\n")
                time.sleep(0.5)
                slowprint("[2] NO\n\n")
                time.sleep(0.5)

                student_choice = input("Press [1] if YES or press [2] if NO: ")
                print()
                clear_terminal()

                if student_choice == '1':
                    new_game()
                    break
                elif student_choice == '2':
                    quit_game()
                    break
                else:
                    art()
                    slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")

        while True:
            slowprint("[1] Look for other way to enter \n")
            time.sleep(0.5)
            slowprint("[2] Try to open the door\n\n")
            time.sleep(0.5)

            student_choice = input("Press [1] or press [2]: ")
            print()
            clear_terminal()

            if student_choice == '1':
                choice_one()
                break
            elif student_choice == '2':
                choice_two()
                break
            else:
                art()
                slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
        
    def endgame():
        art()
        slowprint("You've been eaten by the zombie. Game over!\n")
        time.sleep(0.5)
        slowprint("Do you want to try again?\n\n")
        time.sleep(0.5)

        while True:
            slowprint("[1] YES\n")
            time.sleep(0.5)
            slowprint("[2] NO\n\n")
            time.sleep(0.5)

            student_choice = input("Press [1] if YES or press [2] if NO: ")
            print()
            clear_terminal()

            if student_choice == '1':
                new_game()
                break
            elif student_choice == '2':
                quit_game()
                break
            else:
                art()
                slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
    
    while True:
        slowprint("[1] YES\n")
        time.sleep(0.5)
        slowprint("[2] NO\n\n")
        time.sleep(0.5)

        student_choice = input("Press [1] if YES or press [2] if NO: ")
        print()
        clear_terminal()

        if student_choice == '1':
            endgame()
            break
        elif student_choice == '2':
            startgame()
            break
        else:
            art()
            slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")

def quit_game():
    art()
    slowprint("You quit the game. Come play again!")
    
    exit()

while True:
    time.sleep(0.3)
    print("[1] New Game")
    time.sleep(0.3)
    print("[2] Quit Game\n")
    time.sleep(0.3)

    playerChoice = input("Do you want to play? Press [1] if YES or press [2] if NO: ")
    time.sleep(0.5)
    
    clear_terminal()

    if playerChoice == '1':
        new_game()
        break
    elif playerChoice == '2':
        quit_game()
        break
    else:
        art()
        slowprint("You enter an invalid character, please only choose between 1 & 2. :)\n\n")
        


