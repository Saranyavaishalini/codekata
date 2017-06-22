a=input("enter the number")
rev=0
sum=0
print(str(a))
while(a>0):
	rev=a%10
	sum=(sum*10)+rev
	a=a//10
print(sum)
