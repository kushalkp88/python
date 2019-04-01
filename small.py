x=int(input("Enter number "))
y=int(input("Enter number "))
z=int(input("Enter number "))
def small(x,y,z):
	if(x<y and x<z):
		return(x)
	elif(y<z and y<x):
		return(y)
	else:
		return(z)	
a=small(x,y,z)
print(a)
