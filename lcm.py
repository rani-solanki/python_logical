num1=int(input("enter the umber"))
num2=int(input("enter the number"))
index=2
while(num1>0):
    if index%num1==0 and index%num2==0:
        print(index)
        num1=0
    index=index+1
