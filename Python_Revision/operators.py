#Comparison operator

x = 10
y = 20
z = 10

print(x == z)
print(y == z)


# logical or , and , Not opeartors
print(x == z and y == z)
print(not(x == z and y == z))
print(x == z or y == z)
print("Not opearot",x != z)

#identity operator
x = "python"
y= "programming"
print("identity operator 1",x is y)
print("identity operator 2",x is not y)

x = 50
a = [10,20,30]
b = [40,50,60]
c = a
print("identity operator 3",a is c)
print("identity operator 4",a is not c)
print(x in b)

#Data types
a = 10 < 5
print("Data Types 1", a)
print("Data Type of a",type(a))
name = 'Python'
print("Datatype of name", type(name))
print("Index of string "+ name + ": ", name[0])
print("Index of string "+ name + ": ", name[3])
length = len(name) - 1 
print("Index of string "+ name + ": ", name[len(name) - 1])

# list
my_list = [1,2,3,4,5,6,7]
print("list : ", my_list)
my_list.insert(1,0)
print("list after insert", my_list)
print("print list of specific range :", my_list[1:3])
print("print list of specific range :", my_list[-3:-1])

#dicitonary
my_dict = {10:"Vino",2:"Sathya"}
print(my_dict.get(2))
my_dict[10] = "Vinoth"
print(my_dict)
print(my_dict.pop(2))
print(my_dict)
my_dict[3] = "Thanu"
my_dict.update()
print(my_dict)

#tuple
my_tuple = (10,20,30,40,40)
print(my_tuple)

#set
my_set = {10,20,30,40,40}
print(my_set)

#range
my_range = list(range(1,10,2))
print(my_range)

my_range = tuple(range(1,12))
print(my_range)