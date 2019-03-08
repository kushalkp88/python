def max(a,b,c):
	if (a>b and a>c):
		return a
	elif (b>a and b>c):
		return b
	else: 
		return c


a=input("first number")
b=input("secod number")
c=input("third number")

m=max(a,b,c)
print(m, "is the largest")