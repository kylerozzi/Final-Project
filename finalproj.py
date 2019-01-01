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
                
            
            
            else:
                pass
            
            
            

        elif q3 == "S":
            print("Sword at your side, you proceed further into the cave. At some point, you catch sight of a door being guarded by sleeping wolf. You can either decide to turn around and go back or quietly go past the dog through the door: Enter “T” for turn around and “Q” for quietly going past: ")
            
        else: 
            pass
            
    else:
        pass

else:
    pass
    