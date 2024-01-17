# Lambda
f = lambda a = 20:"Yes" if(a%2 == 0) else "No"

result = f(a=10)
print(result)

result = f(a=15)
print(result)

result = f()
print(result)