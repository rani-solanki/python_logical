list=[[1,2,3,4],[4,5,6,7],[3,4,5,6]]
a=[]
i=0
while(i<len(list)):
    j=0
    while(j<=len(list)-1):
        a.append(list[i][j])
        j=j+1
    i=i+1
# print(a)
x=0
while(x<len(a)):
    y=0
    count=0
    while(y<len(a)):
        if(a[x]==a[y]):
            count=count+1
        y=y+1
    x=x+1
    print(a[x],count)