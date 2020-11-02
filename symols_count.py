string="{{{}}{{}}{{{}}}}"
i=0
count=0
count1=0
while(i<len(string)):
    if string[i]=="{":
        count=count+1
    elif string[i]=="}":
        count1=count1+1
    i=i+1
if count==count1:
    print("True")
else:
    print("False")