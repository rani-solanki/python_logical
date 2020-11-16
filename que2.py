# a=[6,2,3,8]
# i=1
# b=[]
# while(i<=max(a)):
#     b.append(i)
#     i=i+1
# print(b)
# m=[]
# k=2
# while(k<len(b)):
#     if b[k] not in a:
#         m.append(b[k])
#     k=k+1
# print(len(m))
def makeArrayConsecutive2(statues):
    a=min(statues)
    b=max(statues)
    count=0
    for i in range(a,b):
        if i not in statues:
            count+=1
    print(count)
makeArrayConsecutive2([5,4,6])