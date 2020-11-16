User=int(input("enetr the number"))
count=0
while(User > 0):
    d=User % 10
    User=User//10
    print(User)
    count=count+1
print(count)


sum=int(input("enter the number"))
s=0
while(sum>0):
    f=sum % 10
    s=s+f**2
    sum=sum//10
print(s)
