def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

  
l=[1,2,3,4,5,6,7,8,9,10]

for k in range(10):
    print(Fibonacci(l[k]))