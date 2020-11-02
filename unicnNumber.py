list1=[1,2,3,4,5,6]
list2=[2,3,4,1,9,8]
i=0
list3=[]
while(i<len(list1)):
    j=0
    while(j<len(list2)):
        if list1[i]==list2[j]:
            list3.append(list1[i])
        j=j+1
    i=i+1
print(list3)
        