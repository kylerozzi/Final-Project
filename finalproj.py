#Kyle Rozzi

print("Hi there! Welcome to Adventure of the Cave! Make decisions to alter the game and end victorious!")

q1 = input("You are taking your regular walk in the forest. You look to your right and catch sight of a cave. Do you enter? Enter “Y” for yes and “N” for no: ")

if q1 == "N":
    print("You lack a sense of adventure: GAME OVER")
elif q1 == "Y":
    q2 = input("You enter the cave, and you see a lantern on the ground.Do you pick it up?  Enter “Y” for yes and “N” for no: ")
    if q2 == "N":
        print("You’re in a dark cave and you don’t pick up a lantern - smart move: GAME OVER")
    elif q2 == "Y":
        q3 = input("You pickup the lantern and continue walking further into the cave. At some point, you catch sight of a sword and a gold brick sitting next to one another on the ground. You can only take one because of the lantern. Enter “S” for sword and “G” for the gold brick: ")
        if q3 == "G":
            q4 = input("Although it’s heavy you are able to proceed further into the cave. At some point, you catch sight of a door being guarded by sleeping wolf. You can either decide to turn around and go back or quietly go past the dog through the door: Enter “T” for turn around and “Q” for quietly going past: ")
            if q4 == "T":
                print("You are a coward: GAME OVER")
            elif q4 == "Q":
                q5 == input("You quietly sneak through the door without waking the wolf, but once you enter the new section of the cave, you are confronted by a massive figure. The figure bellows “Turn around or Die!” You can either attempt to bribe them with the gold brick or club them over the head with it: Enter “B” to bribe and “C” to club: ")
                if q5 == "B":
                    print("You attempt to bribe the figure, and they respond with “Ha-Ha, foolish traveler. I only accepts bribes of swords. Not worthless gold bricks.” The figure proceeds to kill you: Game Over")
                elif q5 == "C":
                    q6 = input("You club the figure over the head and it works! You are free to continue through the cave. After a while, you reach the end of the cave. There are two rooms that you can enter. One of them is filled with treasure and the other has a puppy. Which do you choose: Enter “T” for the treasure room and “P” for the puppy room: ")
                    if q6 == "P":
                        q7 = input("You enter the room. You have the choice to take a puppy home and care for it as your own:  Enter “Y” to take the puppy and “N” to leave empty handed: ")
                        if q7 == "N":
                            print("You want to end your adventure empty handed? Well, it's your prerogative - Thank you for playing: The End")
                        elif q7 == "Y":
                            print("Fantastic decision. You take home the puppy and end up with a great companion. A successful adventure, I’d say: The End")

                    elif q6 == "T":
                        q8 = input("You enter the room. You have the choice to take as much treasure as you can or head home empty handed:  Enter “Y” to take the treasure and “N” to leave empty handed: ")
                        if q7 == "N":
                            print("You want to end your adventure empty handed? Well, it's your prerogative - Thank you for playing: The End")
                        elif q7 == "Y":
                            print("Fantastic decision. You take home the treasure and find yourself incredibly rich. A successful adventure, I’d say: The End")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
            

        elif q3 == "S":
            q4 = input("Sword at your side, you proceed further into the cave. At some point, you catch sight of a door being guarded by sleeping wolf. You can either decide to turn around and go back or quietly go past the dog through the door: Enter “T” for turn around and “Q” for quietly going past: ")
            if q4 == "T":
                print("You are a coward: GAME OVER")
            elif q4 == "Q":
                q5 == input("You quietly sneak through the door without waking the wolf, but once you enter the new section of the cave, you are confronted by a massive figure. The figure bellows “Turn around or Die!” You can either attempt to bribe them with the gold brick or club them over the head with it: Enter “B” to bribe and “C” to club: ")
                if q5 == "B":
                    print("You attempt to bribe the figure, and they respond with “Ha-Ha, foolish traveler. I only accepts bribes of swords. Not worthless gold bricks.” The figure proceeds to kill you: Game Over")
                elif q5 == "C":
                    q6 = input("You club the figure over the head and it works! You are free to continue through the cave. After a while, you reach the end of the cave. There are two rooms that you can enter. One of them is filled with treasure and the other has a puppy. Which do you choose: Enter “T” for the treasure room and “P” for the puppy room: ")
                    if q6 == "P":
                        q7 = input("You enter the room. You have the choice to take a puppy home and care for it as your own:  Enter “Y” to take the puppy and “N” to leave empty handed: ")
                        if q7 == "N":
                            print("You want to end your adventure empty handed? Well, it's your prerogative - Thank you for playing: The End")
                        elif q7 == "Y":
                            print("Fantastic decision. You take home the puppy and end up with a great companion. A successful adventure, I’d say: The End")

                    elif q6 == "T":
                        q8 = input("You enter the room. You have the choice to take as much treasure as you can or head home empty handed:  Enter “Y” to take the treasure and “N” to leave empty handed: ")
                        if q7 == "N":
                            print("You want to end your adventure empty handed? Well, it's your prerogative - Thank you for playing: The End")
                        elif q7 == "Y":
                            print("Fantastic decision. You take home the treasure and find yourself incredibly rich. A successful adventure, I’d say: The End")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass