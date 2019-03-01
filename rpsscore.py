	#rock paper scissors game
#calling random module for choosing a string from tuple using .choice function
import random
p = 0
c = 0
i = 0
a = ("rock", "papers", "scissors")

opt = input("Press s to start and q to quit ")
if opt == "s":
    print("Lets start this game")

    while i<6:

        com = random.choice(a)

        player = input("Type q to quit\nType rock or papers or scissors: ")

        if player == "rock" or player == "papers" or player == "scissors":
            print("Computer chose", com, "and You chose", player)

            if (player == "rock" and com == "scissors") or (player == "papers" and com == "rock") or \
                    (player == "scissors" and com == "papers"):
                print("Yes! you win")
                p = p+1
            elif (player == "scissors" and com == "rock") or\
                    (player == "rock" and com == "papers") or (player == "papers" and com == "scissors"):
                print("Damn! computer wins")
                c = c+1
            elif player==com:
                print("Lol! it's a tie")
            print("Your score is", p, "and Computer's score is", c)
        elif player=="q":
        	print("Thanks for playing!")
        	quit()
        else:
            print("give a valid input")
        i+=1
        continue
elif opt == "q":
    print("Thanks for not playing!")
    quit()
if(p>c):
    print("You win!!!")
else:
    print("you loss!!!")
       	