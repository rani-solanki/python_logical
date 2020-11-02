# list sorting use two loop
# list = [1, 0, 0, 0, 1, 1,1, 1, 0]
# i = 0
# while(i<len(list)):
#     b=[]
#     j = 0
#     while(j < len(list)-1):
#         if list[j] > list[j+1]:
#             temp=list[j]
#             list[j]=list[j+1]
#             list[j+1]=temp
#         j =j+1
#     b.append(list)
#     i=i+1
# print(b)


# list sorting use of a loop
list = [1, 0, 0,0, 0, 1, 1,1, 1, 0]
less_than_list =[]
greter_than_list =[]
i=0
while(i<len(list)):
    if list[i]==0:
        less_than_list.append(list[i])
    elif list[i]==1:
        greter_than_list.append(list[i])
    i=i+1
print(less_than_list+greter_than_list)