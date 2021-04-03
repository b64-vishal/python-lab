n=int(input("enter any number"))
s=0
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
print("the reverse number is ",s)
