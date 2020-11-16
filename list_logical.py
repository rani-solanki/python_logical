# in this question we have to count string value that in side. 
# the string first element and last element it is same.
sample_List=['abc', 'xyx', 'abv', '122f']
i=0
b=[]
conut=0
while(i<len(sample_List)):
    j=0
    a=[]
    while(j<len(sample_List[i])):
        h=sample_List[i][j]
        a.append(h)
        j=j+1
    b.append(a)
    if a[0]==a[-1]:
        conut=conut+1
    i=i+1
print(b)







print(conut)
user=int(input( ))
print(type(user))
i=0
if user==i:
    prin("yes")