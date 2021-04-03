ch=input("enter any character ")
if (ch>='a' and  ch<='z'):
    print("lowercase alphabet")
elif (ch>='A' and ch<='Z'):
    print("uppercase alphabet")
elif(ch>='0' and ch<='9'):
    print("digit")
else:
    print("special character")
