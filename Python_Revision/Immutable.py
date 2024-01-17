# *When to variable have same data , python at run time wont allocate 2 spaces for 
# *the both the variable it will create one space and point both variables to same location
# *as they are having same data is called immutable.

a = 10
b = 10 
print(a,b)
print(id(a))  # id is used to identify the address of the memory space where the value is stored
print(id(b))

a = 10
b = 20
print(a,b)
print(id(a))
print(id(b))

#Assignments
print("Assignments")
lst = ["India","USA","UK"]
print(lst)
lst.append("Cannada")
print(lst)
del lst[1]
print(lst)
lst.insert(1,"USA")
print(lst)

# SET
print("\n SET")
st = {"India","USA","UK"}
print(st)
st.add("Cannada")
print(st)
st.remove("USA")
print(st)
lst1 = ["Africa","Asia"]
st.update(lst1)
print(st)


a = 10 
del a
print(a)
