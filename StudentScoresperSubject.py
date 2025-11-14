nstudents = int(input("Enter number of students:"))
nsubject = int(input("Enter number of subjects:"))
average = 0
grade = 0
c_av=0
for i in range(1,nstudents+1):
    average = 0
    print("Student ",i)
    for j in range(0,nsubject):
        grade=0
        grade=int(input("Enter Score:"))
        average+=grade
    average = average/nsubject
    print("Average for Student ", i, " = ",average)
    c_av+=average
c_av=c_av/nstudents
print("Class Average = ", c_av)