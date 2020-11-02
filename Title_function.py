# string_name="i am rani solanki"
# list1=string_name.split()
# for i in list1:
#     print(i.capitalize())
    

string_name="i am rani solanki"
string = string_name.split()
list1=list(string)
for i in list1:
    for j in range(len(i)):
        if j==0:
            temp=i[0]
            print(temp.upper())
            if j==" ":
                print(5*" ")
        else:
            print(i[j])
        

# name=" i am rani solanki"
# for i in name:
#     if i==" ":
#         print()
#     else:
#         print(i,end="")
# print()