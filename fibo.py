n=int(input("Enter a number untill which fibo series is needed:"))
a,b=0,1
c=0
for i in range(0,n):
	if(i==0):
		c=0
		print(c)
	elif(i==1):
		c=1
		print(c)
	else:
		c=a+b
		a=b
		b=c
		print(c)
 

