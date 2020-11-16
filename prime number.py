num=int(input("enter the numebr"))
if num%2!=0 and num%3!=0:
    print("prime number")
else:
    print("not prime number")


n=23
i=1
cont=0
while(i<=n):
    if n%i==0:
        cont=cont+1
    i=i+1
if cont==2:
    print("prime number")
else:
    print("not prime number")

