list = [1,2,4,5,2,3,9,8,1,2,10,3,4,9]
i=0
list1=[]
while(i<len(list)):
    j=0
    count=0
    while(j<len(list)):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    k=list[i],count
    if k not in list1:
        list1.append(k)
    i=i+1
print(list1)