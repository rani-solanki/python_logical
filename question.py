# list = [1, 2, 3, 2, 4, 2, 4, 5, 6, 3, 2]# count occurence question
# list = [1, 2, 3, 2, 4, 2, 4, 5, 6, 3, 2]
# i =0
# list1=[]
# while(i <len(list)):
#     j = 0
#     count=0
#     while(j <len(list)):
#         if list[i] not in list1:
#             list1.append(list[i])
#         j=j+1
#     i=i+1
# print(list1)

# count occurence question
list = [1, 2, 3, 2, 4, 2, 4, 5, 6, 3, 2]
i =0
list1=[]
while(i <len(list)):
    j = 0
    count=0
    while(j <len(list)):
        if list[i] not in list1:
            count=count+1
            a=count,list[i]
            list1.append(a)
            break
        j=j+1
    i=i+1
print(list1)




# user=int(input("enter the number"))
# sum=0
# for i in range(1,user):
#     sum=sum+i
# print(sum)
# def sum(number):
#     fo
#         return i*sum(i+1) 
# user=int(input("enter the number"))
# print(sum(i))

# def factorial(number):
#     if number==1:
#         return number
#     else:
#         return number*factorial(number-1)
# print(number)