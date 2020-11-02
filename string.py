# # use of rstrip 
# string = '  Hello  World   From Pankaj \t\n\r\tHi There '
# f=string.rstrip()
# print(f)

book={ }
plce=book['bob']={
    'name':'Rani solanki',
    'school':'Gov.girl school',
    'mobaile':236876498250
}
book['mob']={
    'name':'rinki',
    'school':'gov.girl school',
    'phone':7687697080
}
def internet_one(response):
    for i in response:
        print(response[i],i)        
internet_one(plce)
print(plce)

