# lambda arguments : expression
x = lambda a : a + 10
print(x(5))
def function(b):
    return lambda a:a*b
mycoder=function(2)
mysolder=function(6)
mymoler=function(7)

print(mycoder(11))
print(mysolder(44))


# lamda function
y=lambda b:b + 5
print(y(5))

# how to print function
x = lambda a, b : a * b
print(x(5, 6))
# use ofthree argument
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

# how to inside function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 
# how to use return fuction
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
# how to use return function 
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
# how to use two argumentnt
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
# 