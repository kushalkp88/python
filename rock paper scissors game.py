#rock paper scissors game
import random
l=["r","p","s"]

u=input("enter your choice")

c=random.choice(l) 
print("comp chooses",c)

if u==c:
    print("tie")
elif u==r and c==p: u==s and c==r: and u==p and c==s:
    print("comp wins")
elif c==r and u==p: c==s and u==r: and c==p and u==s:
    print("you win")