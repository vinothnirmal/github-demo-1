import sys

lst = sys.argv

# Assignment
bal = 10000
print("Options available : \n\t{}\n\t{}\n\t{}\n\t{}".format("1. Check Balance","2. Withdraw","3. Deposit Cash","4. Deposit Check"))
option = int(lst[1])
match option:
    case 1:
        print("Balance is : ",bal)
    case 2:
        draw = int(input("Enter the amount to withdraw : "))
        print("Amount withdrawn successfully")
        bal = bal - draw
        print("Balance is", bal)
    case 3:
        deposit = int(input("Enter the amount to deposit : "))
        print("Amount deposited successfully")
        bal = bal + deposit
        print("Balance is", bal)