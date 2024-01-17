def argskwargs(x,*args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
    modfies_args = args + (40,)
    argskwargsfun1(*modfies_args,**kwargs)   

def argskwargsfun1(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key,value in kwargs.items():
        print(key,value)
    
argskwargs(10,20,30,name = "vinoth",sal = "100000")