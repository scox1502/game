while True:
    user_name = input("please enter your name. ").strip().lower()
    print(f"hello {user_name}")

    print("please note this game has no checkpoints at this momant in time and is in early beta stages")
    choice = input("are you ready to start? [yes/no] ")
    if choice == "yes":
        break

    if choice == "no":
        print("ok goodbye")
        exit()

while True:
    choice = input("you wake up in a cave with your arms chaned to two torches what do you do [try and break the chanes/wait] ")
    if choice == "try and break the chanes":
        break

    if choice == "wait":
        print("as you wait you hear footsteps getting closer and closer and as they enter you see... nothing but before anythig else everything goes black and you fall dead")
        
        choice = input("would you like to try again? [yes/no] ")
    if choice == "yes":
        pass
    
    if choice == "no":
        exit()

