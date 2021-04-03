ch=input("enter the string")
alphabet=digit=special=space=0
for i in range(len(ch)):
    if(ch[i].isalpha()):
        alphabet+=1
    elif(ch[i].isdigit()):
        digit+=1
    else:
        special+=1
print("total number of aphabet :" ,alphabet)
print("totsl number of digit :", digit)
print("total number of special character :",special)
