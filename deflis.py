def sum(a):
	i = 0
	for e in a:
		i=i+e
	return i;

a=[]
n= int(input("number of element in list"))
for k in range(n):
	el = int(input("give the elements of list"))
	a.append(el)

i = sum(a)

print(i, "is sum of list")