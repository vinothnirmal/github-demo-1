print("Enter the marks of student in below subjects :\n\t{}\n\t{}\n\t{}".format("1. Maths","2. Physics","3. Chemistry"))
Maths,Physics,Chemistry = [int(x) for x in input("Enter 3 subbject marks separated by comma(,)").split(",")]
print(Maths,Physics,Chemistry,sep=',')
if(Maths > 35 and Physics > 35 and Chemistry > 35):
    avg = (Maths + Physics + Chemistry)/3
    if(avg <= 59):
        print("Grade : C")
    elif(avg <= 69):
        print("Grade : B")
    else:
        print("Grade : A")
else:
    print("Fail")