family = { "name" : {"vinoth","sathya","thanu","sirpi"}, "age" : {36,28,8,3}}
my_list = list(family.get("name"))
print(my_list)
my_new_list = []
length = len(my_list)
print(tuple(range(length,0,-1)))
for i in tuple(range(length,0,-1)):
  print(my_list[i-1])
  my_new_list.append(my_list[i-1])
  
print(my_new_list)