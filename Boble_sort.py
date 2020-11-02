list=[2,1,0,8,-9,-6,5,-2,3,5]
index=0
while(index<len(list)):
    b=[]
    j=0
    while(j<len(list)-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
        j=j+1
    b.append(list)
    index=index+1
print(b)
