b= list()
a= "yes"
while(a=="yes"):
        c=input()
        b.append(c)
        print('you want to continue shopping')
        a=input()
b.sort(key=len)
print(b)
