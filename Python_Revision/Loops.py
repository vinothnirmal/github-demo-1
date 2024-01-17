usr_range = int(input("Enter the range : "))
if not str(usr_range):
    usr_range = 0
while(usr_range != 0):
   x = list(range(1,usr_range))
   print(x)
   for i in x:
       if(i%2 == 0):
           print(str(i) + " is even")
       else:
           print(str(i) + " is odd")
   usr_range = int(input("Press 0 if you want to exit : "))
   if(usr_range == 0):
       break
   else:
       usr_range = int(input("Enter the range : "))
else:
    print("Range cannot be zero or empty")
   