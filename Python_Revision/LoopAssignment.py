n = int(input("Enter number : "))
lst = []
# for i in range(1,n):
#     lst.append(i)
# print(lst)
while n > 0:
    for i in range(1,n):
        if(i%10 != 0):
          print(i)
        if(i==n-1):
            break
    break