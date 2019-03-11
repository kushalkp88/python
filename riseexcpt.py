#riseexcpt
try:
	a=[1,2,3,4,5,6]
	print(a[7])
	raise IndexError
except IndexError:
	print("IndexeRRor")