#exceptional handeling
try:
	s=1
	print(s)
except:
	print("error")
else:
	print("hii")
finally:
	print("sucess")

#exceptional handeling
try:
	#r=1
	print(r)
except:
	print("error")
else:
	print("hii")
finally:
	print("sucess")


try:
	#q=1
	print(q)
	raise NameError
except NameError:
	print("u have not defined s")
except:
	print("unsucess")
else:
	print("hii")

finally:
	print("sucess")


'''
try:
	#g=1
	print(g)
	raise kusHal
except kusHal:
	print("u have not defined s")
except:
	print("unsucess")
else:
	print("hii")

finally:
	print("sucess")
'''