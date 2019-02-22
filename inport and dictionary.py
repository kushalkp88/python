import random
d = {8:54,56:32,51:84,42:61,46:12,31:45}

p = random.choice([8,54,56,51,84,61,31,46]) 

print("you got",p)

if p in d:
	if p > d[p]:
		printf("snake")
	else:
		print("lader")

	print("you can go to",d[p])