#excpet
try:
	a=int(input("enter number\n"))
	if(a>3):
		print("b=",a/(a+3))
except:
	print("zero error")
except:
	print("great")
finally:
	print("successful")