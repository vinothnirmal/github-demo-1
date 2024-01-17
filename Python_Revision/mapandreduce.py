from functools import reduce

lst = [10,20,30,4,7,9]

f = map(lambda x:x**2,lst)
print(list(f))

f = reduce(lambda x,y:x+y,lst)

print(f)