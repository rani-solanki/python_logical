user=input("enter the string:>")
index_number = 0
count_lowercase =0
count_uppercase=0
while(index_number<len(user)):
    if user[index_number].islower():
        count=count+1
    elif user[index_number].isupper():
        cou=cou+1
    index_number=index_number+1
print("number of lower case",count)
print("number of upper case",cou)


