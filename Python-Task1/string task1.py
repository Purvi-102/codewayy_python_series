
#String concatenation using + operator
fname=input()
lname=input()
name=fname  + lname
print(name)

#String concatenation using join method
colgname=input()
address=input()
info=(" ".join(colgname,address))
print(info)

# marks of 5 different subjects
sub1=float(input())
print(sub1)
sub2=float(input())
print(sub2)
sub3=float(input())
print(sub3)
sub4=float(input())
print(sub4)
sub5=float(input())
print(sub5)

#Calculate total marks
total_marks=sub1+sub2+sub3+sub4+sub5
print(total_marks)

#Calculate percentage
per_marks=((total_marks)/5)*100
print(total_marks)

