gold = []
inventory = ["nothing"]
import weapons

while True:
    user_name = input("please enter your username ").strip().lower()
    print(f"hello {user_name}")

    print("please note this game has no checkpoints at this moment in time. If you exit the game, you will lose everything. However, if you die, you will respawn close to where you died.")
    choice = input("are you ready to start? [yes/no] ")
    if choice == "yes":
        break

    if choice == "no":
        print("ok goodbye")
        exit()

while True:
    choice = input("you wake up in a cave with your arms chained to two torches. What do you do? [break the chains/wait] ")
    if choice == "break the chains":
        print("You break out of the chains with ease and notice a rusty small dagger to your left. You hear running footsteps on your right.")
        break

    if choice == "wait":
        print("As you wait, you hear footsteps getting closer and closer. Suddenly, everything goes black and you fall dead.")
        choice = input("Would you like to try again? [yes/no] ")
        if choice == "yes":
            continue
        if choice == "no":
            exit()

while True:
    choice = input("Do you take the rusty dagger? [yes/no] ")
    if choice == "yes":
        print("You pick up the rusty dagger as you hear the people running are getting scarily close to you.")
        print("RUSTY DAGGER HAS BEEN ADDED TO YOUR INVENTORY")
        inventory.remove("nothing")
        inventory.append(weapons.get_dagger())
        break

    if choice == "no":
        print("You leave the dagger on the floor as you hear the people running getting closer and closer.")
        break

if any(item.get("name") == "Rusty Dagger" for item in inventory):
    while True:
        print("as you hold the dagger in your hand two men in black robes burst though the entrance")
        choice = input("do you fight or run [fight/run]")
        use_item = input(f"what item would you like to use from your invintory? {inventory} ")
        if user_name in inventory:
            print(f"you take out your {use_item} and get ready to fight.")
        break
else:
    while True:
        print("No dagger lol")
        break
