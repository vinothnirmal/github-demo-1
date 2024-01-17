lst = []
for i in range(10):
    lst.append(i)
print(lst)
f = map(lambda x:x**3,lst)
print(list(f))

# List comprehension

lst = [x**3 for x in range(10)]
print(lst)