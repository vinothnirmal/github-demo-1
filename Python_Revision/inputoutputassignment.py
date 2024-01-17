print("Pick any 3 items from the below items :\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format("1. Onions","2. Lettuce","3. Tomato","4. Olives","5. Peppers","6. Tomatoes"))
lstitems = [x for x in input("Enter 3 items separated by comma(,)").split(",")]
length = len(lstitems)
if(length <= 3):
    print("List of items chosen : {}".format(lstitems))
    print("Total bill : ", length*5)
else:
    print("Cannot choose more than 3 items, try again")