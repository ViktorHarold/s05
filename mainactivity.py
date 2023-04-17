print("\nThis is a program wherein you, the user, will be entering the grades of 5 students \non 5 Class Participations/Enabling Assessments, 3 Summative Assessments, and Final \nExamination to compute for the average and its corresponding letter grade.\n")
students = []
for X in range(5):
    print("\n")
    surname = input("Please enter the student's surname: ")
    cp1 = int(input("Please enter your grade on your 1st Class Participation/Enabling Assessment: "))
    cp2 = int(input("Please enter your grade on your 2nd Class Participation/Enabling Assessment: "))
    cp3 = int(input("Please enter your grade on your 3rd Class Participation/Enabling Assessment: "))
    cp4 = int(input("Please enter your grade on your 4th Class Participation/Enabling Assessment: "))
    cp5 = int(input("Please enter your grade on your 5th Class Participation/Enabling Assessment: "))
    sa1 = int(input("Please enter your grade on your 1st Summative Assessment: "))
    sa2 = int(input("Please enter your grade on your 2nd Summative Assessment: "))
    sa3 = int(input("Please enter your grade on your 3rd Summative Assessment: "))
    fe = int(input("Please enter your grade on your Final Examination: "))

    total = ((cp1+cp2+cp3+cp4+cp5) * 0.3) + ((sa1+sa2+sa3) * 0.3) + (fe * 0.4)

    if total >= 90:
        chargrade = "A"
    elif total >= 80:
        chargrade = "B"
    elif total >= 70:
        chargrade = "C"
    elif total >= 60:
        chargrade = "D"
    else:
        chargrade = "F"

    students.append((surname, total, chargrade))

print("\n")
print(" Name\tAverage Grade\tLetter Grade")
for name, grade, letter in students:
    print("\n",name,"\t|\t",grade,"\t|\t",letter)