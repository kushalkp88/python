#rps
import random
l=["r","p","s"]
while True:
	u=input("enter your choice,press q to quit")
	if u=='q':
		print("thank you")
		exit()
	c=random.choice(l) 
	print("comp chooses",c)

	if u==c:
		print("Damn,tie")
	elif (u=="r" and c=="p") or (u=="s" and c=="r") or (u=="p" and c=="s"):
		print("Hell comp wins")
	elif (c=="r" and u=="p") or (c=="s" and u=="r") or (c=="p" and u=="s"):
		print("Hoo rey! you win")