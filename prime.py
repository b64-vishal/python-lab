n=int(input("enter any no ="))
for i in range(2,n):
    if i%n==0:
        print("not a prime")
        break
else:
    print("prime number")
