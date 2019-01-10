#Kyle Rozzi
#Computer Programming Final Project
#Adventure of the Cave
from random import randint
boss = randint(0,2)

print("Welcome to Adventure of the Cave! Make decisions to alter the \
game and end victorious!")

q1 = input("You are walking through the forest and catch sight of a \
cave. Do you enter? Enter “Y” for yes and “N” for no: ")

if q1 == "N":
    
    print("You lack a sense of adventure: GAME OVER")
    
elif q1 == "Y": 
    
    rps = input("Immediately, you confront a massive creature. It announces that 'You \
may only pass if you best me in a game of rock paper scissors. What \
do you chose': Enter R for Rock, P for paper and S for Scissors: ")

    if rps == 'R':
        win = 'Scissors'
    elif rps == 'S':
        win = 'Paper'
    elif rps == 'P':
        win = 'Rock'


    if boss == 2:
        if rps == 'R':
            print("The creature chooses paper and proceeds to crush your \
puny head: GAME OVER")
        elif rps == 'P':
            print("The creature chooses scissors and proceeds to crush your \
puny head: GAME OVER")
        elif rps == 'S':
            print("The creature chooses rock and proceeds to crush your puny \
head: GAME OVER")

    elif boss == 1:
        if rps == 'R':
            print("The creature chooses rock as well and announcse that 'A Tie \
won't save you'.\
He proceeds to crush your puny head: GAME OVER")
        elif rps == 'P':
            print("The creature chooses paper as well and announcse that 'A Tie \
won't save you'.\
He proceeds to crush your puny head: GAME OVER")
        elif rps == 'S':
            print("The creature chooses rock as well and announcse that 'A Tie \
won't save you'.\
He proceeds to crush your puny head: GAME OVER")
    elif boss == 0:
        print('The creature chooses',win,'and you win!')
        q3 = (input('After proceeding through the cave for some time you \
catch sight of a sword and a gold brick. \
You can only take one. Enter “S” for sword \
and “G” for the gold brick: '))
        if q3 == "G":
            q4 = input("You proceed further into the cave. You come across \
a door being guarded by sleeping wolf. You can either \
turn around and go back or quietly sneak past the wolf \
: Enter “T” for turn around and “Q” for quietly going past: ")
            if q4 == "T":
                print("You are a coward: GAME OVER")
            elif q4 == "Q":
                q5 = input("You quietly sneak past, but are immediately confronted \
by a massive figure. The figure bellows “Turn \
around or Die!” You can either attempt to bribe them with the \
gold or club them over with head with it: Enter “B” to bribe and “A” to attack: ")
                if q5 == "B":
                    print("You attempt to bribe the figure, and they respond with \
“Ha-Ha, foolish traveler. I only accepts bribes of swords. Not worthless gold \
bricks.” The figure proceeds to kill you: Game Over")
                elif q5 == "C":
                    q6 = input("You club the figure over the head and it works! \
After a while, you reach the end of \
the cave. There are two rooms that you can enter. One of them is filled with \
treasure and the other has a puppy. Which do you choose: Enter “T” for the \
treasure room and “P” for the puppy room: ")
                    if q6 == "P":
                        q7 = input("You enter the room. Enter “Y” to take the \
puppy home and “N” to leave empty handed: ")
                        if q7 == "N":
                            print("You want to end your adventure empty handed? \
Well, it's your prerogative - Thank you for playing: The End")
                        elif q7 == "Y":
                            print("Fantastic decision. You take home the puppy \
and end up with a great companion. A successful adventure, I’d say: The End")

                    elif q6 == "T":
                        q8 = input("You enter the room. Enter “Y” to take the treasure and \
“N” to leave empty handed: ")
                        if q8 == "N":
                            print("You want to end your adventure empty handed? Well, \
it's your prerogative - Thank you for playing: The End")
                        elif q8 == "Y":
                            print("Fantastic decision. You take home the treasure and \
find yourself incredibly rich. A successful adventure, I’d say: The End")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
            

        elif q3 == "S":
            q9 = input("You proceed further into the cave. You come across \
a door being guarded by sleeping wolf. You can either \
turn around and go back or quietly sneak past the wolf \
: Enter “T” for turn around and “Q” for quietly going past: ")
            if q9 == "T":
                print("You are a coward: GAME OVER")
            elif q9 == "Q":
                q10 = input("You quietly sneak past, but are immediately confronted \
by a massive figure. The figure bellows “Turn \
around or Die!” You can either attempt to bribe them with the \
sword or attack them with it: Enter “B” to bribe and “A” to attack: ")
                if q10 == "A":
                    print("You attempt to attack the figure, but it is \
unsuccessful. The figure responds with “Ha-Ha, foolish traveler. \
I can only be defeated when clubbed with a gold brick, not a puny sword” \
The figure proceeds to kill you: Game Over")
                elif q10 == "B":
                    q11 = input("You attempt to bribe the figure with the sword and it \
works! After a while, you \
reach the end of the cave. There are two rooms that you can enter. \
One of them is filled with treasure and the other has a puppy. Which \
do you choose: Enter “T” for the treasure room and “P” for the puppy room: ")
                    if q11 == "P":
                        q12 = input("You enter the room. Enter “Y” to take the puppy home \
and “N” to leave empty handed: ")
                        if q12 == "N":
                            print("You want to end your adventure empty handed? Well, it's \
your prerogative - Thank you for playing: The End")
                        elif q12 == "Y":
                            print("Fantastic decision. You take home the puppy and end \
up with a great companion. A successful adventure, I’d say: The End")
                    elif q11 == "T":
                        q13 = input("You enter the room. Enter “Y” to take the treasure \
and “N” to leave empty handed: ")
                        if q13 == "N":
                            print("You want to end your adventure empty handed? Well, \
it's your prerogative - Thank you for playing: The End")
                        elif q13 == "Y":
                            print("Fantastic decision. You take home the treasure and \
find yourself incredibly rich. A successful adventure, I’d say: The End")
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