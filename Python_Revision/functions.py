#function without parameters
def functioncall():
    print("Hello world")

#fucntion with parameters
def add(x,y):
    z = x + y
    return z

#lambda functions
sub = lambda x,y : x-y
call = lambda : functioncall()


a = str(add(1,2))
print(sub(4,2))
print(a)
#functioncall()
call()