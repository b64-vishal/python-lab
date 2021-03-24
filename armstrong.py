n=int(input("enter a number"))
s=0
temp=n
while(temp>0):
    r=temp%10
    s=s+r**3
    temp=temp//10
if n==s:
    print("armstrong number")
else:
    print("not an armstrong number")
    
