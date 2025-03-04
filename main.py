gold = []
invintory = []
while True:
    user_name = input("please enter your username ").strip().lower()
    print(f"hello {user_name}")

    print("please note this game has no checkpoints at this momant in time so if you exit the game you will lose everything altho if you die you will respon close to where you died")
    choice = input("are you ready to start? [yes/no] ")
    if choice == "yes":
        break

    if choice == "no":
        print("ok goodbye")
        exit()

while True:
    choice = input("you wake up in a cave with your arms chaned to two torches what do you do [break the chanes/wait] ")
    if choice == "break the chanes":
        print("you break out of the chanes with ease and notice a rusty small dagger to your left and you hear running footsteps on your right")
        break

    if choice == "wait":
        print("as you wait you hear footsteps getting closer and closer and as they enter you see... nothing but before anythig else everything goes black and you fall dead")
        
        choice = input("would you like to try again? [yes/no] ")
    if choice == "yes":
        pass
    
    if choice == "no":
        exit()

while True:
    choice = input("do you take the rusty dagger? [yes/no] ")
    if choice == "yes":
        print("DAGGER HAS BEEN ADDED TO YOUR INVINTORY")
        invintory.append("dagger")
        break
    if choice == "no":
        print("you leave the dagger on the floor as your hear the people running get closer and closer")
        break

